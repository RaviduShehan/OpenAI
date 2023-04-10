FROM python:buster
WORKDIR /MainApp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src src
EXPOSE 5000
ENTRYPOINT ["python", "./src/main.py"]