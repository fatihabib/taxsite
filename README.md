# Tax Automation Django Project

This is a Django web project for **Customer Service Week** (Tax Automation Department).  
It includes HTML, CSS, JavaScript, and Django as backend.

---

## 🚀 Quick Start (using this zip)
1. Unzip the project:
   ```bash
   unzip tax_automation_site_full_with_readme.zip
   cd tax_automation_site_full
   ```

2. Create & activate a virtual environment:
   - **macOS/Linux**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows (CMD)**
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```
   - **Windows (PowerShell)**
     ```powershell
     python -m venv venv
     venv\Scripts\Activate.ps1
     ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the server:
   ```bash
   python manage.py runserver
   ```

6. Open the site in your browser:  
   👉 http://127.0.0.1:8000/

---

## 📂 Project Structure
```
tax_automation_site_full/
├── manage.py
├── requirements.txt
├── taxsite/        # Django project settings
├── siteapp/        # Main app (views, urls, templates, static)
│   ├── templates/  # base.html, index.html
│   └── static/     # css, js, images
└── README.md
```

---

## 🖼️ Features
- **Hero Section**: Customer Service Week, Tax Automation Dept, background images
- **Structure Section**: 4 divisions, 15 departments
- **Events Section**: event cards with images
- **Responsive design** with DM Sans font

---

## 👩‍💻 Development Notes
- Replace placeholder images inside `siteapp/static/siteapp/images/`
- Add Django models to manage divisions/departments/events dynamically (optional)
- For production, set a real `SECRET_KEY` in `taxsite/settings.py` and configure `ALLOWED_HOSTS`.

---

Enjoy 🎉  
