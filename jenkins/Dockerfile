# jenkins/Dockerfile
FROM jenkins/jenkins:lts
USER root
RUN jenkins-plugin-cli --plugins blueocean git docker-workflow
USER jenkins