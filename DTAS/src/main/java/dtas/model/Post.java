package dtas.model;

import javax.persistence.*;
import java.io.Serializable;
import java.time.LocalDateTime;

/**
 * Created by Dawid on 2016-10-18.
 */

@Entity
@Table(name = "posts")

public class Post implements Serializable {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    @ManyToOne(optional = false)
    @JoinColumn(name="user")
    private User author;

    @Column(nullable = false)
    private LocalDateTime createDateTime;

    @Column(nullable = false)
    private String title;

    @Transient
    private String excerpt;

    @Column(nullable = false)
    private String content;

    public Post(){
        createDateTime = LocalDateTime.now();
    }

    public Post(User author, String title, String content) {
        this();
        this.author = author;
        this.title = title;
        this.content = content;
    }

    public long getId() {

        return id;
    }

    public void setId(long id) {

        this.id = id;
    }

    public User getAuthor() {

        return author;
    }

    public void setAuthor(User author) {

        this.author = author;
    }

    public LocalDateTime getCreateDateTime() {

        return createDateTime;
    }

    public void setCreateDateTime(LocalDateTime createDateTime) {

        this.createDateTime = createDateTime;
    }

    public String getTitle() {

        return title;
    }

    public void setTitle(String title) {

        this.title = title;
    }

    public String getExcerpt(){
        String[] split = content.split(" ");

        StringBuilder sb = new StringBuilder();

        int words = 0;
        for(String s : split){

            sb.append(s).append(" ");

            if(++words > 20){
                break;
            }
        }

        return sb.toString();

    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
}
