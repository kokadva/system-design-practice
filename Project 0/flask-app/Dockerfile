FROM python:3.7.9-alpine
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]