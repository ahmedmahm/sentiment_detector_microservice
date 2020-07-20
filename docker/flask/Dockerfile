# Dockerfile

# inherit the Python 3 image. 
FROM python:3
# Set an environment variable 
ENV APP /app
# Instruct Docker to operate from there
RUN mkdir $APP
WORKDIR $APP
# Expose the port uWSGI will listen on
EXPOSE 5000
# Copy the requirements file in order to install
# Python dependencies
COPY requirements.txt .
# Install Python dependencies
RUN pip install --upgrade pip -r requirements.txt
# copy the rest of the codebase into the container
COPY . .
# run uWSGI with the ini file
CMD [ "uwsgi", "--ini", "app.ini" ]