FROM isatools/isatools:3.6-alpine-0.9.4

MAINTAINER PhenoMeNal-H2020 Project ( phenomenal-h2020-users@googlegroups.com )

LABEL Description="Tools to query MetaboLights ISA-Tab"
LABEL software.version="0.9.4"
LABEL version="0.6.1"
LABEL software="mtblisa"

WORKDIR /mtblisa
COPY \
  run_mtblisa.py \
  run_test.sh \
  run_tests.py \
/usr/local/bin/


RUN chmod a+rx \
  /usr/local/bin/run_mtblisa.py \
  /usr/local/bin/run_test.sh \
  /usr/local/bin/run_tests.py

ENTRYPOINT ["run_mtblisa.py"]
