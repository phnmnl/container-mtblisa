FROM python:3-onbuild
LABEL Description="Tools to query MetaboLights ISA-Tab"
MAINTAINER David Johnson, david.johnson@oerc.ox.ac.uk
RUN pip install isatools --upgrade
ADD run_mtblisa.py /
ADD requirements.txt /
ENTRYPOINT ["python", "run_mtblisa.py"]