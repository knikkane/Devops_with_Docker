# Exercise 1.15
Extending a simple [gitlog parser script](https://github.com/knikkane/git_log_to_df) that parses Git log data from your local folder and organizes it into a Pandas DataFrame. Adding Flask to expose a a web interface for the original script, transforming it into a web API.

Flask introduces a route /gitlog to trigger the script, rendering an HTML page (gitlog_table.html) with the parsed Git log data. The web application uses the render_template function to present the data in columns: Author, Date, Email, and Message.

The Git log data is provided to the Docker container by mounting a directory from the host machine. Accessing http://localhost:5000/gitlog triggers the execution of the original Python script, presenting the parsed Git log data on the HTML page.

## Usage
```shell
~$ docker pull knikkane/gitlog-parser
~$ docker run -p 5000:5000 -v "/home/user/mygitrepo:/app" knikkane/gitlog-parser
```

## Link to the project in Docker Hub
[gitlog-parser](https://hub.docker.com/repository/docker/knikkane/gitlog-parser)
