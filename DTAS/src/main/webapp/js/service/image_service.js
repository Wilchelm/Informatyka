/**
 * Created by Damin Walony.
 */


function dropzone() {

    return function(scope, element, attrs) {

        var config = {
            url: 'http://localhost:8080/v1/upload',
            maxFilesize: 2048,
            paramName: "files",
            maxThumbnailFilesize: 10,
            parallelUploads: 1,
            autoProcessQueue: false
        };

        var eventHandlers = {
            'addedfile': function(file) {
                scope.file = file;
                if (this.files[1]!=null) {
                    this.removeFile(this.files[0]);
                }
                scope.$apply(function() {
                    scope.fileAdded = true;
                });
            },

            'success': function (file, response) {
            }
        };

        dropzone = new Dropzone(element[0], config);

        angular.forEach(eventHandlers, function(handler, event) {
            dropzone.on(event, handler);
        });

        scope.processDropzone = function() {
            dropzone.processQueue();
        };

        scope.resetDropzone = function() {
            dropzone.removeAllFiles();
        }
    }
}

angular.module('dtas').directive('dropzone', dropzone);