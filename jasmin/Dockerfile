FROM jookies/jasmin

RUN apt-get update
RUN apt-get install -y wget
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install redis && python-mimeparse
RUN apt-get install -y python-psycopg2
#RUN sed 's/#publish_submit_sm_resp = False/publish_submit_sm_resp = True/' /etc/jasmin/jasmin.cfg > /etc/jasmin/1jasmin.cfg
#RUN rm -f /etc/jasmin/jasmin.cfg && mv /etc/jasmin/1jasmin.cfg /etc/jasmin/jasmin.cfg
#RUN chown jasmin:jasmin /etc/jasmin/jasmin.cfg
COPY restAPI.conf /etc/supervisor/conf.d/
COPY sms_logger.conf /etc/supervisor/conf.d/
COPY sms_logger.py /
RUN chmod 777 /sms_logger.py
COPY filtres/* /filtres/
RUN chmod 777 /filtres/*
