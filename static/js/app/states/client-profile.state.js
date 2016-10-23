'use-strict'

app.config(function ($stateProvider) {

  $stateProvider.state('clientProfile', {
    url: '/client-profile/:clientId',
    templateUrl: 'js/app/templates/client-profile.state.html',
    controller: 'ClientProfileCtrl',
    resolve: {
    	client: function(ClientFactory, $stateParams) {
            
            return ClientFactory.get_client_info($stateParams.clientId);
        }
    }
  });

});