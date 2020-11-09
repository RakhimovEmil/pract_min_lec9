FROM python:3
RUN pip3 install flask \
    && python3 -m pip install requests 
COPY controller.py /
EXPOSE 8080
ENTRYPOINT ["python3", "controller.py"]
