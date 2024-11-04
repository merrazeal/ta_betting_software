FROM elasticdump/elasticsearch-dump:latest

WORKDIR /app

RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["sh", "/tmp/es_dump/entrypoint.sh"]
