# my-learning-journey 🚀
My personal learning notebook to grow daily through small and consistent efforts.

Hi 👋  
My name is Tanishq.

I am a beginner and I am learning step by step.
This GitHub is my daily learning notebook.

### Why I made this
- To learn slowly
- To be consistent
- To improve myself every day

### Promise to myself
I will try to update this daily, even if it is small.

notes/dbms.md

📘 DBMS (Database Management System)

1️⃣ Introduction

DBMS stands for Database Management System.

It is software that is used to store, manage, and organize data in a structured way.

A DBMS allows users to:

Store data

Retrieve data

Update data

Delete data

Secure data


Example: College student record system.

2️⃣ Why DBMS is Needed

Without DBMS:

Data becomes messy

Duplicate data increases

Security is weak

Searching data is slow


With DBMS:

Data is organized

Easy to search

Secure

Accurate

3️⃣ Basic Terms

Data → Raw facts (Name, Age)

Information → Processed data

Table → Collection of rows and columns

Field → Column in a table

Record → Row in a table

Primary Key → Unique value to identify each record


Example:

Roll No	Name 	Age
107  	Rohit   21
Here, Roll No is the Primary Key.

4️⃣ Functions of DBMS

1. Data Storage

2. Data Retrieval

3. Data Update

4. Data Deletion

5. Data Security

6. Backup and Recovery

5️⃣ Types of DBMS

1. Hierarchical DBMS


2. Network DBMS


3. Relational DBMS (Most Important)

Relational DBMS stores data in tables and uses SQL.


6️⃣ Advantages of DBMS

Reduces data redundancy

Improves security

Maintains data consistency

Easy data access

Data backup available

7️⃣ Disadvantages of DBMS

Costly

Complex to manage

Requires trained users

8️⃣ Conclusion

DBMS is an important software system that helps in managing large amounts of data efficiently and securely.

## 9️⃣ DBMS Architecture

DBMS Architecture explains how data is stored and accessed.

### 1-Tier Architecture
- Database and user are on the same system.
- Mostly used for learning and small applications.

### 2-Tier Architecture
- Client directly communicates with database.
- Used in small client-server applications.

### 3-Tier Architecture
- Client → Application Server → Database
- Most secure and widely used.
- Example: Banking and web applications.
## Day 4:
- Learned DBMS architecture.
- Understood 1-tier, 2-tier, and 3-tier systems.

## 10️⃣ Normalization

**Normalization** = Organizing tables in DBMS to **remove redundancy*(duplicate data) and **avoid errors**.

### 1️⃣ First Normal Form (1NF)

* Each column must have atomic values(no lists in a cell)
* Each row must be unique

Example:

| Roll No | Name  | Subjects      |
| ------- | ----- | ------------- |
| 101     | Rahul | Math, Science |

✅ 1NF fixes it:

| Roll No | Name  | Subject |
| ------- | ----- | ------- |
| 101     | Rahul | Math    |
| 101     | Rahul | Science |

### 2️⃣ Second Normal Form (2NF)

* 1NF + No partial dependency
* Every column depends on whole primary key

### 3️⃣ Third Normal Form (3NF)

* 2NF + No transitive dependency
* Columns depend only on primary key, not on other columns

### Day 5:

* Learned basics of Normalization
* Understood 1NF, 2NF, 3NF with example

11️⃣ ER Diagram (Entity Relationship Diagram)

An **ER Diagram** is a visual representation of data and the relationship between data in a database.

It helps in **database design** before creating tables.

 🔹 Entity

An **Entity** is a real-world object.

Examples:

* Student
* Teacher
* Course

Entity is represented using a **Rectangle**.
 🔹 Attribute

An **Attribute** describes an entity.

Examples:

* Student Name
* Roll Number
* Age

Attribute is represented using an **Oval**.


 🔹 Primary Key

A **Primary Key** uniquely identifies each record.

Example:

* Roll Number (for Student)

Primary key is underlined in ER Diagram.

🔹 Relationship

A **Relationship** shows how two entities are connected.

Example:

* Student **enrolls in** Course

Relationship is represented using a **Diamond**.
🔹 Types of Relationships
* One to One (1:1)
* One to Many (1:M)
* Many to Many (M:M)

Example:

* One teacher teaches many students (1:M)
  
 🔹 Advantages of ER Diagram
* Easy to understand database structure
* Helps in proper database design
* Reduces errors before implementation
## Day 6:

* Learned ER Diagram concepts
* Understood entity, attribute, and relationship
* Learned importance of ER Diagram in DBMS

## 12️⃣ Keys in DBMS

A **Key** is used to identify records uniquely in a table.

Keys help to:

* Avoid duplicate data
* Maintain data accuracy
* Create relationships between tables

### 🔑 Primary Key

* Uniquely identifies each record
* Cannot be NULL
* Only one primary key in a table

Example:

* Roll Number in Student table

### 🔑 Foreign Key

* A key used to link two tables
* Refers to the primary key of another table

Example:

* Student table has Course ID as foreign key

### 🔑 Candidate Key

* All possible keys that can uniquely identify a record
* One candidate key becomes the primary key

Example:

* Roll No, Email ID

### 🔑 Super Key

* A set of one or more attributes that identify records uniquely

Example:

* (Roll No + Name)

### 🔑 Alternate Key

* Candidate keys not selected as primary key

Example:

* Email ID (if Roll No is primary key)

### 🔑 Composite Key

* A key made of more than one attribute

Example:

* (Student ID + Subject ID)

### 🔑 Difference: Primary Key vs Foreign Key

| Primary Key    | Foreign Key      |
| -------------- | ---------------- |
| Unique         | Not unique       |
| Cannot be NULL | Can be NULL      |
| One per table  | Multiple allowed |

## Day 7:

* Learned different types of keys in DBMS
* Understood how tables are connected using keys

