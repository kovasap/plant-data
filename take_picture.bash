#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

raspistill -w 1296 -h 972 -t 1 -vf -hf -o ~/plant-data/pics/$DATE.jpg
