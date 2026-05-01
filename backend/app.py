from flask import Flask ,request,jsonify 
from flask_cors import CORS  # برای ارتباط با فرانت‌اند (مهم)

app = Flask(__name__)
CORS(app)  # اجازه می‌دهد فرانت‌اند از هر جایی به این سرور متصل شود

# داده‌های کاربران در حافظه (برای تست)
# در پروژه واقعی باید از دیتابیس مانند SQLite یا PostgreSQL استفاده شود
users_db = [
    {
        "id": 1,
        "username": "admin",
        "password": "admin",  # در پروژه واقعی باید هش شود
        "email": "admin@library.com",
        "display_name": "مدیر سیستم"
    }
]
current_user_id_counter = 2  # برای تولید ID جدید

# ==========================================
# ۱. مسیر ثبت‌نام (Register)
# ==========================================
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # دریافت اطلاعات از فرم
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    display_name = data.get('display_name', username)  # اگر نمایشی نداد، نام کاربری را بگذار
    
    # اعتبارسنجی ساده
    if not username or not password:
        return jsonify({"success": False, "message": "نام کاربری و رمز عبور الزامی است"}), 400
    
    # بررسی تکراری نبودن نام کاربری
    for user in users_db:
        if user['username'] == username:
            return jsonify({"success": False, "message": "این نام کاربری قبلاً استفاده شده است"}), 400
    
    # ایجاد کاربر جدید
    global current_user_id_counter
    new_user = {
        "id": current_user_id_counter,
        "username": username,
        "password": password,
        "email": email,
        "display_name": display_name
    }
    users_db.append(new_user)
    current_user_id_counter += 1
    
    return jsonify({"success": True, "message": "ثبت‌نام با موفقیت انجام شد", "user": {
        "id": new_user["id"],
        "username": new_user["username"],
        "display_name": new_user["display_name"]
    }}), 201

# ==========================================
# ۲. مسیر ورود (Login)
# ==========================================
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')
    
    # جستجوی کاربر
    for user in users_db:
        if user['username'] == username and user['password'] == password:
            return jsonify({"success": True, "message": "ورود موفق", "user": {
                "id": user["id"],
                "username": user["username"],
                "display_name": user["display_name"],
                "email": user.get("email", ""),
                "role": "admin" if user["username"] == "admin" else "user"
            }}), 200
    
    return jsonify({"success": False, "message": "نام کاربری یا رمز عبور اشتباه است"}), 401

# ==========================================
# ۳. راه‌اندازی سرور
# ==========================================
if __name__ == '__main__':
    print("سرور Flask در حال اجرا است...")
    print("آدرس: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)