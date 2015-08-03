import json
import operator

from flask import request


class FilterConfig(object):

    def __init__(self, cfg):
        super(FilterConfig, self).__init__()
        self._cfg = cfg

    def filter(self, iterator, metadata):
        filter_json = self._get_filter_json()
        filter_config = metadata['filter_config'] = self._create_filter_config_dict(filter_json)
        for arg, value in filter_json.items():
            if arg not in self._cfg:
                continue
            f = self._cfg[arg]
            iterator = f.filter(iterator, value)
        return iterator

    def _get_filter_json(self):
        filter_json = request.args.get('filter', None)
        if filter_json is None:
            filter_json = {}
        else:
            try:
                filter_json = json.loads(filter_json)
            except ValueError:
                filter_json = {}
        return filter_json


    def _create_filter_config_dict(self, filter_json):
        returned = [
            {
                'name': name,
                'selected': name in filter_json,
                'value': filter_json.get(name),
                'options': [
                    {'name': opt_name, 'selected': filter_json.get(name, None) == opt_name}
                    for opt_name in f.options]
            }
            for name, f in self._cfg.items()
        ]
        return returned


class ConstFilter(object):

    def __init__(self, field, options):
        super(ConstFilter, self).__init__()
        self.field = field
        self.options = {
            opt_name: opt_val if isinstance(opt_val, tuple) else (operator.eq, opt_val)
            for opt_name, opt_val in options.items()
        }

    def filter(self, iterator, value):
        operator, opt_val = self.options[value]
        iterator = iterator.filter(operator(self.field, opt_val))
        return iterator
