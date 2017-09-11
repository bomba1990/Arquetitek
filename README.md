export DJANGO_SETTINGS_MODULE=config.settings.local_development


Docker build

docker build .   --build-arg REQUIREMENTS=production.txt