FROM python:3.7

ADD ./mockserver/ /mockserver/
ADD Pipfile /
ADD Pipfile.lock /

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system --deploy

CMD ["python","-m","mockserver"]