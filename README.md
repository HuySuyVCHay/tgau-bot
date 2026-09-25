# TG Bot — aiogram template

Простой шаблон Telegram-бота на aiogram 3.x.

## Структура

app/
├── main.py
├── handlers/    # обработчики команд и сообщений
├── keyboards/   # reply и inline клавиатуры
└── utils/       # логирование и вспомогательные модули

## Установка

1. Клонируй репозиторий и перейди в папку проекта
2. Создай виртуальное окружение и активируй его:
   python -m venv .venv
   .venv\Scripts\activate
3. Установи зависимости:
   pip install -r requirements.txt
4. Скопируй .env.example в .env и впиши свой токен бота (от @BotFather):
   BOT_TOKEN=твой_токен

## Запуск

Запускай из корня проекта:
python -m app.main