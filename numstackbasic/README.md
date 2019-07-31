```
docker build -t numstackpro:alpine-miniconda3-python3.6 .
docker run -d -p 80:80 numstackpro:alpine-miniconda3-python3.6
docker run -it numstackpro:alpine-miniconda3-python3.6 sh
docker stop $(docker ps -aq)
```