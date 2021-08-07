FROM selenium/standalone-chrome:91.0

WORKDIR /synctube-rpa-tunkki

COPY rpa-tunkki.py /synctube-rpa-tunkki

RUN sudo apt update

RUN sudo apt install -y python3-pip

RUN pip3 install selenium

ENTRYPOINT ["python3", "rpa-tunkki.py"]
