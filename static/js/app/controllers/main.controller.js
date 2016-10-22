'use-strict'

app.controller('MainCtrl', function (ClientFactory) {

	ClientFactory.get_client_info(12);

});