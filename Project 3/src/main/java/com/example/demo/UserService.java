package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserService {

    @Autowired
    private IUserRepository userRepository;

    @Autowired
    private RedisTemplate redisTemplate;

    private static final String KEY = "USER";

    public User saveUser(User user) {
        return userRepository.save(user);
    }

    public List<User> getUsers() {
        System.out.println("Getting users from database");
        return userRepository.findAll();
    }

    public User getUser(Integer id) {
        System.out.println("Getting user from database");
        return userRepository.findById((long)id).get();
    }
}
