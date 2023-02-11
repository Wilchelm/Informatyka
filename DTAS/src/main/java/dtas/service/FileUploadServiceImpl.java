package dtas.service;


import dtas.model.FileUpload;
import dtas.model.Post;
import dtas.model.User;
import dtas.repository.FileUploadRepository;
import org.springframework.stereotype.Component;

import java.util.List;

@Component("fileUploadService")
public class FileUploadServiceImpl implements FileUploadService {

    private final FileUploadRepository fileUploadRepository;

    public FileUploadServiceImpl(FileUploadRepository fileUploadRepository) {
        this.fileUploadRepository = fileUploadRepository;
    }

    @Override
    public FileUpload findByFilename (String filename) {
        return fileUploadRepository.findByFilename(filename);
    }

    @Override
    public void uploadFile(FileUpload doc) {
        fileUploadRepository.saveAndFlush(doc);
    }

    @Override
    public FileUpload findById(Integer id) {
        return fileUploadRepository.findById(id);
    }

    @Override
    public void deleteFile(FileUpload doc) {
        fileUploadRepository.delete(doc);
    }

    @Override
    public FileUpload findByAuthor(User author) {
        return fileUploadRepository.findByAuthor(author);
    }

    @Override
    public List<FileUpload> findAll() {return fileUploadRepository.findAll();}
}
