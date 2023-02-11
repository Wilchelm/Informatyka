'use strict';

angular.module('dtas').factory('UserService', ['$http', '$q', function($http, $q){

    var REST_SERVICE_URI = 'http://localhost:8080/v1/users';

    var factory = {
        fetchRecentlyRegistered: fetchRecentlyRegistered,
        fetchAllUsers: fetchAllUsers,
        fetchActiveUser: fetchActiveUser,
        createUser: createUser,
        updateUser: updateUser,
        deleteUser: deleteUser,
        loginUser: loginUser,
        logoutUser: logoutUser,
        getUserById: getUserById,
        searchUser: searchUser
    };

    return factory;

    function fetchRecentlyRegistered() {
        var deferred = $q.defer();
        $http.get(REST_SERVICE_URI+"?orderBy=registrationDate")
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }

    function fetchActiveUser() {
        var deferred = $q.defer();
        $http.get(REST_SERVICE_URI+"/get-active-commands")
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }

    function loginUser(name, password)
    {
        var deferred = $q.defer();
        $http.get("http://localhost:8080/v1/login-commands?name="+name+"&password="+password)
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }

    function getUserById(id)
    {
        var deferred = $q.defer();
        $http.get(REST_SERVICE_URI+"/"+id)
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }

    function logoutUser()
    {
        var deferred = $q.defer();
        $http.get("http://localhost:8080/v1/logout-commands")
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }

    function fetchAllUsers() {
        var deferred = $q.defer();
        $http.get(REST_SERVICE_URI)
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }

    function createUser(user) {
        var deferred = $q.defer();
        $http.post(REST_SERVICE_URI, user)
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }


    function updateUser(user, id) {
        var deferred = $q.defer();
        $http.put(REST_SERVICE_URI+"/"+id, user)
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }

    function deleteUser(id) {
        var deferred = $q.defer();
        $http.delete(REST_SERVICE_URI+"/"+id)
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }


    function searchUser(username) {
        var deferred = $q.defer();
        $http.get(REST_SERVICE_URI+'?name='+username)
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }

}]);