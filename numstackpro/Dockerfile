FROM frolvlad/alpine-miniconda3:python3.6

# RUN apk add gcc libc-dev make
# COPY ./numstackpro.yml /
# COPY ./numstackpro.txt /
# RUN conda env update -f numstackpro.yml \
#     && rm -rf /var/cache/apk/* && rm -rf /tmp/* && rm -rf ~/.cache/pip \
#     && conda clean --all && conda clean -afy 
# RUN source activate base
###################################################################################
RUN pip install --upgrade pip

RUN apk add --no-cache --virtual .build-deps gcc libc-dev make \
    && pip --no-cache-dir install uvicorn gunicorn fastapi pydantic \
    && apk del .build-deps gcc libc-dev make

RUN conda update -n base -c defaults conda

RUN conda config --add channels intel \
    && conda install -y -c intel numpy==1.16.3 \
    && conda install -y -c intel numba==0.44.1 \
    && conda install -y -c intel cython==0.29.6 \
    && conda install -y -c intel scipy==1.2.1 \
    && conda install -y -c intel scikit-learn==0.20.3 \
    && conda install -y -c intel pandas==0.24.2 \
    && conda clean --all \
    && conda clean -afy 

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