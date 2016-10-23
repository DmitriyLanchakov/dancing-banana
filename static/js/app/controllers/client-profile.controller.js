'use-strict'

app.controller('ClientProfileCtrl', function ($scope, $state, $rootScope, ClientFactory, CocFactory, client) {

	var coc_id = localStorage.getItem('coc_id');
	var coc_name = localStorage.getItem('coc_name');

	$scope.client = client.data;
	$scope.events = {};

	$scope.submitEdit = function() {
		// Update the client (Remember! this is an async function)
		console.log($scope.client)
		ClientFactory.update_client_info($scope.client)
		alert("Edits saved.");
	}

	$scope.grant_bed = function() {
		console.log('you got a bed', coc_id)

		// TODO:
		// make a 'success' modal
		CocFactory.grant_bed($scope.client.id, coc_id).then(function(){
			alert('A bed has been reserved for this client.');
			$state.go('shelterHome')
		})
	}


	$scope.log_notes = function(details) {
		// update events in state
		// TODO: make sure that coc name is updated
		var event = {
			coc_name: coc_name,
			event_type: 'logged note',
			client_id: $scope.client.id,
			details: details
		}
		$scope.client.events.push(event);

		// update event in database
		ClientFactory.log_note($scope.client.id, coc_id, details)

	}

});