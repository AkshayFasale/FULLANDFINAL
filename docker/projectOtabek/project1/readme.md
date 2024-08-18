# Project 1: Setting Up an Ubuntu Container with SSH Access

This project involves setting up an Ubuntu container with SSH access using Docker. Below are the complete steps:

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

So now done with setup of 2 containers, we have to login to container 1 now and see the password of root

## 10. run command to start container1

```bash
docker start container1
```

## 11. Run command to enter into container1

```bash
docker exec -it container1 bash
```

## 12. Run command to get the root password

```bash
cat /etc/shadow | grep root
```

but password is in hashed mode, so lets reset password

## 13. Run command to reset password for root
```bash
passwd root
```

## 14. Now exit the container1

check the IP address of container1
```bash
docker inspect container1 | grep IPAddress
```

## 15. Now enter into container 2 using command

```bash
docker start container2
docker exec -it container2 bash
```

## 16. If in case you get error like u cant access ssh for container1 then go back to container1 and start the ssh using command
```bash
start ssh service
```

## 17. come back to container2
enter command
```bash
ssh @IP address of container1
```
You entered into Container1 from container2