#!/bin/bash

#Build the Docker Image
sudo docker build -t lighthouse-qa-image .

#Run the Docker contatiner with log mounting
sudo docker run -it --rm -v "$(pwd)/tests/logs:/app/tests/logs" lighthouse-qa-image