FROM frolvlad/alpine-miniconda3:python3.6
RUN conda update -n base -c defaults conda
RUN source activate base
RUN pip install --upgrade pip
RUN apk add gcc libc-dev make
COPY ./numstackpro.yml /
COPY ./numstackpro-dev.yml /
COPY ./numstackpro-staging.yml /
COPY ./numstackpro-production.yml /
ARG BUILD_ENV="DEV"
RUN if [ "$BUILD_ENV" = "DEV" ]; then mv numstackpro-dev.yml numstackpro.yml ; fi
RUN if [ "$BUILD_ENV" = "STAGING" ]; then mv numstackpro-staging.yml numstackpro.yml ; fi
RUN if [ "$BUILD_ENV" = "PRODUCTION" ]; then mv numstackpro-production.yml numstackpro.yml ; fi
RUN conda env update -f numstackpro.yml \
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
EXPOSE 8888
CMD ["/start.sh"]