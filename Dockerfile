FROM isatools/isatools:3.6-slim-stretch-0.9.4

MAINTAINER PhenoMeNal-H2020 Project ( phenomenal-h2020-users@googlegroups.com )

LABEL Description="Tools to query MetaboLights ISA-Tab"
LABEL software.version="0.9.4"
LABEL version="0.6"
LABEL software="mtblisa"


ADD run_test.sh /usr/local/bin/run_test.sh
ADD test_query.json /test_query.json
RUN chmod +x /usr/local/bin/run_test.sh

ADD run_mtblisa.py /usr/local/bin/run_mtblisa.py
RUN chmod a+x /usr/local/bin/run_mtblisa.py

ENTRYPOINT ["run_mtblisa.py"]
