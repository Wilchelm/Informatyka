package dtas.controller;

import com.fasterxml.jackson.annotation.JsonView;
import dtas.ViewsContainer;
import dtas.model.User;
import dtas.service.UserService;
import org.apache.catalina.servlet4preview.http.HttpServletRequest;
import org.apache.commons.validator.routines.EmailValidator;
import org.springframework.http.ResponseEntity;
import org.springframework.util.Assert;
import org.springframework.web.bind.annotation.*;

import javax.inject.Inject;
import javax.persistence.EntityNotFoundException;
import java.time.LocalDateTime;
import java.util.List;

/**
 * @author Arkadiusz Rosiak (http://www.rosiak.it)
 * @date 2016-10-10
 */

@RestController
@CrossOrigin(origins = "*")
public class UserController {

    private final UserService userService;

    @Inject
    public UserController(UserService userService) {
        Assert.notNull(userService, "UserService must not be null!");
        this.userService = userService;
    }

    /**
     * Pobieranie wszystkich uzytkownikow
     *
     * @param name opcjonalna nazwa uzytkownika, ktorego nalezy wyszukac
     * @return users list
     */
    @RequestMapping(value = "/v1/user", method = RequestMethod.GET)
    @JsonView(ViewsContainer.UserSummary.class)
    public ResponseEntity getUsersByName(@RequestParam(value = "name", required = false) String name,
                                         @RequestParam(value = "orderBy", required = false) String orderBy) {

        if(orderBy != null){
            return ResponseEntity.ok(userService.findTop10UsersOrderedBy(orderBy));
        }

        if (name != null) {

            List<User> users = userService.findByNameContaining(name);

            if (!users.isEmpty()) {
                return ResponseEntity.ok(users);
            }

            throw new IllegalArgumentException("Nie znaleziono uzytkownikow o podanych kryteriach");
        }

        return ResponseEntity.ok(userService.findAllUsers());
    }


    /**
     * Pobieranie informacji o pojedynczym uzytkowniku
     *
     * @param id id uzytkownika
     * @return user
     */
    @RequestMapping(value = "/v1/user/{id}", method = RequestMethod.GET)
    @JsonView(ViewsContainer.UserDetails.class)
    public ResponseEntity getUserById(@PathVariable long id) throws EntityNotFoundException{
        User user = userService.findById(id);
        return ResponseEntity.ok(user);
    }


    /**
     * Dodawanie nowego uzytkownika
     * @param user <- parametry uzytkownika zakodowane w json np: {"name": "Admin"}
     */
    @RequestMapping(value = "/v1/user", method = RequestMethod.POST)
    @JsonView(ViewsContainer.UserDetails.class)
    public ResponseEntity createUser(@RequestBody User user) {

        checkUserCorrectness(user);
        checkMailCorrectness(user.getMail());

        user.setRegistrationDateTime(LocalDateTime.now());

        userService.saveUser(user);

        return ResponseEntity.ok(null);
    }

    private boolean checkUserCorrectness(User user){
        Assert.notNull(user, "User nie moze byc pusty");
        Assert.notNull(user.getName(), "Musisz podac nazwe uzytkownika");
        Assert.notNull(user.getMail(), "Musisz podac mail uzytkownika");
        Assert.notNull(user.getPassword(), "Musisz podac haslo uzytkownika");

        return true;
    }

    private boolean checkMailCorrectness(String mail){
        boolean correct = EmailValidator.getInstance().isValid(mail);

        if(!correct){
            throw new IllegalArgumentException("Adres email jest nieprawdiłowy");
        }

        return true;
    }

    /**
     * Usuwanie uzytkownika o podanym id
     */
    @RequestMapping(value = "/v1/user/{id}", method = RequestMethod.DELETE)
    public ResponseEntity deleteUser(@PathVariable long id) {

        User user = userService.findById(id);

        if (user != null) {
            userService.deleteUser(user);
            return ResponseEntity.ok(null);
        }

        throw new EntityNotFoundException("Uzytkownik o podanym id nie istnieje");
    }

    /**
     * Aktualizacja uzytkownika
     */
    @RequestMapping(value = "/v1/user/{id}", method = RequestMethod.PUT)
    @JsonView(ViewsContainer.UserDetails.class)
    public ResponseEntity updateUser(HttpServletRequest request, @PathVariable long id, @RequestBody User user) {

        User userInDb = userService.findById(id);
        user.setId(userInDb.getId());

        checkUserCorrectness(user);
        checkMailCorrectness(user.getMail());

        userService.updateUser(user);

        User activeUser = (User) request.getSession().getAttribute("user");
        if(activeUser.getId() == user.getId())
        {
            request.getSession().setAttribute("user", userInDb);
        }

        return ResponseEntity.ok(userInDb);
    }


    @RequestMapping(value = "/v1/login", method = RequestMethod.GET)
    @JsonView(ViewsContainer.UserDetails.class)
    public ResponseEntity loginUser(HttpServletRequest request, @RequestParam("name") String name, @RequestParam("password") String password) {

        if(userService.checkLoginCredentials(name, password))
        {
            User user = userService.findByName(name);
            userService.updateLastSeen(user);

            request.getSession().setAttribute("user", user);
        }

        return ResponseEntity.ok(null);
    }

    @RequestMapping(value = "/v1/logout", method = RequestMethod.GET)
    @JsonView(ViewsContainer.UserDetails.class)
    public ResponseEntity logoutUser(HttpServletRequest request) {
        request.getSession().removeAttribute("user");
        return ResponseEntity.ok(null);
    }

    @RequestMapping(value = "/v1/user/active", method = RequestMethod.GET)
    @JsonView(ViewsContainer.UserDetails.class)
    public ResponseEntity getActiveUser(HttpServletRequest request){

        User user = (User) request.getSession().getAttribute("user");

        if(user == null){
            throw new EntityNotFoundException("User is NOT logged in");
        }

        return ResponseEntity.ok(user);
    }
}
