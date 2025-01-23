# **Cricket Player Analysis - Data Engineering & Machine Learning Project** 🏏📊🚀

## **Project Overview**

This project implements a **complete end-to-end data pipeline** using **Apache Spark, PostgreSQL, Apache Airflow, and Machine Learning** to analyze **cricket player performance**. The pipeline includes **data extraction, transformation, storage, automation, machine learning model training, and visualization**.

---

## **Project Workflow**

1. **Extract Data** → Load CSV into **Pandas & PostgreSQL**.  
2. **Transform Data** → Clean & Process using **Apache Spark**.  
3. **Load Data** → Store transformed data into **PostgreSQL**.  
4. **Automate Workflow** → Use **Apache Airflow DAGs**.  
5. **Train ML Model** → Predict **batting averages** using **Linear Regression**.  
6. **Visualize Insights** → Scatter plots & histograms using **Matplotlib & Seaborn**.  

---

## **Prerequisites**

- **Python 3.x** installed on your system.  
- **Apache Spark** installed and configured.  
- **PostgreSQL** installed and running.  
- **Apache Airflow** set up in a virtual environment.  
- **Required Python Libraries**:  
  ```sh
  pip install pandas numpy psycopg2-binary jupyterlab scikit-learn matplotlib seaborn apache-airflow pyspark
