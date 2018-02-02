# base image
FROM python:3.5
# install Flask and redis
RUN pip install Flask==0.11.1 redis==2.10.5
# add new user 'admin'.  -ms option creates default home directory
RUN useradd -ms /bin/bash admin
# run app under 'admin' user, otherwise will run as root
USER admin
# sets working directory for any run cmd
WORKDIR /app
# copy app directory to container
COPY app /app
# run flask application
CMD ["python", "app.py"] 
