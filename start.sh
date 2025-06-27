#!/bin/bash

echo "Costruzione e avvio del progetto Docker..."
sudo docker-compose down
sudo docker-compose build --no-cache
sudo docker-compose up
