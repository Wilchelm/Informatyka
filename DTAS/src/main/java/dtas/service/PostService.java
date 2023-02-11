package dtas.service;

import dtas.model.Post;
import dtas.model.User;

import java.util.List;

/**
 * Created by Dawid on 2016-10-18.
 */

public interface PostService {

    Post findById(Long id);

    List<Post> findAllPosts();

    List<Post> findByTitle(String title);

    List<Post> findByAuthor(User author);

    List<Post> findTop5PostsOrderedBy(String orderBy);

    void savePost(Post post);

    void updatePost(Post post);

    void deletePost(Post post);
}
