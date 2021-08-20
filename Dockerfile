FROM joyzoursky/python-chromedriver:latest

WORKDIR /usr/workspace
COPY ./test_script.py .
COPY ./requirements.txt .

# upgrade pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


