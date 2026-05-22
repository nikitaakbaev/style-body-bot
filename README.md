# Style Body Bot

Telegram-бот без ИИ для примерного определения типа женской фигуры по трем параметрам: грудь, талия и бедра. Бот показывает тип фигуры, объясняет причину выбора и дает рекомендации по фасонам одежды.

## Что умеет бот

- принимает обхват груди, талии и бедер;
- проверяет, что значения являются числами от 40 до 200 см;
- определяет примерный тип фигуры;
- сохраняет последний результат пользователя в SQLite;
- показывает сохраненный результат по кнопке "Мой результат" или командам `/result` и `/profile`;
- позволяет пересчитать параметры заново.

## Создание бота через BotFather

1. Откройте Telegram и найдите `@BotFather`.
2. Отправьте команду `/newbot`.
3. Укажите название и username бота.
4. Скопируйте токен, который выдаст BotFather.

## Установка

```bash
cd style_body_bot
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Настройка .env

Создайте файл `.env` рядом с `.env.example`:

```bash
cp .env.example .env
```

Заполните токен:

```env
BOT_TOKEN=your_telegram_bot_token
DATABASE_URL=sqlite+aiosqlite:///style_bot.db
```

## Запуск

```bash
python app.py
```

При первом запуске бот автоматически создаст SQLite-базу `style_bot.db`.

## Проверка тестами

```bash
python -m unittest discover -s tests
```

## Ручное тестирование

1. Запустите бота командой `python app.py`.
2. Откройте бота в Telegram и отправьте `/start`.
3. Нажмите "Определить тип фигуры".
4. Введите по очереди грудь, талию и бедра в сантиметрах.
5. Проверьте, что бот показывает тип фигуры, причину и рекомендации.
6. Нажмите "Мой результат" и убедитесь, что последний расчет сохранен.
7. Нажмите "Рассчитать заново" и проверьте обновление результата.
8. Введите некорректные значения, например `abc`, `20`, `250`, и убедитесь, что бот просит повторить ввод.

## Структура проекта

```text
style_body_bot/
├─ app.py
├─ config.py
├─ .env.example
├─ requirements.txt
├─ README.md
├─ database/
│  ├─ db.py
│  └─ models.py
├─ handlers/
│  ├─ fallback.py
│  ├─ start.py
│  ├─ measurements.py
│  └─ profile.py
├─ keyboards/
│  └─ main.py
├─ services/
│  ├─ body_type_detector.py
│  └─ recommendations.py
├─ utils/
│  └─ validators.py
└─ tests/
   ├─ test_body_type_detector.py
   ├─ test_recommendations.py
   └─ test_validators.py
```
