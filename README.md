# 🌐 CoreXManzoid Flask Application  

## 📖 Overview  
**CoreXManzoid** is a Flask-based web application that provides user registration, login, and interaction features.  
Users can:  
✅ Sign up and confirm their email with OTP verification  
✅ Log in securely  
✅ Send questions/messages  
✅ View answers provided by the admin  

The **Admin** can verify users and respond to questions through a dedicated interface.  
Additionally, the app fetches and displays **team information** from an external API.  

---

## ✨ Features  

- 🔑 User sign-up with **email confirmation via OTP**  
- 🔒 Secure password hashing with **Werkzeug**  
- 👤 User login & logout with **Flask-Login**  
- 💬 Post questions/messages and view answers  
- 🛠️ **Admin interface** to verify users & answer questions  
- 📄 Dynamic **About Us** and **Team Member details** pages  
- 🎨 UI styled with **Flask-Bootstrap 5**  
- 🗄️ SQLite database managed with **SQLAlchemy ORM**  

---

## 🛠️ Technologies Used  

- 🐍 Python 3.x  
- ⚡ Flask  
- 🎨 Flask-Bootstrap 5  
- 🔑 Flask-Login  
- 📝 Flask-WTF + WTForms  
- 🗄️ SQLAlchemy ORM  
- 🔒 Werkzeug security  
- 💾 SQLite  
- 🌍 Requests (API integration)  

---

## 🚀 Setup and Installation  

1. **Clone the repository**  

   git clone <repository_url>  
   cd <repository_folder>  

2. **Create and activate a virtual environment**  

   python -m venv venv  
   # On Windows  
   venv\Scripts\activate  
   # On macOS/Linux  
   source venv/bin/activate  

3. **Install dependencies**  

   pip install -r requirements.txt  

   If `requirements.txt` is not available:  

   pip install Flask Flask-Bootstrap flask_sqlalchemy flask_login flask_wtf requests  

4. **Configure environment variables (optional)**  

   export FLASK_APP=main.py  
   export FLASK_ENV=development  
   export SECRET_KEY="your-secret-key"  

5. **Run the application**  

   flask run  

   Or directly:  

   python main.py  

6. **Access the app**  
   👉 Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.  

---

## 🧩 Important Details  

### 🔹 Database Models  
- **UserDB** → stores name, age, email, phone, hashed password, status  
- **UserComment** → stores questions, timestamps, answers, linked to users  

### 🔹 Authentication  
- Passwords hashed with `werkzeug.security.generate_password_hash`  
- Session handling with **Flask-Login**  
- First registered user (`id=1`) is the **Admin**  

### 🔹 Email & OTP  
- OTP sent via `second.py` (not included)  
- User must confirm OTP before completing signup  

### 🔹 Admin Features  
- Restricted routes with `@only_admin` decorator  
- Verify pending accounts  
- Answer user-submitted questions  

---

## 🖥️ Usage  

👤 **User Flow**  
- Sign Up → `/sign-up` (with OTP email confirmation)  
- Login → `/login`  
- Post Questions → User dashboard  

🛠️ **Admin Flow**  
- Verify Users → `/verification/Pending`  
- Answer Questions → `/Answer/<id>`  

---

## 🎨 Customization  

- 🔗 Update the `url` variable in **main.py** to change team data source  
- 🎨 Modify **styles.css** for custom UI design  
- 📝 Update templates in **templates/** for frontend customization  

---

## ⚠️ Notes  

- Email system requires `second.py` (not included)  
- Global variables used for signup → replace with **session or DB** in production  
- Ensure first user has `id=1` for admin privileges  
- Use proper DB migration tools when modifying models  

---

## 📜 License  

📝 Specify your project license here.  

---

## 📬 Contact  

💡 For questions or support, contact the **CoreXManzoid Development Team**.