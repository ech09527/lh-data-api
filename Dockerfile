FROM python:3.11-slim
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN mkdir /app 
COPY . /app
WORKDIR /app
CMD ["fastapi", "run"]
