'use-strict'

app.factory('ClientFactory', function ($http) {

  function getData (res) { 
    console.log(res.data);

    return res.data; 
  }

  return {

    get_clients: function (client_name, phone_number) {
      // Search for client. Return a list of client matches
      return $http.get('../get_clients', { 
          name: client_name, 
          phone_number: phone_number
        }).then(getData);
    },

    update_client_info: function (client) {
      // Update or add client. Return success or failure.

        return $http.put('../update_client_info', { 
            client: client 
          }).then(getData);
    },

    get_client_info: function (client_id) {
      // Return client profile info and event info
      return $http.get('../get_client_info', { 
          id: client_id 
        }).then(getData);
    },

    log_note: function (client_id, coc_id, comments) {
      // Update comments in events

      return $http.post('../log_note', { 
          client_id: client_id, 
          coc_location_id: coc_id,
          event_type: 'logged note',
          details: comments
        }).then(getData);
    },

    submit_referral: function(client_id, to_coc_id, from_coc_id, comments) {
      // Create new event instance. Update Coc with new referral. Return success.

      return $http.post('../submit_referral', { 
          client_id: client_id, 
          coc_location_id: to_coc_id, 
          from_coc_location_id: from_coc_id, 
          event_type: 'referral',
          details: comments 
        }).then(getData);
    }
  };

});