FROM python:3.10.8
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN apt-get update -y && \
    apt-get install build-essential cmake pkg-config gcc g++ python3-setuptools -y --force-yes
RUN pip install dlib==19.9.0
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["qFinder.py"]