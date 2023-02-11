package dtas.model;

import org.hibernate.annotations.NotFound;
import org.hibernate.annotations.NotFoundAction;

import javax.persistence.*;
import java.io.Serializable;
import java.time.LocalDateTime;

/**
 * Created by Michał (Krokogator) on 29.10.2016.
 */

@Entity
@Table(name = "comments")

public class Comment implements Serializable{

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    @ManyToOne(optional = false)
    @JoinColumn(name="user")
    private User author;

    @ManyToOne(optional = false)
    @JoinColumn(name="post")
    private Post post;

    @Column(nullable = false)
    private LocalDateTime createDateTime;

    @Column(nullable = false, length = 3000)
    private String content;

    public Comment(){
        createDateTime = LocalDateTime.now();
    }

    public Comment(User author, Post post, String content) {
        this();
        this.author = author;
        this.post = post;
        this.content = content;
    }

    public long getId() { return id; }

    public void setId(long id) { this.id = id; }

    public Post getPost() { return post; }

    public void setPost(Post post) { this.post = post;}

    public User getAuthor() { return author; }

    public void setAuthor(User author) {
        this.author = author;
    }

    public LocalDateTime getCreateDateTime() {return createDateTime;}

    public void setCreateDateTime(LocalDateTime createDateTime) {this.createDateTime = createDateTime;}

    public String getContent() { return content; }

    public void setContent(String content) { this.content = content; }
}
