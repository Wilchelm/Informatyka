package dtas.controller;


import dtas.model.FileUpload;
import dtas.model.User;
import dtas.service.FileUploadService;
import dtas.service.UserService;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.multipart.MultipartHttpServletRequest;
import org.apache.catalina.servlet4preview.http.HttpServletRequest;

import javax.inject.Inject;
import java.io.File;
import java.time.LocalDateTime;
import java.util.Iterator;
import java.util.List;

@CrossOrigin(origins = "*")
@RestController
public class FileController {

    private FileUploadService fileUploadService;
    private UserService userService;

    @Inject
    public FileController(FileUploadService fileUploadService, UserService userService) {
        this.fileUploadService=fileUploadService;
        this.userService=userService;
    }

    // Download a file
    @RequestMapping(
            value = "/v1/download",
            method = RequestMethod.GET
    )
    public ResponseEntity downloadFile(@RequestParam("filename") String filename) {

        FileUpload fileUpload = fileUploadService.findByFilename(filename);

        // No file found based on the supplied filename
        if (fileUpload == null) {
            return new ResponseEntity<>("{}", HttpStatus.NOT_FOUND);
        }

        // Generate the http headers with the file properties
        HttpHeaders headers = new HttpHeaders();
        headers.add("content-disposition", "attachment; filename=" + fileUpload.getFilename());

        // Split the mimeType into primary and sub types
        String primaryType, subType;
        try {
            primaryType = fileUpload.getMimeType().split("/")[0];
            subType = fileUpload.getMimeType().split("/")[1];
        } catch (IndexOutOfBoundsException | NullPointerException ex) {
            return new ResponseEntity<>("{}", HttpStatus.INTERNAL_SERVER_ERROR);
        }

        headers.setContentType(new MediaType(primaryType, subType));

        return new ResponseEntity<>(fileUpload.getFile(), headers, HttpStatus.OK);
    }


    @RequestMapping(
            value = "/v1/upload",
            method = RequestMethod.POST
    )
    public ResponseEntity uploadFile(MultipartHttpServletRequest request, HttpServletRequest request2) {

        User author = (User) request2.getSession().getAttribute("user");

        try {
            Iterator<String> itr = request.getFileNames();

            while (itr.hasNext()) {
                LocalDateTime x = LocalDateTime.now();
                String uploadedFile = itr.next();
                MultipartFile file = request.getFile(uploadedFile);
                String mimeType = file.getContentType();
                String filename = file.getOriginalFilename();
                byte[] bytes = file.getBytes();

                FileUpload newFile = new FileUpload(author, x,filename, bytes, mimeType);

                fileUploadService.uploadFile(newFile);
            }
        }
        catch (Exception e) {
            return new ResponseEntity<>("{}", HttpStatus.INTERNAL_SERVER_ERROR);
        }

        return new ResponseEntity<>("{}", HttpStatus.OK);
    }

    @RequestMapping(value = "/v1/image2/{id}", method = RequestMethod.GET)
            public byte[] loadImage(HttpServletRequest request, @PathVariable Integer id)
    {

        User author = (User) request.getSession().getAttribute("user");

        FileUpload fileUpload = fileUploadService.findById(id);

        byte[] bytes = fileUpload.getFile();

        System.out.print(fileUpload);

        return bytes;

    }

    @RequestMapping(value = "/v1/image/user/{id}", method = RequestMethod.GET)
    public ResponseEntity loadImage2(@PathVariable long id)
    {
        long idd=0;

        List<FileUpload> fileUpload = fileUploadService.findAll();
        for(FileUpload x : fileUpload ){
            if(x.getAuthor().getId()==id){
                idd=x.getId();
            }
        }

        return ResponseEntity.ok(idd);
    }

}

