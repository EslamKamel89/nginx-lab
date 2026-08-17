FROM nginx:stable

RUN apt-get update && \
    apt-get install -y \
    sudo \
    git \
    curl \
    wget \
    vim \
    less \
    tree \
    procps \
    iproute2 \
    iputils-ping \
    dnsutils \
    net-tools \
    fish \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*

