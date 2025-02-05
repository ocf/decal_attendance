#!/bin/bash

curl -X POST 127.0.0.1:16000 \
	-F "host=$(hostname)" \
	-F "username=$(whoami)" \
	-F "time=$(date)"
