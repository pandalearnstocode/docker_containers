FROM frolvlad/alpine-miniconda3:python3.6
RUN conda update -n base -c defaults conda
RUN source activate base
RUN pip install --upgrade pip
RUN apk add gcc libc-dev make
COPY ./numstackpro.yml /
COPY ./numstackpro.txt /
COPY ./numstackpro-dev.yml /
# If prod
# RUN conda env update -f numstackpro.yml \
#     && rm -rf /var/cache/apk/* && rm -rf /tmp/* && rm -rf ~/.cache/pip \
#     && conda clean --all && conda clean -afy 
# Id dev
RUN conda env update -f numstackpro-dev.yml \
    && rm -rf /var/cache/apk/* && rm -rf /tmp/* && rm -rf ~/.cache/pip \
    && conda clean --all && conda clean -afy 
COPY ./start.sh /start.sh
RUN chmod +x /start.sh
COPY ./gunicorn_conf.py /gunicorn_conf.py
COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh
COPY ./app /app
WORKDIR /app/
ENV PYTHONPATH=/app
EXPOSE 80
# If dev
EXPOSE 8888
CMD ["/start.sh"]