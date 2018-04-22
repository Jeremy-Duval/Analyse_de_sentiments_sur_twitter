angular.module('facto', []).factory('feelItFactory', ['$http', function($http){
    var facto = this;

    facto.getTendances = function () {
        return $http.get('/getTendances').then(function (value) {
            return value.data.items
        }, function (reason) {
            return reason.data
        })
    };

    facto.getTweets = function (research) {
        var req = {
            method: 'GET',
            url: '/getTweets',
            params: { research: research }
        };
        return $http(req).then(function (value) {
            console.log('values get tweets', value);
            return value.data.items
        }, function (reason) {
            return reason.data
        })
    };

    return facto;
}]);