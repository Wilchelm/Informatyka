package dtas.controller;

import dtas.Application;
import dtas.model.Comment;
import dtas.model.Post;
import dtas.model.User;
import dtas.service.CommentService;
import dtas.service.PostService;
import dtas.service.UserService;
import org.apache.catalina.servlet4preview.http.HttpServletRequest;
import org.springframework.http.ResponseEntity;
import org.springframework.util.Assert;
import org.springframework.web.bind.annotation.*;

import javax.inject.Inject;
import javax.persistence.Entity;
import javax.persistence.EntityExistsException;
import javax.persistence.EntityNotFoundException;
import java.time.LocalDateTime;
import java.util.List;

/**
 * Created by Michał (Krokogator) on 31.10.2016.
 */
@RestController
@CrossOrigin(origins = "*")
public class CommentController {

    private final CommentService commentService;
    private final PostService postService;
    private final UserService userService;

    @Inject
    public CommentController(CommentService commentService, PostService postService, UserService userService) {

        this.commentService = commentService;
        this.postService = postService;
        this.userService = userService;

    }
    /**
     * POST
     * Dodanie komentarza
     */
    @RequestMapping(value = "/v1/comment", method = RequestMethod.POST)
    public ResponseEntity createComment(HttpServletRequest request ,@RequestBody Comment comment){
        User author = (User) request.getSession().getAttribute("user");
        comment.setAuthor(author);
        comment.setCreateDateTime(LocalDateTime.now());
        //Post post = postService.findById(1L);
        //comment.setPost(post);

        validateComment(comment);
        commentService.saveComment(comment);

        return ResponseEntity.ok(null);

    }

    private boolean validateComment(Comment comment){
        Assert.notNull(comment.getAuthor(),"Komentarz nie posiada autora");
        Assert.notNull(comment.getPost(),"Komentarz nie jest przypisany do posta");
        Assert.notNull(comment.getContent(),"Tresc komentarza jest pusta");
        return true;
    }
    /**
     * Aktualizacja komentarza
     * @param id
     * @param newcomment
     * @return
     */
    @RequestMapping (value = "/v1/comment/{id}", method = RequestMethod.PUT)
    public ResponseEntity updateComment(HttpServletRequest request, @PathVariable long id,@RequestBody Comment newcomment){
        Comment comment = commentService.findById(id);
        newcomment.setId(comment.getId());
        newcomment.setAuthor(comment.getAuthor());
        newcomment.setPost(comment.getPost());
        validateComment(comment);

        commentService.updateComment(newcomment);

        return ResponseEntity.ok(null);
    }

    /**
     * GET
     * Pobieranie wszystkich komentarzy
    */
    @RequestMapping(value = "/v1/comment", method = RequestMethod.GET)
    public ResponseEntity getComments(){ return ResponseEntity.ok(commentService.findAllComments()); }

    /**
     * Wyświetlanie po autorze (ID)
     */
    @RequestMapping(value = "/v1/user/{author}/comments", method = RequestMethod.GET)
    public ResponseEntity getCommentsByAuthorName(@PathVariable String author){
        int switcher;
        long authorID=0;
        try{
            authorID = Long.parseLong(author);
            switcher = 1;
        }
        catch(NumberFormatException ParseFail){
            switcher = 2;
        }

        if(switcher == 1){
            List<Comment> comments = commentService.findByAuthor(userService.findById(authorID));
            if(comments != null){
                return ResponseEntity.ok(comments);
            }
            throw new EntityNotFoundException("Nie znaleziono komentarzy autora o takim id");
        }
        if(switcher == 2){
            List<Comment> comments = commentService.findByAuthor(userService.findByName(author));
            if (comments != null) {
                return ResponseEntity.ok(comments);
            }
            throw new EntityNotFoundException("Nie znaleziono komentarzy autora o takiej nazwie");
        }
        throw new EntityNotFoundException("Użytkownik nie istnieje");
    }

    /**
     * Wyświetlanie po poście
     */
    @RequestMapping(value = "/v1/post/{post}/comments", method = RequestMethod.GET)
    public ResponseEntity getCommentsByPost(@PathVariable String post) {
        long postID=0;
        try{
            postID = Long.parseLong(post);
        }
        catch(NumberFormatException ParseFail){}
        List<Comment> comments = commentService.findByPost(postService.findById(postID));
        if (comments != null) {
            return ResponseEntity.ok(comments);
        }
        throw new EntityNotFoundException("Nie znaleziono komentarzy dla postu o takim id");
    }

    /**
     * Pobieranie pojedynczego komentarza
     * @param id  - id komentarza
     * @return post
     */
    @RequestMapping (value = "v1/comment/{id}", method = RequestMethod.GET)
    public ResponseEntity getCommentById(@PathVariable long id){

        Comment comment = commentService.findById(id);

        if(comment != null){
            return ResponseEntity.ok(comment);
        }
        throw new EntityNotFoundException("Post o podanym id nie istnieje.");
    }
    /**
     * DELETE
     * Usuwanie
     */
    @RequestMapping(value = "/v1/comment/{id}", method = RequestMethod.DELETE)
    public ResponseEntity deleteComment(@PathVariable long id){
        Comment comment = commentService.findById(id);
        if(comment != null){
            commentService.deleteComment(comment);
            return ResponseEntity.ok(null);
        }
        throw new EntityNotFoundException("Komentarz o podanym id nie istnieje");
    }
}
