package dtas.repository;

import dtas.model.Comment;
import dtas.model.Post;
import dtas.model.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

/**
 * Created by Michał (Krokogator) on 30.10.2016.
 */

public interface CommentRepository extends JpaRepository<Comment, Long> {

    Comment findById(long id);
    List<Comment> findByContentContaining(String content);
    List<Comment> findByPost(Post post);
    List<Comment> findByAuthor(User author);
}
