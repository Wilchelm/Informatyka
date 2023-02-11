
'use strict';

angular.module('dtas').factory('PostService', ['$http', '$q', function($http, $q){

    var REST_SERVICE_URI = 'http://localhost:8080/v1/posts';

    var factory = {
        fetchRecentlyCreated: fetchRecentlyCreated,
        fetchPostsByTitle : fetchPostsByTitle,
        fetchPostsByAuthor : fetchPostsByAuthor,
        fetchAllPosts: fetchAllPosts,
        createPost: createPost,
        updatePost: updatePost,
        deletePost: deletePost,
        getPostById: getPostById,
        imageId: imageId
    };

    return factory;

    function imageId(id) {
        var deferred = $q.defer();
        $http.get('http://localhost:8080/v1/files/users/'+id)
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    console.error('Error while fetching image service');
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }

    function fetchPostsByTitle(title) {
        var deferred = $q.defer();
        $http.get(REST_SERVICE_URI+"?title="+title)
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

    function fetchPostsByAuthor(author) {
        var deferred = $q.defer();
        $http.get("/v1/users/"+author+"/posts")
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    console.error('Error while fetching posts by author');
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }

    function fetchRecentlyCreated() {
        var deferred = $q.defer();
        $http.get(REST_SERVICE_URI+"?orderBy=createDate")
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    console.error('Error while fetching recently created posts');
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }

    function fetchAllPosts() {
        var deferred = $q.defer();
        $http.get(REST_SERVICE_URI)
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    console.error('Error while fetching Posts');
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }

    function createPost(post) {
        var deferred = $q.defer();
        $http.post(REST_SERVICE_URI, post)
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    console.error('Error while creating Post');
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }


    function updatePost(post) {
        var deferred = $q.defer();
        $http.put(REST_SERVICE_URI+'/'+ post.id, post)
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    console.error('Error while updating Post');
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }

    function deletePost(id) {
        var deferred = $q.defer();
        $http.delete(REST_SERVICE_URI+'/'+id)
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    console.error('Error while deleting Post (Service)');
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }

    function getPostById(id)
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


}]);