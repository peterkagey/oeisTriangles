FROM public.ecr.aws/lambda/python:3.8

RUN pip install tweepy
RUN pip install Pillow -t .

COPY data.json ./
COPY b_file_parser.py ./
COPY b_file_lookup.py ./
COPY triangle_drawer.py ./
COPY sequence_drawer.py ./
COPY oeis_drawer.py ./
COPY json_accountant.py ./
COPY app.py ./


CMD ["app.handler"]
