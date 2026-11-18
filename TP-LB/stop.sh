#!/bin/bash
#arret des conteneurs
docker stop nginx-lb nginx1 nginx2

#suppression
docker network rm tplb
