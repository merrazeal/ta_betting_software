# ta_betting_software

Тестовое задание в Betting Software

2 микросервиса взаимодействуют друг с другом с помощью http и канала pubsub

Создадим общую сеть

```
docker network create bsw_network
```

### Bet Maker
```
make bet_maker_build
make bet_maker_up
```

### Line Provider
```
make line_provider_build
make line_provider_up
```

Возможные улучшения:
- кеширование
- бэкофы
- тротлинг на create, update операции
- использовать rabbitmq с ack
- nginx как reverse proxy для каждого микросервиса
- мониторинг
- тесты
