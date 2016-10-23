'use-strict'

// inject client info before loading the page?

app.controller('MainCtrl', function ($scope, $state, ClientFactory, CocFactory) {

	$scope.user = {};

	console.log('USER', $scope.user);
	$scope.search = function() {
		
		$state.go('client-search-results', {})
	}

	// Search for a client
	ClientFactory.get_clients($scope.user)
		.then(function(client_list) {
			// go to the client-search-results state (make this a child state?)
		})

	// // Get total number of beds, available beds, and list of referrals
	// // TODO: get the coc_id
	// CocFactory.get_coc_info(GET COC_ID)
	// 	.then(function() {
	// 		// display information on page
	// 		$scope.total_beds;
	// 		$scope.available_beds;
	// 		$scope.referrals_list;
	// 	})

	


})