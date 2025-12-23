# CSV to MySQL ETL Pipeline (Data Engineering Project)

## 📌 Project Overview
This project implements an **end-to-end ETL (Extract, Transform, Load) pipeline** that ingests a CSV dataset, applies data transformations and validations using Python, and loads the processed data into a MySQL database for analytical querying.

The goal of this project is to demonstrate **core Data Engineering fundamentals** such as schema enforcement, data validation, clean pipeline design, and reliable database loading.

---

## 🏗️ Architecture

```
CSV File
   ↓
Extract (pandas)
   ↓
Transform (schema enforcement, validation)
   ↓
Processed CSV
   ↓
Load (MySQL)
```

---

## 🛠️ Tech Stack
- Python
- Pandas
- MySQL
- mysql-connector-python
- SQL

---

## 📂 Project Structure

```
DE_Project/
│
├── data/
│   ├── raw/
│   │   └── Raw_Superstore.csv
│   └── processed/
│       └── clean_superstore.csv
│
├── etl_pipeline/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── db/
│   └── mysql_connection.py
│
├── dev/
│   └── config.example.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 📥 Extract Step
- Reads raw CSV using pandas
- Validates file accessibility
- Loads data into a DataFrame

---

## 🔄 Transform Step
- Standardizes column names to `snake_case`
- Converts data types (dates, numeric fields)
- Adds derived column: `total_sales`
- Performs data validation checks
- Saves cleaned data to processed directory

---

## 🗄️ Database Design
- Database: `de_project`
- Table: `sales`
- Primary Key: `row_id` (chosen because `order_id` is not unique)
- Uses appropriate SQL data types

---

## 📤 Load Step
- Converts NaN values to SQL NULL
- Uses parameterized SQL queries
- Bulk inserts using `executemany()`
- Uses `INSERT IGNORE` to ensure idempotent loads

---

## ⚙️ Configuration

This project uses a configuration file for paths and database credentials.

### Steps:
1. Copy the example config file:
```bash
cp dev/config.example.py dev/config.py
```

2. Update the following values in `config.py`:
- `local_directory`
- MySQL credentials (`host`, `user`, `password`, `database`)

> ⚠️ `config.py` is intentionally ignored in `.gitignore` to avoid exposing credentials.

---

### Data Quality Enhancements
- Handled missing and inconsistent values in retail dataset
- Applied validation rules and separated rejected records
- Enhanced transformation logic for messy real-world data


## ▶️ How to Run

1. Create the MySQL database and `sales` table
2. Update credentials in `dev/config.py`
3. Run the pipeline:
```bash
python main.py
```

---

## 📈 Key Learnings
- End-to-end ETL pipeline design
- Schema enforcement before database load
- Data validation and defensive programming
- Idempotent database loading
- Clean project structure and configuration management

---

## 🚀 Future Enhancements
- Add logging and error handling
- Implement incremental loads
- Convert pipeline to PySpark
- Introduce Airflow for orchestration
