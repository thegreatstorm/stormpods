FROM centos:latest
# Centos Latest
RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y git ansible ncurses
RUN echo "alias ll='ls -l --color=auto'" >> /root/.bashrc

RUN mkdir -p /opt/server/