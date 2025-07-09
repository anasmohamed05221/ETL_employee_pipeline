# 🛠️ Employee ETL Pipeline (CSV → Python → SQL Server)

This is a beginner-friendly ETL (Extract, Transform, Load) pipeline project built with **Python** and **SQL Server**. It extracts employee data from a `.csv` file, cleans and transforms it, loads it into a local SQL Server database, then performs actual **SQL queries** to demonstrate filtering and analysis skills.

---

## 📦 Features

- Extracts raw employee data from a CSV file
- Doubles all employee salaries
- Converts birthdates from `DD/MM/YYYY` to `YYYY-MM-DD`
- Sorts employees by salary and then name
- Loads the clean data into a SQL Server table (`employees`)
- Runs real SQL queries: `WHERE`, `ORDER BY`, `GROUP BY`, etc.

---

## 🧰 Tech Stack

| Layer     | Tool                     |
|-----------|--------------------------|
| Language  | Python 3.x               |
| Database  | Microsoft SQL Server     |
| Connector | pyodbc + ODBC Driver 17  |
| Input     | CSV File (`employees_data.csv`) |

---

## 🗃️ Project Structure

ETL_employee_pipeline/
│
├── main.py # The main Python script (ETL process + SQL queries)
├── employees_data.csv # Input CSV file with raw data
└── README.md # Project documentation

---

## 🧠 How It Works


🔹 1. Extract
read_csv_file() reads all employee records from the CSV file.

🔹 2. Transform
double_salary() doubles the salary.

convert_birthdates() formats the birth date to SQL-compatible format.

sort_data() sorts employees by salary, then name.

🔹 3. Load
load_to_sql_server():

Connects to SQL Server

Drops & recreates the employees table

Inserts all transformed records

🔹 4. Run SQL Queries
run_sql_queries():

Runs real SQL queries on the employees table

Displays filtered and grouped results in terminal


## 🧠 Sample SQL Queries Used

-- Get employees with salary over 30,000
SELECT name, salary FROM employees
WHERE salary > 30000
ORDER BY salary DESC;

-- Employees born after 1990
SELECT name, birthdate FROM employees
WHERE birthdate > '1990-01-01';

-- Count of employees by birth year
SELECT YEAR(birthdate) AS birth_year, COUNT(*) AS count
FROM employees
GROUP BY YEAR(birthdate)
ORDER BY birth_year;


## 📘 Example Output

🔎 Employees with salary > 30,000:
('Eman Ali', 36000.0)
('Omar Hassan', 36000.0)
('Nour Mahmoud', 36000.0)
...

📆 Employees born after 1990:
('Amal Omar', '1998-11-13')
('Aya Ahmed', '1998-11-20')
('Ali Samir', '1997-03-14')
('Fatma Omar', '1995-03-02')
('Ali Yassin', '1995-02-02')
...

📊 Count of employees per birth year:
(1984, 1)
(1985, 4)
(1986, 2)
(1987, 2)
(1988, 2)
(1989, 3)
(1990, 2)
(1991, 3)
(1992, 3)
(1993, 3)
(1994, 3)
(1995, 2)
(1997, 2)
(1998, 2)


## 💡 Learning Goals

✅ Practice real-world ETL using Python

✅ Understand CSV parsing and data transformation

✅ Connect Python to SQL Server using pyodbc

✅ Write and execute real SQL queries (SELECT, WHERE, GROUP BY)


## 🧪 Possible Future Improvements
 Use Pandas for data manipulation

 Export query results to CSV

 Use API requests
 

## 📄 License

This project is licensed under the MIT License — free for personal and commercial use.

🙋‍♂️ Author
Anas Mohamed
AASTMT Computer Science Student
