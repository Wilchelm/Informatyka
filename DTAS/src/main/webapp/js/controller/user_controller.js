'use strict';

angular.module('dtas').controller('UserController', ['$scope', '$state', '$location', 'UserService', function($scope, $state, $location, UserService) {
    var self = this;

    $scope.loginData = {};
    self.user={id:null,name:'',lastSeen:'',mail:'',password:'',password2:'',registrationDateTime:''};
    self.users=[];
    self.recentlyRegistered = [];
    self.errorMessage = '';

    self.isLogged = isLogged;
    self.login = login;
    self.logout = logout;
    self.submit = submit;
    self.edit = edit;
    self.remove = remove;
    self.reset = reset;

    fetchActiveUser();

    function isLogged(){
        return self.user.id != null;
    }

    function fetchActiveUser(){
        UserService.fetchActiveUser().then(
            function (d) {
                self.user = d;
            },
            function (errResponse) {
                self.user={id:null,name:'',lastSeen:'',mail:'',password:'',password2:'',registrationDateTime:''};
            }
        );
    }

    fetchRecentlyRegistered();

    function fetchRecentlyRegistered() {

        UserService.fetchRecentlyRegistered()
            .then(
                function (d) {
                    self.recentlyRegistered = d;
                },
                function (errResponse) {
                    console.error('Error while fetching recently registered users (ctrl)');
                }
            );
    }

    fetchAllUsers();

    function fetchAllUsers(){
        UserService.fetchAllUsers()
            .then(
                function(d) {
                    self.users = d;
                },
                function(errResponse){
                    console.error('Error while fetching Users');
                }
            );
    }

    function createUser(user){
        UserService.createUser(user)
            .then(
                function(d)
                {
                    reset();
                    window.location = "#/home";
                },
                function(errResponse){
                    $scope.errormsg = "Błąd " + errResponse.status + ": " + errResponse.data.message;
                }
            );
    }

    function updateUser(user, id){
        UserService.updateUser(user, id)
            .then(
                function(errResponse){
                    alert("Błąd " + errResponse.status + ": " + errResponse.data.message);
                }
            );
    }

    function deleteUser(id){
        UserService.deleteUser(id)
            .then(
                function (d) {
                    fetchActiveUser();
                    $state.reload();
                },
                function(errResponse){
                    console.error('Error while deleting User');
                }
            );
    }

    function login(){
        if(self.user.name!==null && self.user.password !== null)
        {
            UserService.loginUser($scope.loginData.name, $scope.loginData.password)
            .then(
                function (d) {
                    fetchActiveUser();
                    $state.reload();
                },
                function(errResponse){
                    self.errorMessage = "Wprowadzone dane logowania są nieprawidłowe";
                    alert(self.errorMessage);
                }
            );
        }
    }

    function logout(){
        UserService.logoutUser()
            .then(
                function (d) {
                    fetchActiveUser();
                    $state.reload();
                },
                function(errResponse){
                    console.error('Error while logging user out');
                }
            );
        reset();
    }

    function submit() {

        if(self.user.password !== self.user.password2)
        {
            $scope.errormsg = "Podane hasła są różne!";
            return;
        }

        if(self.user.id===null){
            createUser(self.user);
        }else{
            updateUser(self.user, self.user.id);
        }
    }

    function edit(id){
        console.log('id to be edited', id);
        for(var i = 0; i < self.users.length; i++){
            if(self.users[i].id === id) {
                self.user = angular.copy(self.users[i]);
                break;
            }
        }
    }

    function remove(id){
        console.log('id to be deleted', id);
        if(self.user.id === id) {//clean form if the user to be deleted is shown there.
            reset();
        }
        deleteUser(id);
    }


    function reset(){
        self.user={id:null,username:'',address:'',email:''};
        $scope.myForm.$setPristine(); //reset Form
    }

}]);