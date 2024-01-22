# TD3 - Containerize a simple application

Subject

Take/make a simple application, such as a Python script, and create a Dockerfile that packages it into a container. (It should need dependencies/Extenal Libraries)

Build an image of it, push it into the Public Registry (Docker Hub).

Run the container and verify that the application works as expected.

Ask someone to try your image on their own PC.

Document all steps and explain in detail all components you used.

Bonus:

```
- Have the smallest possible image size
- Run a linter on the Dockerfile
- Explain the difference between ADD and COPY in a Dockerfile
- Make the container run without sudo rights
- Run a secure scan on the container and take it into account
- Add your code on a public GitHub repository
```

Let’s create a simple python script that draw a rotating donut in the terminal using numpy.

![Untitled](assets/TD3%20-%20Containerize%20a%20simple%20application%200e26382e801b457fa6300842157dd773/Untitled.png)

Then, we create a requirements.txt file to indicate dependencies.

![Untitled](assets/TD3%20-%20Containerize%20a%20simple%20application%200e26382e801b457fa6300842157dd773/Untitled%201.png)

As I’ve created a python virtual environment for this script, i created a .dockerignore file to indicates that the `env` directory should be ignored.

![Untitled](assets/TD3%20-%20Containerize%20a%20simple%20application%200e26382e801b457fa6300842157dd773/Untitled%202.png)

Then, let’s create the Dockerfile.

![Untitled](assets/TD3%20-%20Containerize%20a%20simple%20application%200e26382e801b457fa6300842157dd773/Untitled%203.png)

I used python:3.10.12-alpine because it is the smallest version (to have the smallest container size possible)

We can now build the image with the following command:

```bash
sudo docker build -t louiscockenpot/moving-donut:1.0 .
```

![Here is an screen of `docker image ls` , you can see that the size of my image is 147MB](assets/TD3%20-%20Containerize%20a%20simple%20application%200e26382e801b457fa6300842157dd773/Untitled%204.png)

Here is a screen of `docker image ls` , you can see that the size of my image is 147MB

We can now publish the image to docker hub.

```bash
sudo docker push louiscockenpot/moving-donut:1.0
```

![Untitled](assets/TD3%20-%20Containerize%20a%20simple%20application%200e26382e801b457fa6300842157dd773/Untitled%205.png)

Someone can now pull it, then run a container from it.

```bash
sudo docker run -it --name donut louiscockenpot/moving-donut:1.0
```

![Untitled](assets/TD3%20-%20Containerize%20a%20simple%20application%200e26382e801b457fa6300842157dd773/Untitled%206.png)

![Untitled](assets/TD3%20-%20Containerize%20a%20simple%20application%200e26382e801b457fa6300842157dd773/Untitled%207.png)

The donut is moving !

Let’s run haodling (online version) on my Dockerfile:

![Untitled](assets/TD3%20-%20Containerize%20a%20simple%20application%200e26382e801b457fa6300842157dd773/Untitled%208.png)

We can see that there is no issue.

Difference between ADD and COPY in the Dockerfile:

- the ADD directive can accept a **remote URL** for its source argument.
- The COPY directive, on the other hand, can only accept **local files.**

Now, to make the container run without the sudo permission, we need to add the user (me) to the docker group:

```bash
sudo gpasswd -a louis docker
```

```bash
sudo service docker restart
```

Then, i had to logout and logback to apply the changes.

Now, i can use `docker start -i moving-donut` to start again the container (without sudo this time)

Let’s run a vulnerability analysis (with Scout Analysis on Dockerhub).

![Untitled](assets/TD3%20-%20Containerize%20a%20simple%20application%200e26382e801b457fa6300842157dd773/Untitled%209.png)

Here we have 2 HIGH, 2 MEDIUM and 0 LOW vulnerabilities.
