# jenkins/Dockerfile
FROM jenkins/jenkins:lts
USER root
RUN curl -L "https://github.com/docker/compose/releases/download/v2.2.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose
RUN jenkins-plugin-cli --plugins blueocean git docker-workflow
USER jenkins
