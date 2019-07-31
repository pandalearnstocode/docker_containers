```
docker build -t numstackexperimental:alpine-miniconda3-python3.6 .
docker run -d -p 80:80 numstackexperimental:alpine-miniconda3-python3.6
docker run -it numstackexperimental:alpine-miniconda3-python3.6 sh
docker stop $(docker ps -aq)
```