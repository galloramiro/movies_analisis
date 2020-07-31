FROM jupyter/scipy-notebook

ENV PYTHONDONTWRITEBYTECODE=1

ADD requirements.txt /home/$NB_USER/
RUN pip install -r requirements.txt
