```
docker build -t numstackplus:alpine-miniconda3-python3.6 .
docker run -d -p 80:80 numstackplus:alpine-miniconda3-python3.6
docker run -it numstackplus:alpine-miniconda3-python3.6 sh
docker stop $(docker ps -aq)
```