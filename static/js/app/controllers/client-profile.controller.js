'use-strict'

app.controller('ClientProfileCtrl', function ($scope, $state, ClientFactory, CocFactory, client) {

	$scope.client = client.data;
	$scope.events = {};

	$scope.submitEdit = function() {
		// Update the client (Remember! this is an async function)
		ClientFactory.update_client_info($scope.client)
	}

	$scope.grant_bed = function() {
		console.log('you got a bed')
		
		// TODO: 
		// get the coc_id
		// make a 'success' modal
		CocFactory.grant_bed($scope.client.id, 9).then(function(){
			alert('A bed has been reserved for this client.');
			$state.go('shelterHome')
		})
	}

	// $scope.refer = function() {
	// 	$state.go('', {
			
	// 	})
	// }


	$scope.log_notes = function(details) {
		// update events in state
		var event = {
			// coc_location_id: GET COC_ID
			event_type: 'logged note',
			client_id: $scope.client.id,
			details: details
		}
		$scope.client.events.push(event);

		// update event in database
		ClientFactory.log_note($scope.client.id, 9, details)

	}

});