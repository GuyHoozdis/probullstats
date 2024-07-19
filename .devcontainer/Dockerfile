FROM mcr.microsoft.com/devcontainers/python:3.11 as builder

RUN apt update && sudo apt install -y --no-install-recommends \
    build-essential \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    libsqlite3-dev


# ==============================================================================
# Parallel Build Intermediate Layers
# ==============================================================================
FROM builder as py38

WORKDIR ${HOME}/build

RUN wget https://www.python.org/ftp/python/3.8.19/Python-3.8.19.tgz && \
    tar xvf Python-3.8.19.tgz && \
    ./Python-3.8.19/configure --enable-optimizations && \
    make altinstall


FROM builder as py39

WORKDIR ${HOME}/build

RUN wget https://www.python.org/ftp/python/3.9.19/Python-3.9.19.tgz && \
    tar xvf Python-3.9.19.tgz && \
    ./Python-3.9.19/configure --enable-optimizations && \
    make altinstall


FROM builder as py310

WORKDIR ${HOME}/build

RUN wget https://www.python.org/ftp/python/3.10.14/Python-3.10.14.tgz && \
    tar xvf Python-3.10.14.tgz && \
    ./Python-3.10.14/configure --enable-optimizations && \
    make altinstall


FROM builder as py312

WORKDIR ${HOME}/build

RUN wget https://www.python.org/ftp/python/3.12.4/Python-3.12.4.tgz && \
    tar xvf Python-3.12.4.tgz && \
    ./Python-3.12.4/configure --enable-optimizations && \
    make altinstall


# ==============================================================================
# Dev Container
# ==============================================================================
FROM mcr.microsoft.com/devcontainers/python:3.11 as dev

COPY --from=py38 /usr/local/include/python3.8/ /usr/local/include/python3.8/
COPY --from=py38 /usr/local/bin/python3.8 /usr/local/bin/
COPY --from=py38 /usr/local/bin/python3.8-config /usr/local/bin/
COPY --from=py38 /usr/local/share/man/man1/python3.8.1 /usr/local/share/man/man1/
COPY --from=py38 /usr/local/lib/python3.8/ /usr/local/lib/python3.8/
COPY --from=py38 /usr/local/lib/libpython3.8.a /usr/local/lib/

COPY --from=py39 /usr/local/include/python3.9/ /usr/local/include/python3.9/
COPY --from=py39 /usr/local/bin/python3.9 /usr/local/bin/
COPY --from=py39 /usr/local/bin/python3.9-config /usr/local/bin/
COPY --from=py39 /usr/local/share/man/man1/python3.9.1 /usr/local/share/man/man1/
COPY --from=py39 /usr/local/lib/python3.9/ /usr/local/lib/python3.9/
COPY --from=py39 /usr/local/lib/libpython3.9.a /usr/local/lib/

COPY --from=py310 /usr/local/include/python3.10/ /usr/local/include/python3.10/
COPY --from=py310 /usr/local/bin/python3.10 /usr/local/bin/
COPY --from=py310 /usr/local/bin/python3.10-config /usr/local/bin/
COPY --from=py310 /usr/local/share/man/man1/python3.10.1 /usr/local/share/man/man1/
COPY --from=py310 /usr/local/lib/python3.10/ /usr/local/lib/python3.10/
COPY --from=py310 /usr/local/lib/libpython3.10.a /usr/local/lib/

COPY --from=py312 /usr/local/include/python3.12/ /usr/local/include/python3.12/
COPY --from=py312 /usr/local/bin/python3.12 /usr/local/bin/python3.12
COPY --from=py312 /usr/local/bin/python3.12-config /usr/local/bin/python3.12-config
COPY --from=py312 /usr/local/share/man/man1/python3.12.1 /usr/local/share/man/man1/python3.12.1
COPY --from=py312 /usr/local/lib/python3.12/ /usr/local/lib/python3.12/
COPY --from=py312 /usr/local/lib/libpython3.12.a /usr/local/lib/libpython3.12.a


RUN apt update && apt install -y --no-install-recommends \
    httpie \
    silversearcher-ag

RUN pipx install poetry && pipx ensurepath
