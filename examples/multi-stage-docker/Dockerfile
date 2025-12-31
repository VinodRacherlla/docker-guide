###########################################
# BASE IMAGE
###########################################

FROM ubuntu AS build

WORKDIR /app

RUN apt update && apt install -y python3 

COPY . /app

###########################################
# DISTOLESS FINAL IMAGE
###########################################

FROM gcr.io/distroless/python3

WORKDIR /app

COPY --from=build /app /app

EXPOSE 8080

ENTRYPOINT ["python3", "app.py"]