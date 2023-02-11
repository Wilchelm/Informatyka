package dtas.controller;

import dtas.model.Post;
import dtas.model.User;
import dtas.service.PostService;
import dtas.service.UserService;
import org.apache.catalina.servlet4preview.http.HttpServletRequest;
import org.springframework.http.ResponseEntity;
import org.springframework.util.Assert;
import org.springframework.web.bind.annotation.*;

import javax.inject.Inject;
import javax.persistence.EntityExistsException;
import javax.persistence.EntityNotFoundException;
import java.time.LocalDateTime;
import java.util.List;

/**
 * Created by Dawid on 2016-10-18.
 */
@RestController
@CrossOrigin(origins = "*")
public class PostController {

    private final PostService postService;
    private final UserService userService;

    @Inject
    public PostController(PostService postService, UserService userService) {
        this.postService = postService;
        this.userService = userService;
    }

    /**
     * Pobieranie wszystkich postów
     *
     * @param title opcjonalny tytuł postu, ktorego nalezy wyszukac
     * @return post list
     */
    @RequestMapping (value = "v1/post", method = RequestMethod.GET)
    public ResponseEntity getPostsByTitle(@RequestParam(value = "title", required = false) String title,
                                          @RequestParam(value = "orderBy", required = false) String orderBy){

        if(orderBy != null){
            return ResponseEntity.ok(postService.findTop5PostsOrderedBy(orderBy));
        }

        if(title!= null){
            List<Post> posts = postService.findByTitle(title);
            if(!posts.isEmpty()){
                return ResponseEntity.ok(posts);
            }
            throw new IllegalArgumentException("Nie znaleziono postu z takim tytułem.");
        }
        return ResponseEntity.ok(postService.findAllPosts());
    }

    /**
     * Pobieranie wszystkich postow danego autora za pomoca id or name
     * @param author - id or name usera
     * @return post list
     */
    @RequestMapping (value = "/v1/user/{author}/posts", method = RequestMethod.GET)
    public ResponseEntity getPostByAuthorName(@PathVariable String author){
        int test;
        long aut=0;
        try {
            aut = Long.parseLong(author);
            test = 1;
        } catch (NumberFormatException nfe) {
            test =2;
        }

        if(test == 1){
            List<Post> posts = postService.findByAuthor(userService.findById(aut));
            if(posts != null){
                return ResponseEntity.ok(posts);
            }
            throw new EntityNotFoundException("Nie znaleziono postow autora z takim id");
        }
        if(test == 2) {
            List<Post> posts = postService.findByAuthor(userService.findByName(author));
            if (posts != null) {
                return ResponseEntity.ok(posts);
            }
            throw new EntityNotFoundException("Nie znaleziono postow autora z taka nazwa");
        }
        throw new EntityNotFoundException("Taki uzytkownik nie istnieje");
    }

    /**
     * Pobieranie pojedynczego posta
     * @param id  - id posta
     * @return post
     */
    @RequestMapping (value = "v1/post/{id}", method = RequestMethod.GET)
    public ResponseEntity getPostById(@PathVariable long id){

        Post post = postService.findById(id);

        if(post != null){
            return ResponseEntity.ok(post);
        }
        throw new EntityNotFoundException("Post o podanym id nie istnieje.");
    }


    /**
     * Dodanie postu
     * @param post - parametry postu bla bla bla
     */
    @RequestMapping (value = "/v1/post", method = RequestMethod.POST)
    public ResponseEntity createPost(HttpServletRequest request , @RequestBody Post post) {

        User author = (User) request.getSession().getAttribute("user");
        post.setAuthor(author);
        post.setCreateDateTime(LocalDateTime.now());

        if (checkPostCorrectness(post)) {
            postService.savePost(post);
            return ResponseEntity.ok(null);
        }
        throw new EntityExistsException("Post jest niepoprawny");
    }

    private boolean checkPostCorrectness(Post post){
        Assert.notNull(post, "Post nie moze byc pusty");
        Assert.notNull(post.getAuthor(), "Brak autora");  /**Autor bedzie dodany automatycznie ale moze sobie byc ten assert ^^*/
        Assert.notNull(post.getTitle(), "Musisz podac tutul postu");
        Assert.notNull(post.getContent(), "Musisz podac zawartosc postu");
        return true;
    }

    /**
     * Aktualizacja postu
     * @param id
     * @param post
     * @return
     */
    @RequestMapping (value = "/v1/post/{id}", method = RequestMethod.PUT)
    public ResponseEntity updatePost(HttpServletRequest request, @PathVariable long id,@RequestBody Post post){
        Post postInDb = postService.findById(id);
        post.setId(postInDb.getId());
        post.setAuthor(postInDb.getAuthor());

        User activeUser = (User) request.getSession().getAttribute("user");
        if(activeUser.getId() == post.getAuthor().getId())
        {
            if (checkPostCorrectness(post)) {
                postService.updatePost(post);
                return ResponseEntity.ok(postInDb);
            }
            throw new EntityNotFoundException("Post jest niepoprawny");
        }
        throw new EntityNotFoundException("Nie jestes autorem tego postu");
    }

    /**
     * Kasacja postu
     * @param id - id postu
     */
    @RequestMapping (value = "/v1/post/{id}", method = RequestMethod.DELETE)
    public ResponseEntity deletePost(HttpServletRequest request, @PathVariable long id){

        Post post = postService.findById(id);
        User activeUser = (User) request.getSession().getAttribute("user");
        if(activeUser.getId() == post.getAuthor().getId()){
            postService.deletePost(post);
            return ResponseEntity.ok(null);
        }
        throw new EntityNotFoundException("Post o podanym id nie istnieje lub nie jestes jego autorem");
    }


}
