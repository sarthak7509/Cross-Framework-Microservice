package com.sarthak.UserService.Controllers;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;
 
import com.sarthak.UserService.models.Movies;

/**
 * MovieController
 */
@RestController
public class MovieController {

    @Autowired
    private RestTemplate restTemplate;

    @GetMapping("/movies")
    public ResponseEntity<String> getMovies(){
        String result = restTemplate.getForObject("http://recommendation-service/movies",String.class);
        return ResponseEntity.status(200).body(result);
    }

    @PostMapping("/movies")
    public ResponseEntity<String> getRecommadation(@RequestBody Movies movies){
        String result = restTemplate.postForObject("http://recommendation-service/movies/",movies,String.class);
        return ResponseEntity.status(200).body(result);
    }
}