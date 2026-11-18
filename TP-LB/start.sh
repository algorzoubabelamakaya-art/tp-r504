#!/bin/bash
docker network create tplb

docker build -t im-nginx-lb tp-A/
#les sous dossiers
mkdir -p shared1 shared2

#fichiers html
echo "<h1>Hello 1</h1>" > shared1/index.html
echo "<h1>Hello 2</h1>" > shared2/index.html

#les 2servers
docker run -d --rm \
	--name nginx1 \
	--network tplb \
	-p 81:80 \
	--mount type=bind,source="$(pwd)"/shared1,target=/usr/share/nginx/html \
	nginx

docker run -d --rm --name nginx2 --network tplb -p 82:80 \
    --mount type=bind,source="$(pwd)"/shared2,target=/usr/share/nginx/html \
    nginx
#load balancing
docker run -d --rm --name nginx-lb --network tplb -p 83:80 im-nginx-lb

