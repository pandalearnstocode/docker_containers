```
docker build -t numstackcustomized:alpine-miniconda3-python3.6 .
docker run -d -p 80:80 numstackcustomized:alpine-miniconda3-python3.6
docker run -it numstackcustomized:alpine-miniconda3-python3.6 sh
docker stop $(docker ps -aq)
```