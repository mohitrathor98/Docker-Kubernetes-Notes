FROM  faucet/python3

WORKDIR /app

COPY . /app

RUN pip install Flask pymongo requests

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

EXPOSE 5000