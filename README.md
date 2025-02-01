# Yatube API Documentation

## Описание проекта

**Yatube** — это социальная сеть для публикации постов, комментариев и подписок на других пользователей. API предоставляет возможность взаимодействовать с функционалом Yatube через HTTP-запросы.

## Установка и запуск

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/yatube-api.git
    cd yatube-api
    ```

2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

3. Примените миграции:
    ```bash
    python manage.py migrate
    ```

4. Запустите сервер:
    ```bash
    python manage.py runserver
    ```

## Использование API

### Получение JWT-токена

Для работы с API необходимо получить JWT-токен через эндпоинт:

```http
POST /api/v1/jwt/create/
```

Пример запроса:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Пример ответа:

```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

## Основные эндпоинты

### Публикации
```http
GET /api/v1/posts/ - Получить список всех публикаций.
POST /api/v1/posts/ - Создать новую публикацию.
GET /api/v1/posts/{id}/ - Получить публикацию по ID.
PUT /api/v1/posts/{id}/ - Обновить публикацию по ID.
PATCH /api/v1/posts/{id}/ - Частично обновить публикацию по ID.
DELETE /api/v1/posts/{id}/ - Удалить публикацию по ID.
```

### Комментарии
```http
GET /api/v1/posts/{post_id}/comments/ - Получить все комментарии к публикации.
POST /api/v1/posts/{post_id}/comments/ - Добавить новый комментарий к публикации.
GET /api/v1/posts/{post_id}/comments/{id}/ - Получить комментарий по ID.
PUT /api/v1/posts/{post_id}/comments/{id}/ - Обновить комментарий по ID.
PATCH /api/v1/posts/{post_id}/comments/{id}/ - Частично обновить комментарий по ID.
DELETE /api/v1/posts/{post_id}/comments/{id}/ - Удалить комментарий по ID.
```

### Сообщества
```http
GET /api/v1/groups/ - Получить список всех сообществ.
GET /api/v1/groups/{id}/ - Получить информацию о сообществе по ID.
```

### Подписки
```http
GET /api/v1/follow/ - Получить список подписок пользователя.
POST /api/v1/follow/ - Подписаться на другого пользователя.
```

## Примеры запросов

### Получение списка публикаций
```bash
curl -X GET http://localhost:8000/api/v1/posts/ -H "Authorization: Bearer your_access_token"
```

### Создание новой публикации
```bash
curl -X POST http://localhost:8000/api/v1/posts/ \
  -H "Authorization: Bearer your_access_token" \
  -H "Content-Type: application/json" \
  -d '{"text": "Новая публикация"}'
```

## Авторизация
Для доступа к защищенным эндпоинтам необходимо использовать JWT-токен, полученный через `/api/v1/jwt/create/`. Токен должен быть передан в заголовке `Authorization` в формате `Bearer <ваш_токен>`.

