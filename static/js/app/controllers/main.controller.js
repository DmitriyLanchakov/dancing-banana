'use-strict'

// inject client info before loading the page?

app.controller('MainCtrl', function ($scope, $state, ClientFactory, CocFactory) {

	$scope.user = {};

	console.log('USER', $scope.user);
	$scope.search = function() {
		// $state.go('clientSearchResults')
		// Search for a client
		ClientFactory.get_clients($scope.user.name, $scope.user.phoneNumber)
			.then(function(client_list) {
				// go to the client-search-results state (make this a child state?)
				// $state.go('clientSearchResults')

				// display the clients
				$scope.client_list = client_list;
			})
		
	}


	// Get total number of beds, available beds, and list of referrals

	// get it through the url query
	function getParameterByName(name, url) {
    if (!url) {
      url = window.location.href;
    }
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
	}

	var coc_id = getParameterByName('id'); 
	console.log(coc_id);


	CocFactory.get_coc_info(coc_id)
		.then(function(coc) {
			// display information on page
			console.log(coc);
			$scope.total_beds;
			$scope.available_beds;
			$scope.referrals_list;
		})

	


})