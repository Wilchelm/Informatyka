package dtas.repository;

import dtas.model.User;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

/**
 * @author Arkadiusz Rosiak (http://www.rosiak.it)
 * @date 2016-10-11
 */
public interface UserRepository extends JpaRepository<User, Long>{

    List<User> findByNameContaining(String name);

    List<User> findTop10ByOrderByRegistrationDateTimeDesc();

    User findByName(String name);

    User findByMail(String mail);

    User findById(Long id);

}
