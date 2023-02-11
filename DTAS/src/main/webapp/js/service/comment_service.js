/**
 * Created by Michał (Krokogator) on 08.11.2016.
 */

'use strict';

angular.module('dtas').factory('CommentService', ['$http', '$q', function($http, $q){

    var REST_SERVICE_URI = 'http://localhost:8080/v1/comment/';

    var factory = {
        fetchAllComments: fetchAllComments,
        fetchCommentsByPost: fetchCommentsByPost,
        getCommentById: getCommentById,
        createComment: createComment,
        updateComment: updateComment,
        deleteComment: deleteComment
    };

    return factory;

    function fetchAllComments() {
        var deferred = $q.defer();
        $http.get(REST_SERVICE_URI)
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    console.error('Error while fetching Comment');
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }

    function fetchCommentsByPost(post) {
        var deferred = $q.defer();
        $http.get("/v1/post/"+post+"/comments")
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

    function getCommentById(id)
    {
        var deferred = $q.defer();
        $http.get(REST_SERVICE_URI+id)
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

    function createComment(comment) {
        var deferred = $q.defer();
        $http.post(REST_SERVICE_URI, comment)
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    console.error('Error while creating Comment');
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }


    function updateComment(comment) {
        var deferred = $q.defer();
        $http.put(REST_SERVICE_URI+comment.id, comment)
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    console.error('Error while updating Comment');
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }

    function deleteComment(id) {
        var deferred = $q.defer();
        $http.delete(REST_SERVICE_URI+id)
            .then(
                function (response) {
                    deferred.resolve(response.data);
                },
                function(errResponse){
                    console.error('Error while deleting Comment');
                    deferred.reject(errResponse);
                }
            );
        return deferred.promise;
    }


}]);