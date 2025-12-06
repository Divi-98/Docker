# set a base docker image
FROM python:3.12-slim

#set the curent working directory in the image
WORKDIR /app

#copy the files from the host file system to the image file system
COPY app.py .

#Install the necessary packages
RUN pip install pytz

#Set the environment variables
ENV TZ "Asia/Kolkata"  

#Run a command to start the application
CMD ["python", "app.py"]
