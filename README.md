export DJANGO_SETTINGS_MODULE=config.settings.local_development


Docker build

docker build .   --build-arg REQUIREMENTS=production.txt


CREATE USER arquetitek WITH PASSWORD 'n3yNde36Gb@E*nM2';
CREATE DATABASE arquetitek OWNER arquetitek;