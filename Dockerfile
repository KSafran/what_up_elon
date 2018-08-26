FROM python:3.7
COPY . /my_app
WORKDIR /my_app
RUN pip3 install -r requirements.txt
EXPOSE 80
ENV ER_KEY=keys/event_reg_key.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
