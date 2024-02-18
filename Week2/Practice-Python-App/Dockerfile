FROM  faucet/python3

WORKDIR /app

COPY . /app

RUN pip install Flask

CMD ["flask", "--app","app", "run"]

EXPOSE 5000