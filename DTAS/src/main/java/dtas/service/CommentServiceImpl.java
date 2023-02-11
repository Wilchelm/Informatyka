package dtas.service;

import dtas.model.Comment;
import dtas.model.Post;
import dtas.model.User;
import dtas.repository.CommentRepository;
import org.springframework.stereotype.Component;

import java.util.List;

/**
 * Created by Michał (Krokogator) on 30.10.2016.
 */

@Component("commentService")
public class CommentServiceImpl implements CommentService {

    private final CommentRepository commentRepository;

    public CommentServiceImpl(CommentRepository commentRepository) {
        this.commentRepository = commentRepository;
    }

    @Override
    public Comment findById(long id) {

        return commentRepository.findById(id);
    }

    @Override
    public List<Comment> findAllComments() {

        return commentRepository.findAll();
    }

    @Override
    public List<Comment> findByCommentContaining(String content) {

        return commentRepository.findByContentContaining(content);
    }

    @Override
    public List<Comment> findByPost(Post post) {

        return commentRepository.findByPost(post);
    }

    @Override
    public List<Comment> findByAuthor(User author) {

        return commentRepository.findByAuthor(author);
    }

    @Override
    public void saveComment(Comment comment) {

        commentRepository.save(comment);
    }

    @Override
    public void updateComment(Comment comment) {

        commentRepository.save(comment);
    }


    @Override
    public void deleteComment(Comment comment) {

        commentRepository.delete(comment);
    }
}
