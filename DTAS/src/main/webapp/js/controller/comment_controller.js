/**
 * Created by Michał (Krokogator) on 08.11.2016.
 */


angular.module('dtas').controller('CommentController', ['$scope', 'CommentService', function($scope, CommentService) {

    var self = this;
    self.comment={id:null,author:null,content:'',post:{id:null},createDateTime:null};
    self.comments=[];
    self.commentsByPost=[];

    self.searchByPost = searchByPost;
    self.submit = submit;
    self.edit = edit;
    self.remove = remove;
    self.reset = reset;
    self.resetAll = resetAll;
    self.setPost = setPost;
    self.editMode = editMode;
    self.updateComment = updateComment;
    self.deleteComment = deleteComment;


    fetchAllComments();

    function fetchAllComments(){
        CommentService.fetchAllComments()
            .then(
                function(d) {
                    self.comments = d;

                },
                function(errResponse){
                    console.error('Error while fetching Comments');
                }
            );
    }

    function fetchCommentsByPost(post){

        CommentService.fetchCommentsByPost(post)
            .then(
                function (d) {
                    self.commentsByPost = d;
                    for(var i = 0; i < self.commentsByPost.length; i++){
                        self.commentsByPost[i].createDateTime=prettyDateTime(self.commentsByPost[i].createDateTime);
                    }
                },
                function (errResponse) {
                    console.error('Error while fetching posts by author (ctrl)');
                }
            );
    }

    function searchByPost(post) {
        console.log('Search Posts By Post', post);
        fetchCommentsByPost(post);
    }

    function createComment(comment){
        CommentService.createComment(comment)
            .then(
                fetchAllComments,
                searchByPost(self.comment.post.id),
                function(errResponse){
                    console.error('Error while creating Comment');
                }
            );
    }

    // function updateComment(comment, id){
    //     CommentService.updateComment(comment, id)
    //         .then(
    //             fetchAllComments,
    //             function(errResponse){
    //                 console.error('Error while updating Comment');
    //             }
    //         );
    // }

    function updateComment(comment){
        CommentService.updateComment(comment)
            .then(
                fetchAllComments(),
                window.location = "#/post/"+comment.post.id,
                function(errResponse){
                    console.error('Error while updating Comment');
                }
            );
    }

    function deleteComment(id,postid){
        CommentService.deleteComment(id)
            .then(
                fetchAllComments(),
                //window.location.reload(),
                searchByPost(postid),
                function(errResponse){
                    console.error('Error while deleting Comment');
                }
            );
    }

    function setPost(postid){
        self.comment.post.id=postid;
        console.log('Post ID: ', postid);
    }

    function editMode(id){
        window.location = "#/editcomment/"+id;
    }

    function submit() {
        if(self.comment.id===null){
            console.log('Saving New Comment', self.comment);
            createComment(self.comment);

        }else{
            updateComment(self.comment, self.comment.id);
            console.log('Comment updated with id ', self.comment.id);
        }
        reset();
    }

    function edit(id){
        console.log('id to be edited', id);
        for(var i = 0; i < self.comments.length; i++){
            if(self.comments[i].id === id) {
                self.comment = angular.copy(self.comments[i]);
                break;
            }
        }
    }

    function remove(id,list){
        console.log('id to be deleted', id);
        if(self.comment.id === id) {
            reset();
        }
        deleteComment(id,list.post.id);
    }

    function reset(){
        self.comment={id:null,author:null,content:'',post:{id:null},createDateTime:null};
        $scope.myForm.$setPristine();
    }

    function resetAll(){
        self.comment={id:null,author:null,content:'',post:{id:null},createDateTime:null};
        self.comments=[];
        self.commentsByPost=[];
    }


}])