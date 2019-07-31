FROM frolvlad/alpine-miniconda3:python3.6

# ENV PYTHONDONTWRITEBYTECODE=true

RUN conda update -n base -c defaults conda

RUN conda install --yes \
    nomkl \
    numpy \
    pandas \
    numba \
    scipy \
    scikit-learn \
    && conda clean -afy \
    && conda clean --all

RUN apk add --no-cache --virtual .build-deps gcc libc-dev make \
    && pip --no-cache-dir install coloredlogs uvicorn gunicorn fastapi pydantic \
    && apk del .build-deps gcc libc-dev make

RUN rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    rm -rf ~/.cache/pip

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