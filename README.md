# 🏛️ Portal Group — Социальный Форум в Золотых Тонах

![Python](https://img.shields.io/badge/Python-3.12-ffd700?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-6.0-092e20?style=for-the-badge&logo=django)
![UI](https://img.shields.io/badge/UI-Dark_Gold-black?style=for-the-badge)

**Portal Group** — это современная платформа для обсуждений, выполненная в элегантной темной эстетике с золотыми акцентами. Проект ориентирован на удобство ведения дискуссий и визуальный комфорт.

---

## 📸 Скриншоты интерфейса

| Главная страница | Страница поста | Профиль пользователя |
| :---: | :---: | :---: |
| ![Home Page](https://raw.githubusercontent.com/Top1pro5/Portal-Group/main/screenshots/home.png) | ![Post Detail](https://raw.githubusercontent.com/Top1pro5/Portal-Group/main/screenshots/post.png) | ![Profile](https://raw.githubusercontent.com/Top1pro5/Portal-Group/main/screenshots/profile.png) |

---

## ✨ Ключевые возможности

- **🎨 Дизайн "Black & Gold":** Кастомный CSS с использованием градиентов, теней и глубокого черного цвета.
- **🖼️ Авто-оптимизация медиа:** При загрузке огромных фото (более 800px) система автоматически сжимает их с помощью Pillow, сохраняя место на сервере.
- **💬 Умные обсуждения:** Поддержка многоуровневых ответов внутри одного поста.
- **🔒 Безопасность:** Интегрированная система авторизации Django с кастомными формами регистрации.

## 🛠 Технологический стек

- **Backend:** Python 3.12 + Django 6.0
- **Database:** SQLite (локально)
- **Frontend:** CSS3 (Custom Variables, Flexbox, Grid)
- **Image Processing:** Pillow

---

## 🚀 Быстрый старт

### 1. Подготовка окружения
Клонируйте проект и создайте виртуальную среду:
```bash
git clone [https://github.com/Top1pro5/Portal-Group.git](https://github.com/Top1pro5/Portal-Group.git)
cd Portal-Group
python -m venv .venv
# Для Windows:
.venv\Scripts\activate
# Для Linux/Mac:
source .venv/bin/activate
```
### 2. Установка зависимостей
```bash
pip install django Pillow
```
### 3. Инициализация базы данных
-Создайте таблицы и суперпользователя (админа):
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
### 4. Запуск
```bash
python manage.py runserver
```

# 📂 Структура проекта

**apps/accounts/**— логика пользователей, профили и форум.

**templates/**— HTML-шаблоны

**static/**— CSS стили и кастомные скрипты.

**media/**— место хранения загруженных пользователями фото.

# 🤝 Контакты

Автор: Top1pro5

Проект находится в стадии активной разработки.
