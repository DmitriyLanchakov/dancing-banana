'use-strict'

app.config(function ($stateProvider) {

  $stateProvider.state('clientSearchResults', {
    url: '/search/:client_name/:phone_number',
    templateUrl: 'js/app/templates/client-search-results.html',
    controller: 'SearchCtrl',
    resolve: {
    	clientsList: function(ClientFactory, $stateParams) {
            console.log('state params',$stateParams);
            
            return ClientFactory.get_clients($stateParams.client_name, $stateParams.phone_number);
        }
    }
  });

});