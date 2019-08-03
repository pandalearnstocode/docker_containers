FROM frolvlad/alpine-miniconda3:python3.6
COPY ./production.yml /
RUN conda env update -f production.yml \
    && rm -rf /var/cache/apk/* && rm -rf /tmp/* && rm -rf ~/.cache/pip \
    && conda clean --all && conda clean -afy
COPY ./production.txt /
RUN pip install --upgrade pip
RUN apk add --no-cache --virtual .build-deps gcc libc-dev make \
    && pip3 --no-cache-dir install -r production.txt \
    && apk del .build-deps gcc libc-dev make
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