![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Aiogram](https://img.shields.io/badge/Aiogram-3.x-red)
![License](https://img.shields.io/badge/license-MIT-green)


# 🎭 Golden Mask Bot



A Telegram bot for the **“Golden Mask”** event, built with **Aiogram 3**.  
The bot provides event information, menus, contacts, activities, and includes tools for **broadcasting**, **inviting users**, and **running giveaways**.

## 🚀 Features

### 📌 User Features
- Welcome video on `/start`
- Main menu with event sections
- Legend of the event  
- Program schedule  
- Menu and activities  
- Animation and restaurant info  
- Contacts and address  
- Easily editable YAML-based content

### 👑 Admin Features
- `/broadcast` — send a message to all users
- `/invite` — send a “participate” button to all users
- `/draw` — randomly pick a giveaway winner
- `/reset_draw` — clear all participants

## 📁 Project Structure

```
project/
│── app/
│   ├── handlers.py        # Commands and callback handlers
│   ├── db.py              # SQLite functions 
│   ├── keyboards.py       # Inline keyboard layouts
│   ├── config_loader.py   # Loads YAML content
│   ├── content.yaml       # Texts for menus and sections
│── run.py                 # Bot entry point
│── requirements.txt
│── README.md
│── .gitignore
```

## ✏️ Editing Content (YAML Configuration)

All content is inside `app/content.yaml`.

Example:

```yaml
start_text: "Welcome to the Golden Mask!"
legend: "The legend of the evening..."
program: "Event Program:"
menu: "Menu:"
activities: "Activities available"
contacts: "Event address"
restraunts: "Restaurant information"
animation: "Animation zone"
sales: "Special offers"
dress: "Dress code"
```

## 👑 How to Add an Administrator

Admin ID is in `handlers.py`:

```python
ADMIN_ID = 412718651
```

To add a new admin:

1. Ask them to open **@userinfobot**
2. Copy their numeric **user ID**
3. Edit:

```python
ADMIN_ID = [412718651, NEW_ADMIN_ID]
```

## ▶️ Installation & Running

### 1. Create a virtual environment
```
python -m venv .venv
```

### 2. Activate it  
Windows:
```
.venv\Scripts\activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Create `.env` file
```
API_KEY=your_bot_token_here
```

### 5. Run the bot
```
python run.py
```

## 🛠️ Requirements
- Python **3.10+**
- Telegram Bot API token from **@BotFather**
- Aiogram **3.x**

## 💛 Author
Developed with love by **Ilya Novo** 🖤✨
