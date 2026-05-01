document.addEventListener('DOMContentLoaded', function() {
    // ==========================================
    // ۱. سوئیچ بین فرم لاگین و ثبت‌نام
    // ==========================================
    const loginTab = document.getElementById('loginTab');
    const registerTab = document.getElementById('registerTab');
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const loginMessage = document.getElementById('loginMessage');
    const registerMessage = document.getElementById('registerMessage');

    loginTab.addEventListener('click', function() {
        loginTab.classList.add('active');
        registerTab.classList.remove('active');
        loginForm.style.display = 'block';
        registerForm.style.display = 'none';
        // پنهان کردن پیام‌ها
        loginMessage.className = 'auth-message';
        loginMessage.style.display = 'none';
        registerMessage.className = 'auth-message';
        registerMessage.style.display = 'none';
    });

    registerTab.addEventListener('click', function() {
        registerTab.classList.add('active');
        loginTab.classList.remove('active');
        registerForm.style.display = 'block';
        loginForm.style.display = 'none';
        loginMessage.className = 'auth-message';
        loginMessage.style.display = 'none';
        registerMessage.className = 'auth-message';
        registerMessage.style.display = 'none';
    });

    // ==========================================
    // ۲. تابع نمایش پیام
    // ==========================================
    function showMessage(element, message, type) {
        element.textContent = message;
        element.className = 'auth-message ' + type;
        element.style.display = 'block';
    }

    // ==========================================
    // ۳. فرم لاگین
    // ==========================================
    loginForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        const username = document.getElementById('loginUsername').value.trim();
        const password = document.getElementById('loginPassword').value.trim();

        if (!username || !password) {
            showMessage(loginMessage, 'لطفاً نام کاربری و رمز عبور را وارد کنید', 'error');
            return;
        }

        try {
            const response = await fetch('http://127.0.0.1:5000/api/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });

            const data = await response.json();

            if (data.success) {
                showMessage(loginMessage, 'ورود موفق! در حال انتقال...', 'success');
                // ذخیره اطلاعات کاربر در localStorage
                localStorage.setItem('currentUser', JSON.stringify(data.user));
                // هدایت به داشبورد (در پروژه واقعی به dashboard.html بروید)
                setTimeout(() => {
                    alert('شما با موفقیت وارد شدید. (به داشبورد هدایت می‌شوید)');
                    // window.location.href = 'dashboard.html';
                }, 1000);
            } else {
                showMessage(loginMessage, data.message || 'خطا در ورود', 'error');
            }
        } catch (error) {
            showMessage(loginMessage, 'مشکل در ارتباط با سرور. لطفاً مطمئن شوید بک‌اند Flask روشن است.', 'error');
            console.error(error);
        }
    });

    // ==========================================
    // ۴. فرم ثبت‌نام
    // ==========================================
    registerForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        const username = document.getElementById('regUsername').value.trim();
        const password = document.getElementById('regPassword').value.trim();
        const email = document.getElementById('regEmail').value.trim();
        const displayName = document.getElementById('regDisplayName').value.trim();

        // اعتبارسنجی ساده
        if (!username || !password) {
            showMessage(registerMessage, 'نام کاربری و رمز عبور الزامی است', 'error');
            return;
        }
        if (username.length < 3) {
            showMessage(registerMessage, 'نام کاربری حداقل ۳ کاراکتر باید باشد', 'error');
            return;
        }
        if (password.length < 4) {
            showMessage(registerMessage, 'رمز عبور حداقل ۴ کاراکتر باید باشد', 'error');
            return;
        }

        try {
            const response = await fetch('http://127.0.0.1:5000/api/register', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password, email, display_name: displayName })
            });

            const data = await response.json();

            if (data.success) {
                showMessage(registerMessage, 'ثبت‌نام با موفقیت انجام شد! اکنون می‌توانید وارد شوید.', 'success');
                // پاک کردن فرم
                document.getElementById('regUsername').value = '';
                document.getElementById('regPassword').value = '';
                document.getElementById('regEmail').value = '';
                document.getElementById('regDisplayName').value = '';
                // پس از ۲ ثانیه به لاگین بروید
                setTimeout(() => {
                    loginTab.click();
                }, 2000);
            } else {
                showMessage(registerMessage, data.message || 'خطا در ثبت‌نام', 'error');
            }
        } catch (error) {
            showMessage(registerMessage, 'مشکل در ارتباط با سرور. لطفاً مطمئن شوید بک‌اند Flask روشن است.', 'error');
            console.error(error);
        }
    });
});