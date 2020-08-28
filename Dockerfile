FROM python:3.8.5

ADD pip.conf /root/.config/pip/pip.conf
RUN pip3 install websockets asyncio

ADD ./main.py /opt/
WORKDIR /opt

EXPOSE 5678
CMD ["python3", "main.py"]
