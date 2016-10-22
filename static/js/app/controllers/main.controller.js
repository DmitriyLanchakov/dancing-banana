'use-strict'

// inject client info before loading the page?

app.controller('MainCtrl', function ($scope, ClientFactory, CocFactory) {

	ClientFactory.get_client_info(12)
	.then(function(client) {
		$scope.client = client;
		console.log("this is the client: ", $scope.client)
	})
	

	CocFactory.get_coc_info()

})