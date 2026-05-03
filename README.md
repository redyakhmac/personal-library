# 📚 Personal Library Dashboard | داشبورد کتابخانه شخصی

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![Flask Version](https://img.shields.io/badge/flask-2.3.3-green)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)

---

## 📖 معرفی پروژه

**داشبورد کتابخانه شخصی** یک برنامه تحت وب کامل و حرفه‌ای برای مدیریت کتاب‌های شخصی شماست. با این برنامه می‌توانید کتاب‌های خود را ثبت کنید، وضعیت مطالعه را پیگیری کنید، آمار بگیرید و از یک داشبورد زیبا و مینیمال استفاده کنید.

## ✨ قابلیت‌های اصلی

- ✅ مدیریت کامل کتاب‌ها (افزودن، ویرایش، حذف، جستجو و فیلتر)
- 📊 داشبورد تعاملی با نمودارهای آماری (وضعیت مطالعه، توزیع سالانه)
- 🌓 تم روشن و تاریک (Dark/Light Mode) با قابلیت تغییر لحظه‌ای
- 🌍 پشتیبانی از دو زبان فارسی و انگلیسی (تغییر زبان در یک کلیک)
- 👤 سیستم احراز هویت و پروفایل کاربری با قابلیت آپلود عکس
- 📱 طراحی واکنش‌گرا (Responsive) و سازگار با موبایل و تبلت
- 🎨 منوی کناری شناور با قابلیت جمع شدن برای استفاده بهتر از فضا
- 📈 امتیازدهی ستاره‌ای و یادداشت‌گذاری روی هر کتاب

### 🛠 **تکنولوژی‌های استفاده شده**

| تکنولوژی | کاربرد |
|---------|--------|
| **Python 3.10+** | زبان برنامه‌نویسی اصلی |
| **Flask** | فریمورک وب (بک‌اند) |
| **SQLAlchemy** | ORM برای ارتباط با دیتابیس |
| **SQLite** | دیتابیس داخلی و سبک |
| **Flask-Login** | مدیریت احراز هویت کاربران |
| **Bootstrap 5 (RTL)** | طراحی رابط کاربری واکنش‌گرا |
| **Chart.js** | رسم نمودارهای تعاملی |
| **FontAwesome 6** | آیکون‌های حرفه‌ای |
| **CustomTkinter** (اختیاری) | رابط گرافیکی دسکتاپ (در نسخه‌های آینده) |

## 📁 ساختار پروژه
  ```bash
personal-library/
├── app.py # فایل اصلی برنامه Flask
├── models.py # مدل‌های دیتابیس (User, Book)
├── requirements.txt # وابستگی‌های پروژه
├── .gitignore # فایل‌های نادیده گرفته شده در گیت
├── static/
│ ├── style.css # استایل‌های سفارشی
│ ├── script.js # کدهای جاوااسکریپت
│ └── profile_pics/ # عکس‌های پروفایل کاربران
├── templates/
│ ├── base.html # قالب پایه (منو و هدر)
│ ├── dashboard.html # صفحه داشبورد
│ ├── books.html # صفحه مدیریت کتاب‌ها
│ ├── add_book.html # فرم افزودن کتاب
│ ├── edit_book.html # فرم ویرایش کتاب
│ ├── settings.html # صفحه تنظیمات پروفایل
│ └── login.html # صفحه ورود و ثبت‌نام
└── locales/
├── fa.json # ترجمه فارسی
└── en.json # ترجمه انگلیسی
```


  
  
### 🚀 **نحوه نصب و اجرا**

#### پیش‌نیازها
- Python 3.10 یا بالاتر
- Git (برای clone کردن پروژه)

#### مراحل نصب (در ویندوز، لینوکس، مک)

```bash
# 1. کلون کردن پروژه از گیت‌هاب
git clone https://github.com/redyakhmac/personal-library.git
cd personal-library

# 2. ایجاد محیط مجازی پایتون (اختیاری ولی توصیه می‌شود)
python -m venv venv
# در ویندوز:
venv\Scripts\activate
# در لینوکس/مک:
source venv/bin/activate

# 3. نصب وابستگی‌ها
pip install -r requirements.txt

# 4. اجرای برنامه
python app.py
سپس در مرورگر خود آدرس http://127.0.0.1:5000 را باز کنید.
```
## 📸 پیش‌نمایش
(تصاویر زیر نمونه‌هایی از رابط کاربری هستند)


| **https://via.placeholder.com/400x200?text=Login+Page** | صفحه اصلی |

| **https://via.placeholder.com/400x200?text=Dashboard** | داشبورد |


	
	
نکته: تصاویر واقعی را می‌توانید پس از اجرای پروژه بگیرید و جایگزین کنید.

## 🎯 ویژگی‌های کلیدی در کد
ترجمه داینامیک: تابع t() در قالب‌ها به راحتی متن‌ها را بر اساس زبان کاربر ترجمه می‌کند.

تم تاریک و روشن: با متغیرهای CSS و ذخیره‌سازی در دیتابیس کاربر.

منوی کشویی: ذخیره وضعیت باز/بسته بودن منو در دیتابیس.

داشبورد تعاملی: نمودارهای دایره‌ای و میله‌ای با Chart.js.

## 🔧 توسعه و مشارکت
اگر ایده یا پیشنهادی برای بهبود پروژه دارید، خوشحال می‌شوم راهنمایی‌هایتان را دریافت کنم.

فورک (Fork) کنید

برنچ (Branch) جدیدی بسازید (git checkout -b feature/AmazingFeature)

کامیت (Commit) تغییرات خود (git commit -m 'Add some AmazingFeature')

پوش (Push) به برنچ (git push origin feature/AmazingFeature)

درخواست پول ریکوئست (Pull Request) بدهید

## 📜 لایسنس
این پروژه تحت لایسنس MIT منتشر شده است. می‌توانید آزادانه از آن استفاده کنید، تغییر دهید و توزیع کنید.

## 📞 ارتباط با من
گیت‌هاب: github.com/redyakhmac

ایمیل: (redyakhmac@gmail.com)

⭐️ اگر از این پروژه خوشتان می‌آید، فراموش نکنید که به آن ستاره دهید!
##



## 📖 Project Introduction
Personal Library Dashboard is a complete and professional web application for managing your personal book collection. You can add books, track reading status, view statistics, and enjoy a beautiful minimal dashboard.

## ✨ Key Features
✅ Full book management (add, edit, delete, search, filter)

📊 Interactive dashboard with charts (reading status, year distribution)

🌓 Dark/Light mode with one-click toggle

🌍 Bilingual support (Persian & English)

👤 User authentication & profile management with avatar upload

📱 Fully responsive design (mobile & tablet friendly)

🎨 Collapsible floating sidebar for better screen usage

📈 Star rating system & notes for each book

💾 Database export (coming soon)

## 🛠 Technologies Used
Technology	Purpose
Python 3.10+	Core programming language
Flask	Web framework (backend)
SQLAlchemy	ORM for database interaction
SQLite	Lightweight built-in database
Flask-Login	User authentication management
Bootstrap 5 (RTL)	Responsive UI design
Chart.js	Interactive charts
FontAwesome 6	Professional icons
CustomTkinter (optional)	Desktop GUI (future version)
## 📁 Project Structure
```bash
personal-library/
├── app.py                 # Main Flask application
├── models.py              # Database models (User, Book)
├── requirements.txt       # Project dependencies
├── .gitignore             # Ignored files for Git
├── static/
│   ├── style.css          # Custom styles
│   ├── script.js          # JavaScript code
│   └── profile_pics/      # User profile pictures
├── templates/
│   ├── base.html          # Base template (sidebar & header)
│   ├── dashboard.html     # Dashboard page
│   ├── books.html         # Books management page
│   ├── add_book.html      # Add book form
│   ├── edit_book.html     # Edit book form
│   ├── settings.html      # Profile settings page
│   └── login.html         # Login & register page
└── locales/
    ├── fa.json            # Persian translations
    └── en.json            # English translations
```
## 🚀 Installation & Run
Prerequisites
Python 3.10 or higher

Git (for cloning the project)

Installation steps (Windows, Linux, macOS)
bash
# 1. Clone the project from GitHub
git clone https://github.com/redyakhmac/personal-library.git
cd personal-library

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py
Then open your browser and go to http://127.0.0.1:5000.

## 📸 Screenshots
 ### Login Page
               https://via.placeholder.com/400x200?text=Login+Page
 ### Dashboard
	             https://via.placeholder.com/400x200?text=Dashboard


## 🎯 Key Code Features
Dynamic translation: The t() function in templates easily translates texts based on user language preference.

Dark/Light theme: Uses CSS variables and stores preference in user database.

Collapsible sidebar: Saves open/close state in database.

Interactive dashboard: Doughnut and bar charts using Chart.js.

## 🔧 Development & Contribution
If you have ideas or suggestions to improve the project, I'd love to hear them.

Fork the project

Create a new branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

## 📜 License
This project is licensed under the MIT License. You are free to use, modify, and distribute it.

## 📞 Contact Me
GitHub: github.com/redyakhmac

Email: (your email here)

⭐️ If you like this project, don't forget to give it a star on GitHub!

