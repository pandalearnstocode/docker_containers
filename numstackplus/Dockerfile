FROM frolvlad/alpine-miniconda3:python3.6
RUN pip install --upgrade pip
RUN apk add gcc libc-dev make
COPY ./numstackplus.yml /
COPY ./numstackplus.txt /
RUN conda env update -f numstackplus.yml \
    && rm -rf /var/cache/apk/* && rm -rf /tmp/* && rm -rf ~/.cache/pip \
    && conda clean --all && conda clean -afy 
RUN source activate base
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
COPY ./gunicorn_conf.py /gunicorn_conf.py
COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh
COPY ./app /app
WORKDIR /app/
ENV PYTHONPATH=/app
EXPOSE 80
CMD ["/start.sh"]