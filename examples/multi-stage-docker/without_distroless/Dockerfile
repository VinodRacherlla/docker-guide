###########################################
# BASE IMAGE
###########################################

FROM ubuntu AS build

WORKDIR /app

RUN apt update && apt install -y python3 

COPY . /app

EXPOSE 8080

ENTRYPOINT ["python3", "app.py"]