#!/bin/bash

IMAGE=movie_analisis 

# Running Jupyter Notebook
#docker run --rm -p 8890:8888 -e GRANT_SUDO=yes --user root -v $PWD/notebooks:/home/jovyan/notebooks $IMAGE


# Running JupyterLab
docker run --rm --network="host" -p 8888:8888 -e GRANT_SUDO=yes -e JUPYTER_ENABLE_LAB=yes --user root -v $PWD/work:/home/jovyan/work $IMAGE 

