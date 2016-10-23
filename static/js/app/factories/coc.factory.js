'use-strict'

app.factory('CocFactory', function ($http) {

  function getData (res) { return res.data; }

  return {

    get_coc_info: function(coc_id) {
      // Return total beds, available beds, and pending request/referrals

      return $http.post('../get_coc_info', { 
          id: coc_id 
        }).then(getData);
    },

    grant_bed: function(client_id, coc_id) {
      // Reduce number of beds by one. Return success.

      // TODO: Update the number of beds available on the front end.
      return $http.put('../grant_bed', { 
          client_id: client_id, 
          coc_location_id: coc_id 
        }).then(getData);
    },

    get_cocs: function(client_id, location, coc_type) {
      // Return filterd list of CoC's.
      return $http.post('../get_cocs', { 
          client_id: client_id, 
          location: location, 
          coc_type: coc_type 
        }).then(getData);
    },

    ask_for_help: function(coc_id) {
      // Return CoC name and phone number.
      return $http.post('../ask_for_help', {
          id: coc_id
        }).then(getData);
    }
  }

  });