# PySpark Sales Analysis

## Objective

Perform sales analysis using the PySpark DataFrame API.

## Dataset

**sales.csv** contains:

* product_id
* product_name
* category
* sales

## Operations Performed

### 1. Read CSV File

Read the sales dataset into a PySpark DataFrame.

### 2. Sort Products by Sales

Sort all products by sales in descending order and display the results on the console.

### 3. Top 3 Products by Sales

Display the top three products with the highest sales values.

### 4. Filter High Sales Products

Filter products with sales greater than **80,000**.

### 5. Save Output

Save the filtered products as a CSV file.

---

## Build Docker Image

```bash
docker build -t sales-analysis .
```

## Run Container

```bash
docker run --rm sales-analysis
```

---

## Expected Top 3 Products

| Product | Category    | Sales  |
| ------- | ----------- | ------ |
| Laptop  | Electronics | 150000 |
| TV      | Electronics | 120000 |
| Mobile  | Electronics | 95000  |

---

## Expected High Sales Products

| Product | Sales  |
| ------- | ------ |
| Laptop  | 150000 |
| TV      | 120000 |
| Mobile  | 95000  |
| Bed     | 90000  |

---

## Output Location

```text
output/high_sales_products/
```

---

## Technologies Used

* Python 3
* Apache Spark (PySpark)
* DataFrame API
* Docker

---

## Project Structure

```text
Assignment17-PySpark/
│
├── data/
│   └── sales.csv
│
├── output/
│   └── high_sales_products/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Dataset

```csv
product_id,product_name,category,sales
101,Laptop,Electronics,150000
102,Mobile,Electronics,95000
103,TV,Electronics,120000
104,Chair,Furniture,30000
105,Table,Furniture,45000
106,Sofa,Furniture,80000
107,Headphones,Electronics,25000
108,Bed,Furniture,90000
```
