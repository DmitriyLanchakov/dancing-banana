'use-strict'

app.config(function ($stateProvider, $stateParams) {

  $stateProvider.state('clientSearchResults', {
    url: '/search',
    templateUrl: 'js/app/templates/client-search-results.state.html',
    controller: 'MainCtrl'
    // resolve: {
    // 	clientsList: function(ClientFactory) {
    //         return ClientFactory.get_clients($stateParams.client_name, $stateParams.phone_number);
    //     }
    // }
  });

});