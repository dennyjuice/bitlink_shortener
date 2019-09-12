# Сокращатель ссылок с помощью API Bit.ly

Консольная утилитка на Python, которая сокращает ссылки или выводит кол-во кликов по битлинку.

### Как установить

Ключ API можно найти зарегистрировавшись в сервисе bit.ly, в настройках профиля -> Generic Access Token
Затем создайте в корне проекта файл ".env" и запишите в него:

```
BITLY_TOKEN=ваш ключ апи
```

Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

### Запуск

```
python main.py "ссылка"
```

Если на входе будет ссылка битлинк, то выведется кол-во кликов по ней за все время, если любая другая, то она сократится и выведется сокращенная ссылка (битлинк)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).