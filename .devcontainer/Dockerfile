FROM python:3.9-slim

# Create a non-root user
RUN groupadd --gid 121 mane && \
    useradd --uid 1000 --gid 121 --create-home --shell /bin/bash mane

# Set up the environment for the non-root user
ENV HOME=/home/mane
ENV PATH="${HOME}/.local/bin:${PATH}"

# Install other necessary tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ssh \
        git \
        vim \
        curl \
        sudo && \
    rm -rf /var/lib/apt/lists/*

# Allow the non-root user to use sudo without a password
RUN echo "mane ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Switch to the non-root user
USER mane

# Set the working directory
WORKDIR /workspace
