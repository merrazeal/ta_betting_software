wget --method=HEAD http://elasticsearch_line_provider:9200/events
if [ $? -ne 0 ]; then
    curl -X PUT "http://elasticsearch_line_provider:9200/events" -H 'Content-Type: application/json' -d @/tmp/es_dump/event_mapping.json
    multielasticdump \
        --direction=load \
        --input=/tmp/es_dump/data \
        --output=http://elasticsearch_line_provider:9200 \
        --ignoreType='mapping' \
        --ignoreType='settings' \
        --ignoreType='template' \
        --ignoreChildError=true \

    echo "ElasticSearch restore completed"
else
    echo "ElasticSearch restore already done"
fi
