'use-strict'

app.config(function ($stateProvider) {

  $stateProvider.state('clientSearchResults', {
    url: '/search',
    templateUrl: 'js/app/templates/client-search-results.state.html',
    controller: 'SearchCtrl',
    resolve: {
    	clientsList: function(ClientFactory, $stateParams) {
            
            return ClientFactory.get_clients($stateParams.client_name, $stateParams.phone_number);
        }
    }
  });

});