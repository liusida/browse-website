# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3-bullseye, 3.10-bullseye, 3-buster, 3.10-buster
ARG VARIANT=3-bullseye
FROM --platform=linux/amd64 python:3.10

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    # Remove imagemagick due to https://security-tracker.debian.org/tracker/CVE-2019-10131
    && apt-get purge -y imagemagick imagemagick-6-common

# Install Chrome for web browsing
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_$(dpkg --print-architecture).deb -o /tmp/chrome.deb \
    && apt-get -y install /tmp/chrome.deb
