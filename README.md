# Описание проекта

Проект представляет собой телеграмм-бота, который отслеживает резкие колебания курсов валют и отправляет уведомления пользователям о значительных изменениях. Для этого используется API для получения данных о курсах валют, анализ этих данных и отправка уведомлений через Telegram.

## Архитектура проекта

### Класс CurrencyAPI:
- **Поля:**
  - api_url (строка) - URL API для получения данных о курсах валют.
- **Методы:**
  - get_currency_data(): Метод для отправки запроса к API и получения данных о курсах валют.

### Класс CurrencyAnalyzer:
- **Поля:**
  - currency_data (список словарей) - данные о курсах валют.
- **Методы:**
  - analyze_currency_data(): Метод для анализа данных о курсах и определения резких колебаний.

### Класс TelegramBot:
- **Поля:**
  - bot_token (строка) - токен бота в Telegram.
- **Методы:**
  - send_notification(user_id, message): Метод для отправки уведомления пользователю с указанным ID.

### Класс MainApp:
- **Методы:**
  - main(): Основной метод приложения, который объединяет работу с классами CurrencyAPI, CurrencyAnalyzer и TelegramBot. Получает данные о курсах валют, анализирует их и отправляет уведомления при необходимости.

Эти классы взаимодействуют между собой для получения данных, их анализа и отправки уведомлений. Каждый класс отвечает за свою четко определенную функциональность, что обеспечит легкость поддержки и расширения проекта в будущем.
