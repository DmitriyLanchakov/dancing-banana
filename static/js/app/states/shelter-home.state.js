'use-strict'

app.config(function ($stateProvider) {

  $stateProvider.state('newPlaylist', {
    url: '',
    templateUrl: '/js/app/templates/shelter-home.state.html',
    controller: 'MainCtrl'
    // resolve:
  });

});