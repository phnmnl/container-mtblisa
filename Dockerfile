FROM ubuntu:16.04

MAINTAINER PhenoMeNal-H2020 Project ( phenomenal-h2020-users@googlegroups.com )

LABEL Description="Tools to query MetaboLights ISA-Tab"
LABEL software.version="0.7.1"
LABEL version="0.2"
LABEL software="mtblisa"

RUN apt-get update && apt-get install -y --no-install-recommends python3-pip python3-dev build-essential && \
    pip3 install --upgrade pip && \
    pip3 install -U setuptools && \
    pip3 install isatools==0.7.1 argparse==1.4.0 && \
    apt-get purge -y python3-pip gcc libxml2-dev libxslt-dev python3-lxml python3-dev build-essential && \
    apt-get install --no-install-recommends python3 && \
    apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD run_test.sh /usr/local/bin/run_test.sh
RUN chmod +x /usr/local/bin/run_test.sh

ADD run_mtblisa.py /usr/local/bin/run_mtblisa.py
RUN chmod a+x /usr/local/bin/run_mtblisa.py

ENTRYPOINT ["run_mtblisa.py"]
