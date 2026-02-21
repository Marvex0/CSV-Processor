# CSV Processing Automation Pipeline

A Python-based CSV data processing system that automatically applies multiple data transformations and validations on .CSV files.

---

# Features

1. Merge multiple CSV files from a folder
2. Append two CSV files without duplicate index issues
3. Split CSV files by row count
4. Split CSV files by column
5. Restructure CSV layout (transpose)
6. Automated testing using PyTest
7. Continuous Integration via GitHub Actions

---

# Project Purpose

This project was developed to practice:

* Python data processing with **pandas**
* Modular software design
* Automated testing workflows
* CI/CD fundamentals
* DevOps-style data pipelines

It simulates a small-scale automated data processing system similar to real-world ETL preprocessing tasks.

---

# Project Structure

```
csv-processor/
├─ .github/workflows/ci.yml   # CI pipeline
├─ functions/                 # Core CSV processing functions
├─ tests/                     # PyTest test cases
├─ input/                     # Source of CSV files for functions
├─ output/                    # Generated results from function
├─ main.py                    # Automation entry point
├─ requirements.txt           # Dependencies
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Marvex0/CSV-Processor
cd CSV-Processor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Place your CSV files inside the input/ folder, then run:

```bash
python main.py
```

The system will automatically:

1. Merge CSV files
2. Append selected CSV files
3. Split by row count
4. Split by column
5. Restructure layout

Processed files will appear in the **output/** folder.

---

# Running Tests

```bash
pytest
```

All functions are validated using automated unit tests.

---

# Continuous Integration

This project uses *GitHub Actions* to automatically:

* install dependencies
* run tests
* execute the CSV pipeline

on every push and pull request.

---

# Requirements

* Python 3.14
* pandas
* numpy
* pytest

---

This project is solely for educational purposes