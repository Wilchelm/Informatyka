//package dtas.service;
//
//import dtas.model.User;
//import org.junit.After;
//import org.junit.Assert;
//import org.junit.Test;
//import org.junit.runner.RunWith;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.boot.test.context.SpringBootTest;
//import org.springframework.test.context.junit4.SpringRunner;
//
//import javax.persistence.EntityExistsException;
//import javax.persistence.EntityNotFoundException;
//
//@RunWith(SpringRunner.class)
//@SpringBootTest()
//public class UserServiceTest {
//
//    @Autowired
//    private UserService userService;
//
//    private User testUser = new User("test_user","test@user.pl","password");
//
//
//    @After
//    public void tearDown() throws Exception {
//        deleteTestUserIfExists();
//
//    }
//
//    private void addTestUserIfNotExists(){
//        if(!userService.isUserExist(testUser)){
//            userService.saveUser(testUser);
//        }
//    }
//
//    private void deleteTestUserIfExists(){
//        if(userService.isUserExist(testUser)) {
//            userService.deleteUser(testUser);
//        }
//    }
//
//    @Test
//    public void falseWhenUserNotExist() throws Exception {
//        deleteTestUserIfExists();
//        Assert.assertFalse("isUserExist() powinno zwracac false, gdy uzytkownik nie istnieje",
//                userService.isUserExist(testUser));
//    }
//
//    @Test
//    public void createNotExistingUser() throws Exception {
//        userService.saveUser(testUser);
//    }
//
//    @Test
//    public void trueWhenUserExists() throws Exception {
//        addTestUserIfNotExists();
//        Assert.assertTrue("isUserExist() powinno zwracac true, gdy uzytkownik istnieje",
//                userService.isUserExist(testUser));
//        deleteTestUserIfExists();
//    }
//
//    @Test
//    public void trueWhenUserWithSameNameExists() throws Exception {
//        addTestUserIfNotExists();
//        User u = new User("test_user", "other@mail.pl", "password");
//        Assert.assertTrue(userService.isUserExist(u));
//    }
//
//    @Test
//    public void trueWhenUserWithSameMailExists() throws Exception {
//        addTestUserIfNotExists();
//        User u = new User("other_user", "test@user.pl", "password");
//        Assert.assertTrue(userService.isUserExist(u));
//    }
//
//    @Test(expected=EntityExistsException.class)
//    public void createExistingUserShouldFail() throws Exception {
//        addTestUserIfNotExists();
//        userService.saveUser(testUser);
//    }
//
//    @Test(expected=IllegalArgumentException.class)
//    public void createNullUserShouldFail() throws Exception {
//        userService.saveUser(null);
//    }
//
//    @Test
//    public void shouldFindUserByIdWhenExists() throws Exception {
//        addTestUserIfNotExists();
//        Assert.assertNotNull(userService.findById(testUser.getId()));
//    }
//
//    @Test(expected = EntityNotFoundException.class)
//    public void shouldNotFindUserByIdWhenNotExists() throws Exception {
//        userService.findById(-1l);
//    }
//
//    @Test
//    public void shouldReturnCollectionOfAllUsers() throws Exception {
//        deleteTestUserIfExists();
//        Object users = userService.findAllUsers();
//        Assert.assertNotNull(users);
//    }
//
//    @Test
//    public void shouldFindExistingUserWithName() throws Exception {
//        addTestUserIfNotExists();
//        User user = userService.findByName(testUser.getName());
//        Assert.assertEquals(testUser, user);
//    }
//
//    @Test(expected = EntityNotFoundException.class)
//    public void shouldNotFindNotExistingUserWithName() throws Exception {
//        deleteTestUserIfExists();
//        userService.findByName(testUser.getName());
//    }
//
//    @Test(expected = IllegalArgumentException.class)
//    public void shouldFindFailWhenUserNameIsEmpty() throws Exception {
//        userService.findByName("");
//    }
//
//    @Test
//    public void shouldFindExistingUserWithMail() throws Exception {
//        addTestUserIfNotExists();
//        User user = userService.findByMail(testUser.getMail());
//        Assert.assertEquals(testUser, user);
//    }
//
//    @Test(expected = EntityNotFoundException.class)
//    public void shouldNotFindNotExistingUserWithMail() throws Exception {
//        deleteTestUserIfExists();
//        userService.findByMail(testUser.getMail());
//    }
//
//    @Test(expected = IllegalArgumentException.class)
//    public void shouldFindFailWhenUserMailIsEmpty() throws Exception {
//        userService.findByMail("");
//    }
//
//    @Test
//    public void shouldDeleteUser() throws Exception {
//        addTestUserIfNotExists();
//        userService.deleteUser(testUser);
//        Assert.assertFalse(userService.isUserExist(testUser));
//    }
//
//    @Test
//    public void shouldUpdateUserMail() throws Exception {
//        deleteTestUserIfExists();
//        addTestUserIfNotExists();
//        User oldUser = testUser;
//        testUser.setMail("changed@mail.pl");
//        userService.updateUser(testUser);
//        User updatedUser = userService.findById(testUser.getId());
//        Assert.assertEquals(testUser.getMail(), updatedUser.getMail());
//        testUser = oldUser;
//    }
//
//    @Test
//    public void shouldUpdateUserName() throws Exception {
//        deleteTestUserIfExists();
//        addTestUserIfNotExists();
//        User oldUser = testUser;
//        testUser.setName("test_user_changed");
//        userService.updateUser(testUser);
//        User updatedUser = userService.findById(testUser.getId());
//        Assert.assertEquals(testUser.getName(), updatedUser.getName());
//        testUser = oldUser;
//    }
//
//    @Test(expected = EntityExistsException.class)
//    public void shouldNotUpdateUserNameWhenAlreadyExists() throws Exception {
//        addTestUserIfNotExists();
//        User secondUser = addSecondUser();
//
//        secondUser.setName(testUser.getName());
//
//        try{
//            userService.updateUser(secondUser);
//        }
//        catch(EntityNotFoundException e){
//            throw e;
//        }
//        finally {
//            userService.deleteUser(secondUser);
//        }
//    }
//
//    @Test(expected = EntityExistsException.class)
//    public void shouldNotUpdateUserMailWhenAlreadyExists() throws Exception {
//        addTestUserIfNotExists();
//        User secondUser = addSecondUser();
//
//        secondUser.setMail(testUser.getMail());
//
//        try{
//            userService.updateUser(secondUser);
//        }
//        catch(EntityNotFoundException e){
//            throw e;
//        }
//        finally {
//            userService.deleteUser(secondUser);
//        }
//    }
//
//    private User addSecondUser(){
//        User secondUser = new User("second_user", "second@mail.com", "password");
//        userService.saveUser(secondUser);
//        return secondUser;
//    }
//
//
//}