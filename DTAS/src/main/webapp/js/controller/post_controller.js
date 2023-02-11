/**
 * Created by Dawid on 2016-11-04.
 */


angular.module('dtas').controller('PostController', ['$scope', 'PostService', function($scope, PostService) {

    var self = this;
    self.post={id:null,excerpt:'',author:null,title:'',content:'',createDateTime:''};
    self.posts=[];
    self.postsByTitle=[];
    self.postsByAuthor=[];
    self.recentlyCreated = [];
    self.imageid = null;

    self.submit = submit;
    self.search = search;
    self.searchByAuthor = searchByAuthor;
    self.edit = edit;
    self.remove = remove;
    self.reset = reset;
    self.resetAll = resetAll;
    self.tryUpdatePost = tryUpdatePost;
    self.updatePost = updatePost;
    self.deletePost = deletePost;
    self.imageId = imageId;
    self.imageHide = imageHide;


    function imageId (id){

        PostService.imageId(id)
            .then(
                function (d) {
                    if(d==0) {
                        self.imageid = null;
                    }else{self.imageid = d;}
                },
                function (errResponse) {
                    console.error('Error while fetching image controler');
                }
            );
    }

    function imageHide(){
        self.imageid=null;
    }

    function fetchPostsByTitle(title){

        PostService.fetchPostsByTitle(title)
            .then(
                function (d) {
                    self.postsByTitle = d;
                },
                function (errResponse) {
                    console.error('Error while fetching posts by title (ctrl)');
                }
            );
    }

    function fetchPostsByAuthor(author){

        PostService.fetchPostsByAuthor(author)
            .then(
                function (d) {
                    self.postsByAuthor = d;
                },
                function (errResponse) {
                    console.error('Error while fetching posts by author (ctrl)');
                }
            );
    }

    fetchRecentlyCreated();

    function fetchRecentlyCreated() {

        PostService.fetchRecentlyCreated()
            .then(
                function (d) {
                    self.recentlyCreated = d;
                },
                function (errResponse) {
                    console.error('Error while fetching recently created posts (ctrl)');
                }
            );
    }

    fetchAllPosts();

    function fetchAllPosts(){
        PostService.fetchAllPosts()
            .then(
                function(d) {
                    self.posts = d;
                },
                function(errResponse){
                    console.error('Error while fetching Posts');
                }
            );
    }

    function createPost(post){
        PostService.createPost(post)
            .then(
                fetchAllPosts(),
                fetchRecentlyCreated(),
                window.location = "#/home",
                function(errResponse){
                    console.error('Error while creating Post');
                }
            );
    }

    function tryUpdatePost(id){
        window.location = "#/editpost/"+id;
    }

    function updatePost(post){
        PostService.updatePost(post)
            .then(
                fetchAllPosts,
                window.location = "#/post/"+post.id,
                function(errResponse){
                    console.error('Error while updating Post');
                }
            );
    }

    function deletePost(id){
        PostService.deletePost(id)
            .then(
                fetchAllPosts,
                window.location = "#/home",
                function(errResponse){
                    console.error('Error while deleting Post (Controler)');
                }
            );
    }

    function submit() {
        if(self.post.id===null){
            console.log('Saving New Post', self.post);
            createPost(self.post);
        }else{
            updatePost(self.post, self.post.id);
            console.log('Post updated with id ', self.post.id);
        }
        reset();
    }

    function search() {
        console.log('Search Posts By Title', self.post.title);
        fetchPostsByTitle(self.post.title);

        reset();
    }

    function searchByAuthor(author) {
        console.log('Search Posts By Author', author);
        fetchPostsByAuthor(author);
    }

    function edit(id){
        console.log('id to be edited', id);
        for(var i = 0; i < self.posts.length; i++){
            if(self.posts[i].id === id) {
                self.post = angular.copy(self.posts[i]);
                break;
            }
        }
    }

    function remove(id){
        console.log('id to be deleted', id);
        if(self.post.id === id) {
            reset();
        }
        deletePost(id);
    }

    function reset(){
        self.post={id:null,author:null,title:'',content:'',createDate:''};
        $scope.myForm.$setPristine();
    }
    function resetAll(){
        self.post={id:null,author:null,title:'',content:'',createDate:''};
        self.posts=[];
        self.postsByTitle=[];
        self.postsByAuthor=[];
        self.recentlyCreated = [];
    }
}]);