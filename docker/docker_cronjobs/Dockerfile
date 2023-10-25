# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory and install the adopt package
WORKDIR /get_data
COPY . /get_data
RUN pip install -r requirements.txt

# Install gcc & cron
RUN apt-get update && apt-get install gcc -y && apt-get clean

COPY crontab.yaml /etc/yacron.d/yacrontab.yaml

CMD /usr/local/bin/yacron