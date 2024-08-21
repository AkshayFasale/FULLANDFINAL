# Docker Project 2
## Dockerising Apache server and making it live

### 1 Step
In this step we will pull ubuntu latest image from docker hub
```bash
FROM ubuntu:latest
```

### 2 Step
In this step we will update and then install apache2 in our ubuntu image
```bash
RUN apt-get update && apt-get install -y apache2
```

### 3 Step
In this step we will expose our apache server on port 80
```bash
EXPOSE 80
```

### 4 Step
In this step, we will set the default command that runs when the container starts. This command will launch the Apache HTTP server and keep it running in the foreground, ensuring that the container remains active.
CMD ["apache2ctl","-D","FOREGROUND"]

### 5 Step
Now open terminal
In this step, we will build the Docker image. The image will be based on the Dockerfile we created and will include Ubuntu with Apache2 installed and configured to run.

```bash
docker build -t my-apache-image .
```

### 6 Step
In this step, we will run a container from the newly built image. The container will start the Apache server, and you can access it via port 80 on your local machine.

```bash
docker run -d -p 80:80 my-apache-image
```
### 7 Step
In this step, you can verify that the Apache server is running by opening a web browser and navigating to http://localhost. If everything is set up correctly, you should see the default Apache welcome page.







