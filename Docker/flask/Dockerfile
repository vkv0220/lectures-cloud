FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV API_KEY="your_key"
ENV NAME="Your name"
ENV FLASK_APP="hello.py"
COPY . /app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
