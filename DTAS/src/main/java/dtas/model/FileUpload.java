package dtas.model;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "files")
public class FileUpload {

    public FileUpload(User author, LocalDateTime createDateTime, String filename, byte[] file, String mimeType) {
        this.author=author;
        this.createDateTime=createDateTime;
        this.file = file;
        this.filename = filename;
        this.mimeType = mimeType;

    }

    public FileUpload() {
        // Default Constructor
    }

    @Id
    @GeneratedValue (strategy = GenerationType.IDENTITY)
    private Integer id;

    @ManyToOne(optional = false)
    @JoinColumn(name="user")
    private User author;

    public User getAuthor() {
        return author;
    }

    public void setAuthor(User author) {
        this.author = author;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public LocalDateTime getCreateDateTime() {
        return createDateTime;
    }

    public void setCreateDateTime(LocalDateTime createDateTime) {
        this.createDateTime = createDateTime;
    }

    private LocalDateTime createDateTime;

    private String filename;

    @Lob
    private byte[] file;

    private String mimeType;


    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }

    public byte[] getFile() {
        return file;
    }

    public void setFile(byte[] file) {
        this.file = file;
    }

    public String getMimeType() {
        return mimeType;
    }

    public void setMimeType(String mimeType) {
        this.mimeType = mimeType;
    }
}
