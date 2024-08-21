### Project 3 
## Dockerizing an Nginx web server

### Step 1
```bash
FROM ubuntu:latest
```
We will pull ubuntu latest image from docker hub

### Step 2
```bash
RUN apt-get update && apt-get upgrade -y
```
Update and then upgrade our ubuntu image.

### Step 3
```bash
RUN apt-get install -y nginx
```
We will install nginx in ubuntu image

### Step 4
```bash
EXPOSE 8080
```
This exposes port 8080 on container allowing it to coming requests

### Step 5
```bash
CMD ["nginx", "-g", "daemon off;"]
```
this will set to execute as a default command when container starts

### Step 6
Now open terminal
```bash
docker build -t project3nginx .
```
Create image using this command

### Step 7
Now create container using created image
```bash
docker run -p 8080:80 --name project3container project3nginx
```

SO you have successuly created container which runs Nginx server..!