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

Now let add index page

### Step 8
create new folder with name myapp
```bash
mkdir myapp
```
Then create index.html file and
```bash
touch index.html
```
Add following code in html file

```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project 3 Docker</title>
</head>
<body>
    <h1>docker project for beginner</h1>
    <h2>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deleniti nostrum unde, iste doloremque pariatur fugiat necessitatibus facilis distinctio consequuntur vitae ratione expedita minus quae? Deserunt voluptatum officia aliquam placeat minus!</h2>
    <button>Submit</button>
</body>
</html>
```

### Step 9
Come back to dockerfile 
Add this line under your RUN command
```bash
COPY myapp /var/www/html
```

Build dockerfile and rerun the container..! (Recall this steps from learning..!)