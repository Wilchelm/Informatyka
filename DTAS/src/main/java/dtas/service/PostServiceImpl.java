package dtas.service;

import dtas.model.Post;
import dtas.model.User;
import dtas.repository.PostRepository;
import org.springframework.stereotype.Component;

import java.util.Collections;
import java.util.List;

/**
 * Created by Dawid on 2016-10-18.
 */

@Component("postService")
public class PostServiceImpl implements PostService{

    private final PostRepository postRepository;

    public PostServiceImpl(PostRepository postRepository) {

        this.postRepository = postRepository;
    }

    @Override
    public Post findById(Long id) {

        return postRepository.findById(id);
    }

    @Override
    public List<Post> findAllPosts() {

        return postRepository.findAll();
    }

    @Override
    public List<Post> findByTitle(String title) {

        return postRepository.findByTitleContaining(title);
    }

    @Override
    public List<Post> findByAuthor(User author){

        return postRepository.findByAuthor(author);
    }

    @Override
    public List<Post> findTop5PostsOrderedBy(String OrderBy){
        if(OrderBy.toLowerCase().equals("createdate")) {
            return postRepository.findTop5ByOrderByCreateDateTimeDesc();
        }
        return Collections.emptyList();
    }

    @Override
    public void savePost(Post post) {

        postRepository.save(post);
    }

    @Override
    public void updatePost(Post post) {

        postRepository.save(post);
    }

    @Override
    public void deletePost(Post post) {

        postRepository.delete(post);
    }
}
