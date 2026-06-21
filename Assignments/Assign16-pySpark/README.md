# Employee Data Processing using PySpark RDDs

## Objective

Perform employee data processing using PySpark RDDs.

## Dataset

**employees.csv** contains:

* id
* name
* department
* salary

## Operations Performed

### 1. Read CSV File

Read the employee dataset into a PySpark RDD.

### 2. Sort Employees by Salary

Sort all employees by salary in descending order and display the results on the console.

### 3. Department-wise Total Salary

Calculate the total salary paid in each department and display the department-wise totals.

### 4. Top 3 Highest Paid Employees

Identify the top three highest-paid employees.

### 5. Save Output

Save the top three highest-paid employees to a text file.

---

## Build Docker Image

```bash
docker build -t employee-rdd .
```

## Run Container

```bash
docker run --rm employee-rdd
```

---

## Expected Department Salary Totals

| Department | Total Salary |
| ---------- | ------------ |
| IT         | 170000       |
| HR         | 85000        |
| Finance    | 130000       |

---

## Expected Top 3 Highest Paid Employees

| ID | Name  | Department | Salary |
| -- | ----- | ---------- | ------ |
| 4  | Priya | Finance    | 70000  |
| 3  | Neha  | IT         | 65000  |
| 7  | Rohit | Finance    | 60000  |

---

## Output Location

```text
output/top3_employees.txt
```

---

## Technologies Used

* Python 3
* Apache Spark (PySpark)
* RDD API
* Docker

---

## Project Structure

```text
Assignment16-pySpark/
│
├── data/
│   └── employees.csv
│
├── output/
│   └── top3_employees.txt
│
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```
