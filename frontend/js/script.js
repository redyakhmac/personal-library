// مدیریت تب‌های صفحه ورود/ثبت‌نامه
if (document.querySelector('.auth-tabs')) {
    const tabs = document.querySelectorAll('.auth-tab');
    const forms = document.querySelectorAll('.auth-form-content');
    
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const target = tab.dataset.tab;
            tabs.forEach(t => t.classList.remove('active'));
            forms.forEach(f => f.classList.remove('active'));
            tab.classList.add('active');
            document.getElementById(`${target}-form`).classList.add('active');
        });
    });
    
    // ثبت‌نام
    document.getElementById('register-btn')?.addEventListener('click', async () => {
        const full_name = document.getElementById('register-name').value;
        let phone = document.getElementById('register-phone').value;
        const email = document.getElementById('register-email').value;
        const password = document.getElementById('register-password').value;
        
        if (!full_name) {
            alert('لطفاً نام کامل خود را وارد کنید');
            return;
        }
        if (!phone || phone.length < 10) {
            alert('شماره موبایل معتبر وارد کنید');
            return;
        }
        if (!password || password.length < 4) {
            alert('رمز عبور حداقل ۴ کاراکتر');
            return;
        }
        
        const res = await fetch('/api/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ full_name, phone, email, password })
        });
        const data = await res.json();
        if (data.success) {
            localStorage.setItem('user', JSON.stringify(data.user));
            window.location.href = data.redirect;
        } else {
            alert(data.message);
        }
    });
    
    // ورود
    document.getElementById('login-btn')?.addEventListener('click', async () => {
        const identifier = document.getElementById('login-identifier').value;
        const password = document.getElementById('login-password').value;
        
        if (!identifier || !password) {
            alert('لطفاً نام کاربری و رمز عبور را وارد کنید');
            return;
        }
        
        const res = await fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ identifier, password })
        });
        const data = await res.json();
        if (data.success) {
            localStorage.setItem('user', JSON.stringify(data.user));
            window.location.href = data.redirect;
        } else {
            alert(data.message || 'نام کاربری یا رمز عبور اشتباه است');
        }
    });
}

// بارگذاری اطلاعات کاربر در صفحات داخلی
async function loadUserInfo() {
    const res = await fetch('/api/current-user');
    const data = await res.json();
    if (data.success) {
        localStorage.setItem('user', JSON.stringify(data.user));
        if (document.getElementById('user-name')) {
            document.getElementById('user-name').innerText = data.user.full_name || 'کاربر';
            document.getElementById('user-phone').innerText = data.user.phone || '';
        }
    } else {
        // اگر کاربر لاگین نبود، به صفحه لاگین برو
        if (window.location.pathname !== '/') {
            window.location.href = '/';
        }
    }
}

// اجرای بارگذاری اطلاعات در صفحات داخلی
if (document.getElementById('user-name')) {
    loadUserInfo();
}