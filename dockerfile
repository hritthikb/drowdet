FROM ubuntu:latest MAINTAINER Ilya Pukhov "ilya.pukhov@gmail.com" 
RUN apt-get update -y 
RUN apt-get install -y python3-pip
python3-dev
build-essential
cmake COPY . /app WORKDIR /app RUN pip3 install flask RUN pip3 install dlib ENTRYPOINT ["python3"] CMD ["app.py"]
