## Сценарий: Управление пользователями

В этом разделе мы рассмотрим сценарий, демонстрирующий основные операции по управлению пользователями с использованием нашего API. Сценарий включает следующие шаги:

1. Получение токена доступа
2. Получение списка пользователей
3. Создание нового пользователя
4. Обновление информации о пользователе
5. Удаление пользователя

### Шаг 1: Получение токена доступа

**Эндпоинт**: /auth/token

**Метод**: POST

**Пример запроса**:

```http
POST /auth/token HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
  "api_key": "YOUR_API_KEY",
  "username": "your_username",
  "password": "your_password"
}
```

**Пример ответа**:

```json
{
  "access_token": "YOUR_ACCESS_TOKEN",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

### Шаг 2: Получение списка пользователей

**Эндпоинт**: /users

**Метод**: GET

**Пример запроса**:

```http
GET /users HTTP/1.1
Host: api.example.com
Authorization: Bearer YOUR_ACCESS_TOKEN
```

**Пример ответа**:

```json
{
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    },
    {
      "id": 2,
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
  ]
}
```

### Шаг 3: Создание нового пользователя

**Эндпоинт**: /users

**Метод**: POST

**Пример запроса**:

```http
POST /users HTTP/1.1
Host: api.example.com
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
  "name": "Alice Johnson",
  "email": "alice.johnson@example.com"
}
```

**Пример ответа**:

```json
{
  "id": 3,
  "name": "Alice Johnson",
  "email": "alice.johnson@example.com"
}
```

### Шаг 4: Обновление информации о пользователе

**Эндпоинт**: /users/{id}

**Метод**: PUT

**Пример запроса**:

```http
PUT /users/3 HTTP/1.1
Host: api.example.com
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
  "name": "Alice Johnson",
  "email": "alice.johnson@newemail.com"
}
```

**Пример ответа**:

```json
{
  "id": 3,
  "name": "Alice Johnson",
  "email": "alice.johnson@newemail.com"
}
```

### Шаг 5: Удаление пользователя

**Эндпоинт**: /users/{id}

**Метод**: DELETE

**Пример запроса**:

```http
DELETE /users/3 HTTP/1.1
Host: api.example.com
Authorization: Bearer YOUR_ACCESS_TOKEN
```

**Пример ответа**:

```json
{
  "message": "User with ID 3 has been deleted successfully."
}
```

## Заключение
Этот сценарий демонстрирует основные операции по управлению пользователями с использованием нашего API. Вы можете использовать эти примеры для интеграции API в свои приложения и выполнения различных операций с пользователями. Подробные сведения о каждом эндпоинте и доступных операциях можно найти в соответствующих разделах документации.