# set a base docker image
FROM python:3.12-slim

#set the curent working directory in the image
WORKDIR /app

#copy the files from the host file system to the image file system
COPY app.py .

#Install the necessary packages
RUN pip install pytz

#Install flask
RUN pip install pytz flask

#Set the environment variables
ENV TZ "Asia/Kolkata"  

#Expose the port 3000
EXPOSE 3000

#Run a command to start the application
CMD ["python", "app.py"]
