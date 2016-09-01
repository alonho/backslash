import DS from 'ember-data';
import Ember from 'ember';
import HasLogicalId from '../mixins/has-logical-id';

export default DS.Model.extend(HasLogicalId, {

    archived: DS.attr('boolean'),
    investigated: DS.attr('boolean'),

    start_time: DS.attr('number'),
    end_time: DS.attr('number'),

    is_abandoned: DS.attr('boolean'),

    in_pdb: DS.attr('boolean'),

    infrastructure: DS.attr(),

    num_error_tests: DS.attr('number'),
    num_errors: DS.attr('number'),
    num_failed_tests: DS.attr('number'),
    num_finished_tests: DS.attr('number'),
    num_skipped_tests: DS.attr('number'),

    ran_all_tests: function() {
        if (this.get('total_num_tests') === null) {
            return true;
        }
        return parseInt(this.get('num_finished_tests')) === parseInt(this.get('total_num_tests'));
    }.property('num_finished_tests', 'total_num_tests'),

    has_tests_left_to_run: Ember.computed.not('ran_all_tests'),


    total_num_tests: DS.attr('number'),
    hostname: DS.attr(),

    num_warnings: DS.attr('number'),
    num_test_warnings: DS.attr('number'),
    num_comments:DS.attr('number'),

    next_keepalive: DS.attr('number'),
    related: DS.attr(),

    total_num_warnings: function() {
        return this.get('num_warnings') + this.get('num_test_warnings');
    }.property('num_warnings', 'num_test_warnings'),

    status: DS.attr('string'),
    status_lower: function() {
        return this.get('status').toLowerCase();
    }.property('status'),

    computed_status: function() {
	if (this.get('is_abandoned')) {
	    return 'ABANDONED';
	}
	if (this.get('is_interrupted')) {
	    return 'INTERRUPTED';
	}
	return this.get('status');
    }.property('status', 'is_abandoned', 'is_interrupted'),

    is_interrupted: function() {
	return this.get('end_time') != null && this.get('has_tests_left_to_run');
    }.property('end_time', 'has_tests_left_to_run'),

    subjects: DS.attr(),

    type: DS.attr(),

    user_id: DS.attr(),
    user_email: DS.attr(),
    user_display_name: DS.attr(),

    real_email: DS.attr(),

    is_delegate: Ember.computed.notEmpty('real_email'),

    is_running: function() {
        return this.get('status') === 'RUNNING';
    }.property('status'),

    finished_running: Ember.computed.not('is_running'),


});
