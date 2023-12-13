# Use a Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python script and templates
COPY . .

# Install dependencies
RUN pip install Flask pandas

# Expose the port your application runs on
EXPOSE 5000

# fixing the permission of the git repository 
RUN git config --global --add safe.directory /usr/src/app/git

# change the working dir to mount
WORKDIR /usr/src/app/git
# Command to run the application
CMD ["python", "/usr/src/app/gitlog_parser.py"]
