package com.example.demo_bean;

import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.FileSystemXmlApplicationContext;
import org.springframework.core.io.FileSystemResource;
import org.springframework.core.io.Resource;

public class BeanDemo {
    public static void main(String[] args)
    {
        // First example
        Resource rs = new FileSystemResource("beans-config.xml");
        BeanFactory beanFactory = new XmlBeanFactory(rs);   // XmlBeanFactory is deprecated

        // Bean class HelloBean is set to bean ID "helloBeanId" in config XML
        HelloBean helloBean = (HelloBean) beanFactory.getBean("helloBeanId");
        System.out.println(helloBean.getHelloStr());



        // Another example
        ApplicationContext applicationContext = new FileSystemXmlApplicationContext("beans-config.xml");

        HelloBean helloBean_2 = (HelloBean) applicationContext.getBean("helloBeanId");
        System.out.println(helloBean_2.getHelloStr());
    }
}
