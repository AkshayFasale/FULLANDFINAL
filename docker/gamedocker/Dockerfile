# In this project i have deoployed 2048 game on AWS EBS using docker container.
# first written this dockerfile
# then hosted it on AWS EBS
 
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y nginx zip curl
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Download the ZIP file correctly
RUN curl -o /var/www/html/master.zip -L https://github.com/gabrielecirulli/2048/archive/refs/heads/master.zip

RUN cd /var/www/html/ && unzip master.zip && mv 2048-master/* . && rm -rf 2048-master master.zip

EXPOSE 80
CMD ["/usr/sbin/nginx", "-c", "/etc/nginx/nginx.conf"]
