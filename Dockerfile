FROM python:3.10.4-slim

RUN apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev build-essential libpq-dev

RUN pip install pipenv --upgrade

COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --system

COPY ./app /app

WORKDIR /app

EXPOSE 8000

ENTRYPOINT ["/bin/bash"]
CMD ["app/run-app.sh"]
