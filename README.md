# docker
Docker with Python

Python code, contained in index.py. The application is a simple, “Hello World” app that uses Flask, a small HTTP server for Python apps.    

To build the image, run Docker build from a command line or terminal that is in the root directory of the application.    
$docker build --tag sks-python-flask-app .    

This will “tag” the image my-python-app and build it. After it is built, you can run the image as a container.        
$docker run --name python-app -p 5000:5000 sks-python-flask-app     

![Imgur Image](https://imgur.com/2PEx4F3.jpg)    
