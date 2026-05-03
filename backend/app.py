from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import re
import os

app = Flask(__name__, 
            template_folder='../frontend',
            static_folder='../frontend',
            static_url_path='')
app.config['SECRET_KEY'] = 'your-secret-key-123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# مدل کاربر
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(20), unique=True, nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    password = db.Column(db.String(200), nullable=False)
    profile_pic = db.Column(db.String(300), nullable=True)
    role = db.Column(db.String(20), default='user')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

# مدل کتاب
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100))
    year = db.Column(db.Integer)
    status = db.Column(db.String(20), default='to_read')
    rating = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# ایجاد جداول و کاربر پیش‌فرض
with app.app_context():
    db.create_all()
    
    admin = User.query.filter_by(role='admin').first()
    if not admin:
        admin = User(
            full_name='مدیر سیستم',
            phone='+989123456789',
            email='admin@library.com',
            password=generate_password_hash('admin'),
            role='admin',
            is_active=True
        )
        db.session.add(admin)
        db.session.commit()
        print('Admin user created - Email: admin@library.com, Phone: 09123456789, Password: admin')

# ==================== صفحات ====================
@app.route('/')
def login_register():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login_register'))
    user = User.query.get(session['user_id'])
    books = Book.query.filter_by(user_id=user.id).all()
    return render_template('dashboard.html', user=user, books=books)

@app.route('/books')
def books_page():
    if 'user_id' not in session:
        return redirect(url_for('login_register'))
    user = User.query.get(session['user_id'])
    books = Book.query.filter_by(user_id=user.id).all()
    return render_template('books.html', user=user, books=books)

@app.route('/users')
def users_page():
    if 'user_id' not in session:
        return redirect(url_for('login_register'))
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/statistics')
def statistics_page():
    if 'user_id' not in session:
        return redirect(url_for('login_register'))
    user = User.query.get(session['user_id'])
    books = Book.query.filter_by(user_id=user.id).all()
    return render_template('statistics.html', user=user, books=books)

@app.route('/settings')
def settings_page():
    if 'user_id' not in session:
        return redirect(url_for('login_register'))
    user = User.query.get(session['user_id'])
    return render_template('settings.html', user=user)

# ==================== API ====================
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    phone = data.get('phone')
    email = data.get('email')
    password = data.get('password')
    full_name = data.get('full_name', '')
    
    if phone:
        phone = re.sub(r'[^0-9]', '', phone)
        if len(phone) == 10:
            phone = '+98' + phone
        elif len(phone) == 11 and phone.startswith('0'):
            phone = '+98' + phone[1:]
        elif not phone.startswith('+'):
            phone = '+98' + phone
    
    if User.query.filter_by(phone=phone).first():
        return jsonify({'success': False, 'message': 'این شماره موبایل قبلاً ثبت شده است'})
    
    if email and User.query.filter_by(email=email).first():
        return jsonify({'success': False, 'message': 'این ایمیل قبلاً ثبت شده است'})
    
    hashed = generate_password_hash(password)
    user = User(phone=phone, email=email, password=hashed, full_name=full_name, role='user')
    db.session.add(user)
    db.session.commit()
    
    session['user_id'] = user.id
    return jsonify({'success': True, 'redirect': '/dashboard', 'user': {
        'id': user.id,
        'full_name': user.full_name,
        'phone': user.phone,
        'email': user.email,
        'role': user.role
    }})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    identifier = (data.get('identifier') or '').strip()
    password = data.get('password') or ''
    
    if not identifier or not password:
        return jsonify({'success': False, 'message': 'لطفاً نام کاربری و رمز عبور را وارد کنید'})

    phone_variants = [identifier]
    if identifier.startswith('0'):
        phone_variants.append('+98' + identifier[1:])
    if not identifier.startswith('+'):
        phone_variants.append('+98' + identifier)

    user = User.query.filter(
        (User.email == identifier) |
        (User.phone.in_(phone_variants))
    ).first()
    
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        return jsonify({'success': True, 'redirect': '/dashboard', 'user': {
            'id': user.id,
            'full_name': user.full_name,
            'phone': user.phone,
            'email': user.email,
            'role': user.role
        }})
    return jsonify({'success': False, 'message': 'نام کاربری یا رمز عبور اشتباه است'})

@app.route('/api/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login_register'))

@app.route('/api/current-user')
def current_user():
    if 'user_id' not in session:
        return jsonify({'success': False})
    user = User.query.get(session['user_id'])
    return jsonify({'success': True, 'user': {
        'id': user.id,
        'full_name': user.full_name,
        'phone': user.phone,
        'email': user.email,
        'role': user.role,
        'profile_pic': user.profile_pic
    }})

@app.route('/api/user-stats')
def user_stats():
    if 'user_id' not in session:
        return jsonify({'success': False})
    user_id = session['user_id']
    total = Book.query.filter_by(user_id=user_id).count()
    completed = Book.query.filter_by(user_id=user_id, status='completed').count()
    reading = Book.query.filter_by(user_id=user_id, status='reading').count()
    to_read = Book.query.filter_by(user_id=user_id, status='to_read').count()
    return jsonify({
        'total': total,
        'completed': completed,
        'reading': reading,
        'to_read': to_read
    })

@app.route('/api/books', methods=['POST'])
def add_book():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'})
    data = request.json
    book = Book(
        title=data['title'],
        author=data.get('author', ''),
        year=data.get('year'),
        status=data.get('status', 'to_read'),
        rating=int(data.get('rating', 0)),
        user_id=session['user_id']
    )
    db.session.add(book)
    db.session.commit()
    return jsonify({'success': True, 'message': 'کتاب با موفقیت اضافه شد'})

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if 'user_id' not in session:
        return jsonify({'success': False})
    book = Book.query.get(book_id)
    if book and book.user_id == session['user_id']:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'success': True})
    return jsonify({'success': False})

@app.route('/api/profile', methods=['POST'])
def update_profile():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not logged in'})
    user = User.query.get(session['user_id'])
    data = request.json
    if 'full_name' in data:
        user.full_name = data['full_name']
    if 'email' in data:
        user.email = data['email']
    db.session.commit()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)