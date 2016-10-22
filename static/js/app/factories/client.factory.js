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
          client_name: client_name, 
          phone_number: phone_number
        }).then(getData);
      
    },
    update_client_info: function (profile_info, client_id) {
      // Update or add client. Return success or failure.

      // post or put?
      return $http.put('../update_client_info', { client_id: client_id,
        profile_info: profile_info })
        .then(getData);
      
    },
    get_client_info: function (client_id) {
      // Return client profile info and event info
      
      return $http.get('../get_client_info', { client_id: client_id })
        .then(getData);
    },
    log_note: function (client_id, coc_id) {
      // Update comments in events

      // post or put?
      return $http.post('../log_note', 
          { 
            client_id: client_id, 
            coc_id: coc_id
          })
          .then(getData);
    },
    submit_referral: function(client_id, to_coc_id, from_coc_id, comments) {
      // Create new event instance. Update Coc with new referral. Return success.

      return $http.post('../submit_referral', { client_id: client_id, to_coc_id: to_coc_id, from_coc_id: from_coc_id, comments: comments })
        .then(getData);

    }
  };

});