# Dockerizing a simple Python Flask web application

### Step 1

Create a folder project4
Create file with this name using touch command

```bash
touch app.py Dockerfile readme.md requirements.txt
```

### Step 2
In requirements.txt file add
flask

Go to this [link](https://flask.palletsprojects.com/en/3.0.x/quickstart/) and copy the first code
paste it in app.py file

under return paste below code

```bash
if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

Explanation:
if __name__ == '__main__':: This line checks if the script is being run directly (as the main program). In Python, the __name__ variable is automatically set to '__main__' when the script is executed directly. If the script is imported as a module in another script, __name__ will not be '__main__', so the block of code inside this if statement will not run.

app.run(host='0.0.0.0'): This line starts the web server.

app: This is typically a Flask or other web framework application instance.
run(): This method starts the web server.
host='0.0.0.0': This tells the server to listen on all available network interfaces, making the web application accessible from any IP address on the network.

### Step 3

Open Dockerfile, Define python version

```bash
FROM python:3.9-slim-buster
```

### Step 4

Need to specify your working directory to app.

```bash
WORKDIR /app
```

### Step 5

Copy requirements from from requirements.txt

```bash
COPY requirements.txt .
```

### Step 6

Run requirements.txt and no-cache-dir so it will install dependencies.

```bash
RUN pip install --no-cache-dir -r requirements.txt
```

### Step 7

Copy entire flask app to working directory

```bash
COPY .   .
```

### Step 8

Expose on port 5000

```bash
EXPOSE 5000
```

### Step 9

TO run app.py use below command
CMD ["python","app.py"]
