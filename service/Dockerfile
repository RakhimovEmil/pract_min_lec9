FROM python:3
RUN pip3 install flask \
    && python3 -m pip install requests 
COPY service.py /
EXPOSE 8081
ENTRYPOINT ["python3", "service.py"]
