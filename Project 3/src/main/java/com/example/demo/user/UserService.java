package com.example.demo.user;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserService {

    @Autowired
    private IUserRepository userRepository;

    public User saveUser(User user) {
        return userRepository.save(user);
    }

    public List<User> getUsers() {
        System.out.println("Getting users from database");
        sleepForAWhile();
        return userRepository.findAll();
    }

    public User getUser(Integer id) {
        System.out.println("Getting user from database");
        sleepForAWhile();
        return userRepository.findById((long)id).get();
    }

    public void sleepForAWhile(){
        try {
            Thread.sleep(4000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
