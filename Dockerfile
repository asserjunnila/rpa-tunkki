FROM selenium/standalone-chrome

WORKDIR /tests

COPY test.py /tests

RUN sudo apt update

RUN sudo apt install -y python3-pip

RUN pip3 install selenium

RUN pip3 install webdriver_manager

ENTRYPOINT ["python3", "test.py"]
