import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.route("sessions", { path: "/sessions" });
  this.route("session", { path: "/sessions/:id" }, function() {
    this.route('errors');
    this.route('single_error', { path: "/errors/:index" });
    this.route('warnings');
  });

  this.route("test", { path: "/tests/:test_id" }, function() {
    this.route('errors');
    this.route('single_error', { path: "/errors/:index" });
    this.route('warnings');
  });

  this.route('login', function() {});
  this.route('profile');
  this.route('user', { path: '/users/:email' }, function() {
    this.route('sessions');
    this.route('admin');
    this.route('preferences');
  });
  this.route('authorize-runtoken', { path: '/runtoken/:requestid/authorize' });
  this.route('loading');
  this.route('users');
  this.route('subjects');
  this.route('subject', { path: '/subjects/:name' });
  this.route('test_info', { path: '/test_info/:id' });
  this.route('stats');
  this.route('component-proofing');
  this.route('setup');
  this.route('suites', function() {
    this.route('new');
  });
  this.route('suite', { path: '/suites/:id' }, function() {
    this.route('edit');
  });
});

export default Router;

