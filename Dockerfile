FROM python:3.7
COPY . /my_app
WORKDIR /my_app
RUN pip3 install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python"]
CMD ["run.py"]
