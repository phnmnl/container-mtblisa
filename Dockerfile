FROM isatools/isatools:3.6-alpine-0.10.0

MAINTAINER PhenoMeNal-H2020 Project ( phenomenal-h2020-users@googlegroups.com )

LABEL Description="Tools to query MetaboLights ISA-Tab"
LABEL software.version="0.10.0"
LABEL version="0.7.8"
LABEL software="isaslicer"

WORKDIR /mtblisa

RUN apk add --no-cache --virtual git-deps git openssh \
    && git clone --depth 1 --single-branch -b develop https://github.com/ISA-tools/isatools-galaxy /files/galaxy \
    && apk del git-deps \
    && rm -rf /var/cache/apk/* \
    && rm -rf /tmp/* /var/tmp/*

ENV PATH=$PATH:/files/galaxy

ADD run_test.sh /usr/local/bin/run_test.sh
ADD run_tests.py /usr/local/bin/run_tests.py
RUN cp /files/galaxy/tools/isaslicer/isaslicer.py /usr/local/bin/isaslicer.py
RUN chmod a+rx \
  /usr/local/bin/isaslicer.py \
  /usr/local/bin/run_test.sh \
  /usr/local/bin/run_tests.py

ENTRYPOINT ["isaslicer.py"]