FROM debian:latest

# Install dependencies
RUN apt update && \ 
    apt install -y \
        make \
        build-essential \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncurses5-dev \
        libncursesw5-dev \
        xz-utils \
        tk-dev \
        libffi-dev \
        liblzma-dev \
        git

# Install pyenv
ENV PYTHON_VERSION 3.12.0
ENV PYENV_ROOT="$HOME/pyenv"
ENV PATH="$PYENV_ROOT/bin:$PATH"
ENV PATH="$PYENV_ROOT/shims:$PATH"
RUN curl https://pyenv.run | bash

# Install python
RUN pyenv install $PYTHON_VERSION
RUN pyenv global $PYTHON_VERSION

# Copy files
RUN mkdir -p /app
COPY requirements.txt /app
WORKDIR /app

# Make venv
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run server
WORKDIR /app/src
EXPOSE 5000
CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "app:app" ]
