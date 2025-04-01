# User Authentication System

This project is a **Django-based User Authentication System** that includes **registration and login functionality** for users.

## Features
✅ User Registration with email and password
✅ User Login with authentication
✅ Secure password hashing
✅ Django session management
✅ Responsive design for user-friendly experience

## Technologies Used
- **Django** (Backend framework)
- **SQLite** (Default Django database)
- **Bootstrap** (For styling)
- **HTML, CSS, JavaScript** (Frontend technologies)

## Installation & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### 2. Create a Virtual Environment
```bash
python -m venv myvenv
source myvenv/bin/activate  # For Mac/Linux
myvenv\Scripts\activate    # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

### 5. Run the Server
```bash
python manage.py runserver
```
Access the app at `http://127.0.0.1:8000/`

## Usage
- **Register:** Users can create an account by providing their email and password.
- **Login:** Users can log in using their credentials.
- **Logout:** Securely log out of the session.

## Project Structure
```
|-- myproject/
|   |-- myapp/
|   |   |-- templates/
|   |   |   |-- registration.html
|   |   |   |-- login.html
|   |   |-- views.py
|   |   |-- models.py
|   |   |-- urls.py
|-- manage.py
|-- requirements.txt
|-- README.md
```

## Future Enhancements
🚀 Add password reset functionality
🚀 Implement social login (Google, Facebook)
🚀 Improve UI with more responsive design

## License
This project is open-source and available under the **MIT License**.

---
💡 **Contributions are welcome!** Feel free to fork the repo and submit a pull request.

