## 0x0F. Python - Object-relational mapping
Tags:
- Python
- OOP
- SQL
- MySQL
- ORM
- SQLAlchemy

Here's a well-structured README based on the provided content:

---

# Python MySQL Integration

## General

This guide covers the fundamentals of integrating Python with MySQL, showcasing the power of Python programming and its ability to handle database operations efficiently.

## Why Python Programming is Awesome

Python is a versatile and powerful programming language that is easy to learn and use. Its readability and simplicity make it a favorite among developers for a wide range of applications, from web development to data science and automation. Python's extensive standard library and vast ecosystem of third-party packages enable rapid development and integration with other technologies, such as MySQL databases.

## How to Connect to a MySQL Database from a Python Script

Connecting to a MySQL database from a Python script is straightforward with the help of libraries such as `mysql-connector-python` or `PyMySQL`. Below is a basic example using `mysql-connector-python`:

```python
import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
	host="localhost",
        user="yourusername",
	password="yourpassword",
	database="yourdatabase"
)

# Create a cursor object
cursor = conn.cursor()

# Your database operations go here

# Close the connection
conn.close()
```

## How to SELECT Rows in a MySQL Table from a Python Script

Selecting rows from a MySQL table can be done using the `SELECT` SQL statement. Here's an example:

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

cursor = conn.cursor()

# Execute a SELECT statement
cursor.execute("SELECT * FROM yourtable")

# Fetch all the rows
rows = cursor.fetchall()

for row in rows:
	print(row)
conn.close()
```

## How to INSERT Rows in a MySQL Table from a Python Script

Inserting rows into a MySQL table is done using the `INSERT` SQL statement. Below is an example:

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

cursor = conn.cursor()

# Execute an INSERT statement
sql = "INSERT INTO yourtable (column1, column2) VALUES (%s, %s)"
values = ("value1", "value2")
cursor.execute(sql, values)

# Commit the transaction
conn.commit()

print(cursor.rowcount, "record inserted.")

conn.close()
```

## What ORM Means

ORM stands for Object-Relational Mapping. It is a programming technique that allows developers to interact with a database using the object-oriented paradigm of their programming language, rather than writing raw SQL queries. ORMs map database tables to classes and rows to objects, making database operations more intuitive and reducing boilerplate code.

## How to Map a Python Class to a MySQL Table

Using an ORM like SQLAlchemy, you can map a Python class to a MySQL table. Here's an example:

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class YourTable(Base):
    __tablename__ = 'yourtable'
    id = Column(Integer, primary_key=True)
    column1 = Column(String)
    column2 = Column(String)

engine = create_engine('mysql+mysqlconnector://user:password@localhost/yourdatabase')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Your ORM operations go here

session.close()
```

## How to Create a Python Virtual Environment

Creating a virtual environment in Python is a best practice to manage dependencies and avoid conflicts between projects. Here’s how to create one:

1. **Install virtualenv** (if not already installed):
    ```bash
        pip install virtualenv
    ```

 2. **Create a virtual environment**:
    ```bash
    	virtualenv venv
    ```

3. **Activate the virtual environment**:
	- On Windows:
   		```bash
	     		venv\Scripts\activate
		```
	- On Unix or MacOS:
		```bash
			source venv/bin/activate
		```

4. **Deactivate the virtual environment**:
	```bash
		deactivate
	```

By following this guide, you'll be well on your way to leveraging the power of Python and MySQL together for your database-driven applications.
