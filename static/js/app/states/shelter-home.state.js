'use-strict'

app.config(function ($stateProvider) {

  $stateProvider.state('shelterHome', {
    url: '', // hard coded for now to coc_id = 10
    templateUrl: 'js/app/templates/shelter-home.html',
    controller: 'MainCtrl',
    resolve: {
        coc: function(CocFactory) {
            var coc_id = 1;
            return CocFactory.get_coc_info(coc_id);
        }
    }
  });

});