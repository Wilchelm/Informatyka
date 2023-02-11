/**
 * Created by Damin Walony.
 */function fileCtrl ($scope) {

    $scope.uploadFile = function() {
        $scope.processDropzone();
    };

    $scope.reset = function() {
        $scope.resetDropzone();
    };
}

angular.module('dtas').controller('fileCtrl', fileCtrl);