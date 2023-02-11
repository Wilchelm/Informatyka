package dtas.service;

import dtas.model.User;

import java.util.List;

/**
 * @author Arkadiusz Rosiak (http://www.rosiak.it)
 * @date 2016-10-11
 */
public interface UserService {

    User findById(Long id);

    List<User> findAllUsers();

    List<User> findTop10UsersOrderedBy(String orderBy);

    List<User> findByNameContaining(String name);

    User findByName(String name);

    User findByMail(String mail);

    boolean isUserExist(User user);

    void saveUser(User user);

    void updateUser(User user);

    void deleteUser(User user);

    void updateLastSeen(User user);

    boolean checkLoginCredentials(String username, String password);

    @Deprecated
    User getLoggedInUser();

}
