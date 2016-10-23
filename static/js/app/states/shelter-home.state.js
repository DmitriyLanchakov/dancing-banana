'use-strict'

app.config(function ($stateProvider) {

  $stateProvider.state('shelterHome', {
    url: '',
    templateUrl: 'js/app/templates/shelter-home.state.html',
    controller: 'MainCtrl'
    // resolve: {
    // 	dog: function() {
    // 		console.log('in state')
    // 	}
    // }
  });

});