var app = angular.module('app', [
    'facto',
    'ngMaterial',
    'ngMessages'
]);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[{');
    $interpolateProvider.endSymbol('}]');
});

app.controller('ctrl', function ($timeout, $scope, feelItFactory, $mdDialog) {

    var ctrl = this;

    ctrl.hashtags = [];

    feelItFactory.getTendances().then(function (value) {
        ctrl.hashtags = angular.copy(value);
        console.log('getTendances', value);
    }, function (reason) {
        console.error('getTendances error', reason);
    });

    ctrl.searchForTweet = function (research) {
        ctrl.researchDone = null;
        ctrl.researchResult = null;
        $mdDialog.show({
            controller: DialogController,
            template: '<md-dialog aria-label="List dialog" class="modal-preloader" layout="row" layout-align="center center">' +
            '<div>\n' +
            '    <md-progress-circular aria-label="preloader" md-mode="indeterminate"></md-progress-circular>\n' +
            '</div>' +
            '</md-dialog>',
            parent: angular.element(document.html),
            clickOutsideToClose:false
        });
        feelItFactory.getTweets(research).then(function (value) {
            console.log('getTweets', value);
            ctrl.researchDone = research;
            ctrl.researchResult = value;
            $mdDialog.hide()
        }, function (reason) {
            console.error('error getTweets', reason);
        });
    };

    function DialogController($scope, $mdDialog) {
        $scope.hide = function() {
            $mdDialog.hide();
        };

        $scope.cancel = function() {
            $mdDialog.cancel();
        };

        $scope.answer = function(answer) {
            $mdDialog.hide(answer);
        };
    }

    /*
    feelItFactory.getTweets('test').then(function (value) {

        console.log('getTweets', value);
    }, function (reason) {
        console.error('error getTweets', reason);
    })
    */

});