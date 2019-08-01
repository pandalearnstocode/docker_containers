```
docker build -t numstackpro:alpine-miniconda3-python3.6 .
docker run -d -p 80:80 numstackpro:alpine-miniconda3-python3.6
docker run -d -p 80:80 -p 8888:8888 numstackpro:alpine-miniconda3-python3.6
docker run -it numstackpro:alpine-miniconda3-python3.6 sh
docker stop $(docker ps -aq)
```

docker run -d -p 80:80 -p 8888:8888 numstackpro:alpine-miniconda3-python3.6