'use-strict'

app.controller('MainCtrl', function ($scope, $state, $rootScope, ClientFactory, CocFactory, coc) {

	localStorage.setItem('coc_id', coc.data.id);
  localStorage.setItem('coc_name', coc.data.name);

	// Coc Information
	$scope.name = coc.data.name;
	$scope.total_beds = coc.data.beds_total;
	$scope.available_beds = coc.data.beds_available;
	$scope.referrals_list = coc.data.events;

	$scope.client = {};

	$scope.search = function() {
		// Search for a client

		// go to the client-search-results state (make this a child state?)
		$state.go('clientSearchResults', {
			client_name: $scope.client.name,
			phone_number: $scope.client.phoneNumber
		})
		
	}

	// // Get total number of beds, available beds, and list of referrals

	// // get it through the url query
	// function getParameterByName(name, url) {
 //    if (!url) {
 //      url = window.location.href;
 //    }
 //    name = name.replace(/[\[\]]/g, "\\$&");
 //    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
 //        results = regex.exec(url);
 //    if (!results) return null;
 //    if (!results[2]) return '';
 //    return decodeURIComponent(results[2].replace(/\+/g, " "));
	// }

	// var coc_id = getParameterByName('id'); 

	// // This is is in the resolve statement for now
	// CocFactory.get_coc_info(coc_id)
	// 	.then(function(coc) {
	// 		// display information on page
	// 		console.log(coc);
	// 		$scope.total_beds = coc.beds_total;
	// 		$scope.available_beds = coc.beds_available;
	// 		$scope.referrals_list = coc.events;
	// 	})

	


})