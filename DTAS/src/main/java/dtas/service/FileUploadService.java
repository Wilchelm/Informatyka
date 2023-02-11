package dtas.service;

import dtas.model.FileUpload;
import dtas.model.Post;
import dtas.model.User;

import java.io.File;
import java.util.List;

public interface FileUploadService {

    FileUpload findById(Integer id);

    FileUpload findByFilename (String filename);

    void uploadFile(FileUpload doc);

    void deleteFile(FileUpload doc);

    FileUpload findByAuthor(User author);

    List<FileUpload> findAll();

}