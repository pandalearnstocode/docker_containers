```
docker build -t numstackallinone:alpine-miniconda3-python3.6 .
docker run -d -p 80:80 numstackallinone:alpine-miniconda3-python3.6
docker run -it numstackallinone:alpine-miniconda3-python3.6 sh
docker stop $(docker ps -aq)
```