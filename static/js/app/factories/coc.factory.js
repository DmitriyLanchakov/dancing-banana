'use-strict'

app.factory('CocFactory', function ($http) {

  function getData (res) { 
    console.log(res.data);

    return res.data; 
  }

  return {
    get_coc_info: function(coc_location) {
      // Return total beds, available beds, and pending request/referrals

      return $http.get('../get_coc_info', { coc_location: coc_location })
        .then(getData);

    },
    grant_bed: function(client_id, coc_id) {
      // Reduce number of beds by one. Return success. 
      // TODO: Update the number of beds available on the front end.

      return $http.put('../grant_bed', { client_id: client_id, coc_location: coc_location })
        .then(getData);

    },
    get_cocs: function(client_id, location, coc_type) {
      // Return filterd list of CoC's.

      return $http.get('../get_cocs', { client_id: client_id, location: location, coc_type: coc_type })
        .then(getData);

    },
    ask_for_help: function(coc_id) {
      // Return CoC name and phone number.

      return $http.get('../ask_for_help', {coc_id: coc_id})
        .then(getData);

    }
  }

  });