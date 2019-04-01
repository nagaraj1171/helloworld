from ubuntu:18.04
RUN ["apt-get", "update"]
RUN ["apt-get", "upgrade", "-y", "--fix-missing"]
RUN apt-get update && apt-get -y install locales build-essential python python3 python3-pip
RUN mkdir -p /opt/helloworld
COPY . /opt/helloworld
WORKDIR /opt/helloworld
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["helloWorld/app.py"]
