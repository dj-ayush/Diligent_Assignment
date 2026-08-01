# 💰 Smart Expense Tracker API

![Django](https://img.shields.io/badge/Django-4.2.7-092E20?style=flat&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST_Framework-3.14.0-red?style=flat)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat&logo=sqlite&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-API_Testing-FF6C37?style=flat&logo=postman&logoColor=white)

A REST API built using **Django REST Framework** to manage personal expenses. It supports creating, viewing, filtering, calculating totals, and deleting expenses.

---

## ✨ Features

- ➕ Add Expense
- 📄 View All Expenses
- 📂 Filter by Category
- 📊 Calculate Total Expenses
- 🗑️ Delete Expense
- ✅ Input Validation
- 🧪 Automated Tests

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Postman

---

## 📁 Project Structure

```text
Diligent_Assignment/
├── README.md
├── AI_NOTES.md
├── requirements.txt
├── Expense_Tracker_API.postman_collection.json
├── Output_Images/
├── src/
└── tests/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/dj-ayush/Diligent_Assignment.git
cd Diligent_Assignment
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Server

```bash
cd src
python manage.py migrate
python manage.py runserver
```

Server:

```text
http://127.0.0.1:8000/
```

---

## 🧪 Run Tests

```bash
cd src
python manage.py test
```

---

## 📬 API Testing (Recommended)

For the easiest evaluation, use the included **Postman Collection**.

Import the following file into Postman:

```text
Expense_Tracker_API.postman_collection.json
```

Run the requests in the following order:

```http
POST    /api/expenses/
GET     /api/expenses/
GET     /api/expenses/?category=Food
GET     /api/expenses/total/
GET     /api/expenses/total/?category=Food
DELETE  /api/expenses/<id>/
```

---

## 📸 Sample Output

### ➕ Create Expense

![Create Expense](Output_Images/create-expense.png)

---

### 📄 View All Expenses

![View All Expenses](Output_Images/get-expenses.png)

---

### 📂 Filter by Category

![Filter by Category](Output_Images/filter-category.png)

---

### 📊 Total Expenses

![Total Expenses](Output_Images/total-expenses.png)

---

### 📊 Total Expenses by Category

![Category Total](Output_Images/category-total-expenses.png)

---

### 🗑️ Delete Expense

![Delete Expense](Output_Images/delete-expense.png)

---

## ✅ Reviewer Notes

For a quick evaluation:

- Install the project using the commands above.
- Run the Django development server.
- Import the provided **Postman Collection**.
- Execute the API requests.
- Compare the responses with the screenshots above.

All required assignment features have been implemented, manually tested, and covered with automated tests.
