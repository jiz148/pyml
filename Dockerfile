FROM python:3

MAINTAINER Jason Zhu <jason.zhuyx@gmail.com>
LABEL maintainer="jason.zhuyx@gmail.com"
LABEL organization="Dockerian"
LABEL project="pyml"

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    bash \
    ca-certificates \
    curl \
    groff \
    jq \
    less \
    make \
    nano \
    tree \
    tar \
    wget \
    zip \
 && rm -rf /var/lib/apt/lists/* \
 && rm /bin/sh && ln -sf /bin/bash /bin/sh \
 && echo "export PS1='\n\u@\h [\w] \D{%F %T} [\#]:\n\$ '" >> ~/.bashrc \
 && echo "alias ll='ls -al'" >> ~/.bashrc \
 && echo "" >> ~/.bashrc

# install gosu
# RUN gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys \
#     B42F6819007F00F88E364FD4036A9C25BF357DD4 \
#  && curl -o /usr/local/bin/gosu -SL \
#    "https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-architecture)" \
#  && curl -o /usr/local/bin/gosu.asc -SL \
#    "https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-architecture).asc" \
#  && gpg --verify /usr/local/bin/gosu.asc \
#  && chmod +x /usr/local/bin/gosu \
#  && rm /usr/local/bin/gosu.asc

# install gosu for a better su+exec command
ARG GOSU_VERSION=1.10
RUN dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
 && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch" \
 && chmod +x /usr/local/bin/gosu \
 && gosu nobody true

COPY tools/entrypoint.sh /usr/local/bin/entrypoint.sh

ENV PROJECT=pyml \
    PROJECT_DIR=ml \
    SHELL=/bin/bash \
    SOURCE=/src

COPY $PROJECT_DIR/requirements-dev.txt $SOURCE/$PROJECT/requirements-dev.txt
COPY $PROJECT_DIR/requirements.txt $SOURCE/$PROJECT/requirements.txt

# install python dependencies, and aws cli
RUN mkdir -p $SOURCE \
 && pip install --upgrade pip \
#&& pip install -r $SOURCE/$PROJECT/requirements-dev.txt \
#&& pip install -r $SOURCE/$PROJECT/requirements.txt \
 && pip install awscli

WORKDIR $SOURCE/$PROJECT

# ENTRYPOINT ["/bin/bash", "-c"]
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["/bin/bash"]
