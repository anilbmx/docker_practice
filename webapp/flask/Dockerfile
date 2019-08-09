#use python 3.6 container image
FROM python:3.6-stretch

# set the working directory
WORKDIR /app

#copy the current directory contents to container at /app
ADD . /app

#install all dependencies
#RUN pip3 install flask
#RUN pip3 install uwsgi
RUN pip3 install -r reqirements.txt

#run command to start uWSGI
#CMD ["python3", "run.py"]
CMD ["uwsgi","app.ini"]
