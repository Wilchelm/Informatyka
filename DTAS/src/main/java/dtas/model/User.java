package dtas.model;

import com.fasterxml.jackson.annotation.JsonView;
import dtas.HashingTool;
import dtas.ViewsContainer;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.HashSet;
import java.util.Set;

/**
 * @author Arkadiusz Rosiak (http://www.rosiak.it)
 * @date 2016-10-10
 */

@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @JsonView(ViewsContainer.UserSummary.class)
    private long id;

    @Column(nullable = false)
    @JsonView(ViewsContainer.UserSummary.class)
    private String name;

    @Column(nullable = false)
    @JsonView(ViewsContainer.UserDetails.class)
    private LocalDateTime registrationDateTime;

    @Column(nullable = false)
    @JsonView(ViewsContainer.UserSummary.class)
    private String mail;

    @Column(nullable = false)
    private String password;

    @Column
    @JsonView(ViewsContainer.UserSummary.class)
    private LocalDateTime lastSeen;

    @OneToMany(fetch = FetchType.EAGER, mappedBy = "author", orphanRemoval = false)
    private Set<Post> posts = new HashSet<>();

    public User(){
        registrationDateTime = LocalDateTime.now();
    }

    public User(String name, String mail, String password) {
        this();
        this.name = name;
        this.mail = mail;
        this.setPassword(password);
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public LocalDateTime getRegistrationDateTime() {
        return registrationDateTime;
    }

    public void setRegistrationDateTime(LocalDateTime registrationDateTime)
    {
        this.registrationDateTime = registrationDateTime;
    }

    public String getMail() {
        return mail;
    }

    public void setMail(String mail) {
        this.mail = mail;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = HashingTool.sha512(password);
    }

    public void setRawPassword(String password)
    {
        this.password = password;
    }

    public LocalDateTime getLastSeen() {
        return lastSeen;
    }

    public void setLastSeen(LocalDateTime lastSeen) {
        this.lastSeen = lastSeen;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof User)) return false;

        User user = (User) o;

        if (getId() != user.getId()) return false;
        if (getName() != null ? !getName().equals(user.getName()) : user.getName() != null) return false;
        return getMail() != null ? getMail().equals(user.getMail()) : user.getMail() == null;

    }

    @Override
    public int hashCode() {
        int result = (int) (getId() ^ (getId() >>> 32));
        result = 31 * result + (getName() != null ? getName().hashCode() : 0);
        result = 31 * result + (getMail() != null ? getMail().hashCode() : 0);
        return result;
    }
}
