
# Project 1: Setting Up an Ubuntu Container with SSH Access

This project involves setting up an Ubuntu container with SSH access using Docker. Below are the steps completed:

## 1. Pull Ubuntu Image
First, pull the Ubuntu image from Docker Hub using the following command:
```bash
docker pull ubuntu
```
## 2. Run the Container

Next, create and start a new container named container1 using the command:
```bash
docker run -it --name container1 ubuntu
```

## 3. Update the Package List
Inside the container, update the package list by running:
```bash
apt-get update
```

## 4. Install OpenSSH Server
To install the OpenSSH server, use the following command:
```bash
apt-get install openssh-server
```

## 5. Install Nano Text Editor
Install the Nano text editor by running:
```bash
apt-get install nano
```

## 6. Configure SSH for Root Login
Edit the SSH configuration file to allow root login. Run the following command to open the configuration file in Nano:
```bash
nano /etc/ssh/sshd_config
```
In the file, find the line with #PermitRootLogin and change it to:
PermitRootLogin yes

## 7. Check Running Services
To check the status of all running services inside the container, use:
```bash
service --status-all
```

## 8. Start the SSH Service
To start the SSH service, run the following command:
```bash
service ssh start
```

## 9. Exit the Container
Finally, exit the container using the command:
```bash
exit
```





