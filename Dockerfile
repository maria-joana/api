# Pull official base image
FROM python:3.10-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/venv/bin:$PATH"

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev libc-dev linux-headers zlib zlib-dev && \
    /venv/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps

# Set work directory
RUN mkdir /api
WORKDIR /api

#Copy project
COPY ./api/ /api

# Configure static and media files
RUN adduser --disabled-password --no-create-home api && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R api:api /vol && \
    chmod -R 755 /vol

USER api
VOLUME /vol/web

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "api.wsgi"]
