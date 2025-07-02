# Titanic Data Cleaning Project

This project demonstrates basic data cleaning steps on the Titanic dataset using Python and Pandas.

## 📁 Project Structure

```
titanic_cleaning_project/
├── titanic_cleaning.py          # Python script for data cleaning
├── cleaned_titanic.csv          # Output: cleaned version of the dataset
├── data_cleaning_notes.md       # Description of cleaning logic
└── README.md                    # Project overview and instructions
```

## 🧹 Cleaning Steps Summary

- Filled missing values in `Age` using the median
- Filled missing values in `Embarked` using the mode (most common port)
- Converted `Sex` into numeric: male → 0, female → 1
- Dropped the following columns due to high nulls or irrelevance:
  - `Cabin`, `Ticket`, `Name`, `PassengerId`

## 🚀 How to Run

1. Make sure Python and pandas are installed:
   ```
   pip install pandas
   ```

2. Run the cleaning script:
   ```
   python titanic_cleaning.py
   ```

3. You will get the output file: `cleaned_titanic.csv`

## 📌 Dataset Source

Titanic dataset from [Data Science Dojo GitHub](https://github.com/datasciencedojo/datasets)

## 🧑‍💻 Author

This project was created as a data engineering training task.
