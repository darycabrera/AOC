# https://hub.docker.com/_/python
# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon)
ARG VARIANT=3-bullseye
FROM python:${VARIANT}

# Add python requirements via pip to image
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

# Install additional OS packages
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends vim