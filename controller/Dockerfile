FROM python:3
RUN pip3 install flask \
    && python3 -m pip install requests \
    && pip3 install pymongo \
    && pip3 install redis
COPY controller.py /
COPY service.py /
COPY repository.py /
EXPOSE 8080 6379 27017
ENTRYPOINT ["python3", "controller.py"]
