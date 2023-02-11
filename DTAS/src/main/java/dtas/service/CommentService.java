package dtas.service;

import dtas.model.Comment;
import dtas.model.Post;
import dtas.model.User;

import java.util.List;

/**
 * Created by Michał (Krokogator) on 30.10.2016.
 */

public interface CommentService {

    Comment findById(long id);

    List<Comment> findAllComments();

    List<Comment> findByCommentContaining(String content);

    List<Comment> findByPost(Post post);

    List<Comment> findByAuthor(User author);

    void saveComment(Comment comment);

    void updateComment(Comment comment);

    void deleteComment(Comment comment);
}
