FROM ubuntu:latest
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y nginx
COPY myapp /var/www/html
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
# nginx: This is the command being run, which starts the Nginx web server.

# -g: This option is used to pass a directive to Nginx from the command line.

# daemon off;: This directive tells Nginx to run in the foreground, meaning it will not fork off as a background process (which is the default behavior).
