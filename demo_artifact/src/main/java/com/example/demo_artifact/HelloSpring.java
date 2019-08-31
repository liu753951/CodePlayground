package com.example.demo_artifact;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloSpring {

    @RequestMapping("/test1")
    public String index_1()
    {
        return "Hello Spring 1";
    }

    @RequestMapping("/test2")
    public String index_2()
    {
        return "Hello Spring 2";
    }

}
