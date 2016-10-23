'use-strict'

// inject client info before loading the page?

app.controller('SearchCtrl', function ($scope, $state, ClientFactory, CocFactory, clientsList) {

	// TODO: figure out why factory doesn't take care of res.data
	$scope.clientsList = clientsList.data;


	console.log('in search control', $scope.clientsList);

});