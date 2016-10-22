'use-strict'

// inject client info before loading the page?

app.controller('MainCtrl', function ($scope, ClientFactory, CocFactory) {

	ClientFactory.get_client_info(12)
	.then(function(client) {
		$scope.client = client;
		console.log("this is the client: ", $scope.client)
	})
	// Search for a client
	ClientFactory.get_clients(GET CLIENT INFO)
		.then(function(client_list) {
			// go to the client-search-results state (make this a child state?)
		})

	// Get total number of beds, available beds, and list of referrals
	CocFactory.get_coc_info(GET COC_ID)
		.then(function() {
			// display information on page
			$scope.total_beds;
			$scope.available_beds;
			$scope.referrals_list;
		})

	


})