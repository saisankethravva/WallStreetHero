#!/bin/bash

mkdir -p /creds
touch /creds/cert.pem
touch /creds/key.pem
chmod 666 /creds/cert.pem
chmod 666 /creds/key.pem
cat /creds/container_required.json | jq -r '.ssl_cert' > /creds/cert.pem
cat /creds/container_required.json | jq -r '.ssl_key' > /creds/key.pem
chmod 400 /creds/cert.pem
chmod 400 /creds/key.pem



