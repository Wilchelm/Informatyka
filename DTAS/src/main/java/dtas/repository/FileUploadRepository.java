package dtas.repository;

import dtas.model.FileUpload;
import dtas.model.Post;
import dtas.model.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.io.File;
import java.util.List;

public interface FileUploadRepository extends JpaRepository<FileUpload, Long>{

    FileUpload findById(Integer id);

    FileUpload findByFilename(String filename);

    FileUpload findByAuthor(User author);

    List<FileUpload> findAll();
}