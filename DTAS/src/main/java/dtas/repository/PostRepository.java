package dtas.repository;

import dtas.model.Post;
import dtas.model.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

/**
 * Created by Dawid on 2016-10-18.
 */
public interface PostRepository extends JpaRepository<Post, Long> {

    Post findById(long id);

    List<Post> findByTitleContaining(String title);

    List<Post> findByAuthor(User author);

    List<Post> findTop5ByOrderByCreateDateTimeDesc();

}
