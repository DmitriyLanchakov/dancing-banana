'use-strict'

app.config(function ($stateProvider) {

  $stateProvider.state('shelterHome', {
    url: '/coc_id/:coc_id', // hard coded for now to coc_id = 10
    templateUrl: 'js/app/templates/shelter-home.html',
    controller: 'MainCtrl',
    resolve: {
        coc: function($stateParams, CocFactory) {
            console.log($stateParams.coc_id)
            // var coc_id = 1;
            return CocFactory.get_coc_info($stateParams.coc_id);
        }
    }
  });

});
