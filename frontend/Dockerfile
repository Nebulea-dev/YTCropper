FROM debian:latest

RUN apt update \
    && apt install -y curl unzip \
    && apt -y autoclean

# Install Node Version Manager
ENV NVM_DIR=/usr/local/nvm
ENV NODE_VERSION=20.17.0

RUN mkdir -p $NVM_DIR

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

RUN . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

# Install Bun
RUN curl -fsSL https://bun.sh/install | bash
ENV PATH="/root/.bun/bin:$PATH"

COPY . /app
WORKDIR /app
RUN bun install

# Start webserver
CMD bun run dev
#RUN bun run build
#CMD bun run preview
