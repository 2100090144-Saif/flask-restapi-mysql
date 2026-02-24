🚀 Flask REST API with MySQL

A simple RESTful API built using **Flask** and **MySQL** that performs CRUD (Create, Read, Update, Delete) operations on student records.

This project demonstrates backend API development, database integration, and JSON-based request/response handling.

---

📌 Project Overview 

This REST API allows users to:

- ➕ Add a new student  
- 📄 Retrieve all students  
- 🔍 Retrieve a single student by ID  
- ✏️ Update student details  
- ❌ Delete a student  

The API communicates using JSON format and connects to a MySQL database.

---

🛠️ Technologies Used

- Python
- Flask
- MySQL
- flask-mysqldb
- Thunder Client / Postman (for testing)
- Git & GitHub

---

📂 Project Structure

flask-restapi-mysql/
│
├── app.py
├── README.md
└── requirements.txt (optional)



Step-1


🗄️ Database Setup

Step 1: 
Create Database

--SQL
CREATE DATABASE restapi_db;


Step 2: Use Database
USE restapi_db;

Step 3: Create Table in MySQL

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

⚙️ Configuration

Update your MySQL configuration inside app.py

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'restapi_db'

▶️ How to Run the Project

1️⃣ Install Dependencies
pip install flask flask-mysqldb

2️⃣ Run Application
python app.py

The server will start at:
http://127.0.0.1:5000

🔥 API Endpoints
📄 Get All Students
GET /students

🔍 Get Student by ID
GET /students/<id>

➕ Add Student
POST /students

JSON Body:
{
    "name": "abc",
    "email": "abc@example.com"
}


✏️ Update Student
PUT /students/<id>

🧪 API Testing
You can test the API using:

Thunder Client (VS Code)

Postman





























