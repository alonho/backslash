import DS from 'ember-data';

export default DS.Model.extend({
    action: DS.attr(),
    timestamp: DS.attr(),
    user_email: DS.attr(),
    user_name: DS.attr(),
    text: DS.attr()

});
