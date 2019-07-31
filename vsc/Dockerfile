# the base miniconda3 image
FROM frolvlad/alpine-miniconda3:python3.6

# load in the environment.yml file - this file controls what Python packages we install
ADD environment.yml /
RUN pip install --upgrade pip
RUN apk add gcc libc-dev make

# install the Python packages we specified into the base environment
RUN conda update -n base conda -y && conda env update

# download the coder binary, untar it, and allow it to be executed
RUN wget https://github.com/codercom/code-server/releases/download/1.1156-vsc1.33.1/code-server1.1156-vsc1.33.1-linux-x64.tar.gz \
    && tar -xzvf code-server1.1156-vsc1.33.1-linux-x64.tar.gz && chmod +x code-server1.1156-vsc1.33.1-linux-x64/code-server

# add in the code folder
ADD ./code/ /code
RUN apk add --update bash
COPY ./docker-entrypoint.sh /
CMD ["sh", "docker-entrypoint.sh"]
# ENTRYPOINT ["bin/sh","docker-entrypoint.sh"]