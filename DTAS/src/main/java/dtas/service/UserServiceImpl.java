package dtas.service;

import dtas.HashingTool;
import dtas.model.User;
import dtas.repository.UserRepository;
import org.springframework.stereotype.Component;
import org.springframework.util.Assert;

import javax.persistence.EntityExistsException;
import javax.persistence.EntityNotFoundException;
import javax.transaction.Transactional;
import java.time.LocalDateTime;
import java.util.Collections;
import java.util.List;

/**
 * @author Arkadiusz Rosiak (http://www.rosiak.it)
 * @date 2016-10-11
 */

@Component("userService")
@Transactional
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;

    public UserServiceImpl(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public User findById(Long id) {
        User user = userRepository.findById(id);

        if(user == null){
            throw new EntityNotFoundException("Uzytkownik o id " + id + " nie istnieje");
        }

        return user;
    }

    @Override
    public List<User> findAllUsers() {
        return userRepository.findAll();
    }

    @Override
    public List<User> findTop10UsersOrderedBy(String orderBy)
    {

        if(orderBy.toLowerCase().equals("registrationdate")){
            return userRepository.findTop10ByOrderByRegistrationDateTimeDesc();
        }

        return Collections.emptyList();
    }

    @Override
    public List<User> findByNameContaining(String name) {
        Assert.notNull(name, "Musisz podac nazwe uzytkownika!");
        return userRepository.findByNameContaining(name);
    }

    @Override
    public User findByName(String name) {

        if(name == null || name.length() == 0){
            throw new IllegalArgumentException("Nazwa uzytkownika nie moze byc pusta");
        }

        User user = userRepository.findByName(name);

        if(user == null){
            throw new EntityNotFoundException("Nie znaleziono uzytkownika o podanej nazwie");
        }

        return user;
    }


    @Override
    public User findByMail(String mail) {

        if(mail == null || mail.length() == 0){
            throw new IllegalArgumentException("Mail nie moze byc pusty");
        }

        User user = userRepository.findByMail(mail);

        if(user == null){
            throw new EntityNotFoundException("Nie znaleziono uzytkownika o podanym mailu");
        }

        return user;
    }

    @Override
    public boolean isUserExist(User user) {
        User userWithName = userRepository.findByName(user.getName());
        User userWithMail = userRepository.findByMail(user.getMail());
        return userWithName != null || userWithMail != null;
    }

    @Override
    public void saveUser(User user) {
        if(user == null){
            throw new IllegalArgumentException("User must not be null!");
        }

        if(isUserExist(user)){
            throw new EntityExistsException("Uzytkownik o podanej nazwie lub adresie email juz istnieje!");
        }

        userRepository.save(user);
    }

    @Override
    public void updateUser(User user) {
        if(user == null){
            throw new IllegalArgumentException("User must not be null!");
        }

        User userInDb = findById(user.getId());

        User userWithName = userRepository.findByName(user.getName());
        if(userWithName != null && !userWithName.equals(userInDb)){
            throw new EntityExistsException("Uzytkownik o podanej nazwie juz istnieje!");
        }

        User userWithMail = userRepository.findByMail(user.getMail());
        if(userWithMail != null && !userWithMail.equals(userInDb)){
            throw new EntityExistsException("Uzytkownik o podanym mailu istnieje!");
        }

        userInDb.setName(user.getName());
        userInDb.setMail(user.getMail());
        userInDb.setRawPassword(user.getPassword());

        userRepository.save(userInDb);
    }

    @Override
    public void updateLastSeen(User user)
    {
        if(user == null){
            throw new IllegalArgumentException("User must not be null!");
        }

        user.setLastSeen(LocalDateTime.now());
        userRepository.save(user);
    }

    @Override
    public void deleteUser(User user) {
        userRepository.delete(user);
    }

    @Override
    public User getLoggedInUser()
    {
        User user = new User("Admin", "admin@admin.pl", "admin");

        if(!isUserExist(user)){
            saveUser(user);
        }
        else{
            user = findByName(user.getName());
        }
        return user;
        /*ServletRequestAttributes attr = (ServletRequestAttributes) RequestContextHolder.currentRequestAttributes();
        HttpSession session = attr.getRequest().getSession();

        return (User) session.getAttribute("user");*/
    }

    @Override
    public boolean checkLoginCredentials(String username, String password)
    {
        User user = findByName(username);

        if(user.getPassword().equalsIgnoreCase(HashingTool.sha512(password)))
        {
           return true;
        }
        else{
            throw new IllegalArgumentException("Authorization failed");
        }
    }
}
