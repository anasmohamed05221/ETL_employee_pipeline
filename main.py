import csv  # For reading CSV files
import pyodbc  # For connecting to SQL Server
from datetime import datetime  # For converting birthdate strings to DATE format

# Connect to SQL Server
def connect_to_sql_server():
    # Establish a connection to the local SQL Server using Windows Authentication
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=ANASASUSTUF\\SQLEXPRESS;'  # Replace with your server name
        'DATABASE=EmployeePipelineDB;'     # Database where the table will be stored
        'Trusted_Connection=yes;'          # Use your Windows login credentials
    )
    return conn  # Return the connection object

# Read CSV File
def read_csv_file(file_name):
    # Open the CSV file and read its contents into a list of rows
    with open(file_name) as f:
         return list(csv.reader(f))  # Each row is a list of values

# Double Each Employee's Salary
def double_salary(data_list):
    # Loop through each employee and double their salary
    for line in data_list:
        # Remove the comma from salary string (e.g., '12,000.00') and convert to float
        line[-1] = float((line[-1].replace(",", ""))) * 2

# Convert Birthdate Format
def convert_birthdates(data_list):
    # Convert birthdate from 'DD/MM/YYYY' format to 'YYYY-MM-DD' for SQL DATE
    for row in data_list:
        try:
            date_obj = datetime.strptime(row[2], "%d/%m/%Y")  # Convert string to datetime
            row[2] = date_obj.strftime("%Y-%m-%d")  # Format datetime back to string
        except ValueError:
            print(f"Could not parse date: {row[2]}")  # Log if date parsing fails

# Sort Employees
def sort_data(data_list):
    # Sort employees first by salary (ascending), then by name (alphabetical)
    return sorted(data_list, key=lambda x: (x[-1], x[0]))

# Load Data into SQL Server
def load_to_sql_server(data_list):
    conn = connect_to_sql_server()  # Connect to SQL Server
    cur = conn.cursor()  # Create a cursor object to execute SQL

    # Drop the existing employees table if it exists (clean slate)
    cur.execute("IF OBJECT_ID('employees', 'U') IS NOT NULL DROP TABLE employees")

    # Create a fresh employees table with proper types
    cur.execute("""
        CREATE TABLE employees (
            name NVARCHAR(100),
            phone NVARCHAR(20),
            birthdate DATE,
            salary FLOAT
        )
    """)

    # Insert each row into the employees table using placeholders
    for row in data_list:
        cur.execute("INSERT INTO employees (name, phone, birthdate, salary) VALUES (?, ?, ?, ?)", row)

    # Save changes and close connection
    conn.commit()
    conn.close()
    print("Data loaded into SQL Server successfully.")

# Run some sql queries
def run_sql_queries():
    conn = connect_to_sql_server()
    cur = conn.cursor()

    print("\nEmployees with salary > 30,000:")
    cur.execute("SELECT name, salary FROM employees WHERE salary > 30000 ORDER BY salary DESC")
    for row in cur.fetchall():
        print(row)

    print("\nEmployees born after 1990:")
    cur.execute("SELECT name, birthdate FROM employees WHERE birthdate > '1990-01-01'")
    for row in cur.fetchall():
        print(row)

    print("\nCount of employees per birth year:")
    cur.execute("""
        SELECT YEAR(birthdate) AS birth_year, COUNT(*) AS count
        FROM employees
        GROUP BY YEAR(birthdate)
        ORDER BY birth_year
    """)
    for row in cur.fetchall():
        print(row)

    conn.close()


def main():
    # Step 1: Read raw CSV data
    data = read_csv_file("employees_data.csv")

    # Step 2: Transform the data
    double_salary(data)         # Multiply salary by 2
    convert_birthdates(data)    # Convert birthdate format

    # Step 3: Sort the cleaned data
    sorted_employees = sort_data(data)

    # Optional: Print for verification
    for row in sorted_employees:
        print(row)

    # Step 4: Load the final data into SQL Server
    load_to_sql_server(sorted_employees)

    # Step 5: undergo desired queries
    run_sql_queries()

if __name__ == "__main__":
    main()