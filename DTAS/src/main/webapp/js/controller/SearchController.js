'use strict';


angular.module('dtas').controller('SearchController', ['$scope', '$state', '$location', 'UserService', 'PostService', function($scope, $state, $location, UserService, PostService) {
    var self = this;

    self.username = '';
    self.title = '';

    self.results = [];
    self.showResults = false;
    self.notFound = false;
    self.notFoundPosts = false;

    self.searchUsers = searchUsers;
    self.searchPosts = searchPosts;


    function searchUsers(){

        self.showResults = false;
        self.notFound = false;
        self.results = [];

        if(self.username !== '')
        {
            UserService.searchUser(self.username).then(
                function(d){
                    self.results = d;
                    self.showResults = true;
                },
                function (errResponse) {
                    self.notFound = true;
                }
            );
        }
    }

    function searchPosts(){

        self.showResults = false;
        self.notFoundPosts = false;
        self.results = [];

        if(self.title !== '')
        {
            PostService.fetchPostsByTitle(self.title).then(
                function (d) {
                    self.results = d;
                    self.showResults = true;
                },
                function (errResponse) {
                    self.notFoundPosts = true;
                }
            );
        }
    }

}]);