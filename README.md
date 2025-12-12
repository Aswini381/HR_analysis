# 📊 HR Analytics Project using Python & Pandas

This project is a complete **HR Data Analysis System** built using Python and Pandas.  
It merges employee, salary, attendance, and project data to generate insights such as performance score, salary analysis, attendance summary, and department-wise statistics.

The final output of the project is a detailed file:



---

## 📁 **Project Overview**

This project performs:

- ✔ Data Cleaning  
- ✔ Data Merging  
- ✔ Salary Analysis  
- ✔ Attendance Analysis  
- ✔ Project Analysis  
- ✔ Performance Scoring  
- ✔ Exporting Final Report  

It simulates a **real-world HR department workflow** using Pandas.

---

## 📂 **Dataset Information**

The project uses the following CSV files:

| File Name        | Description |
|------------------|-------------|
| `employees.csv`  | Employee details (name, department, join date) |
| `salary.csv`     | Base salary, bonus, and deductions |
| `attendance.csv` | Daily attendance with work hours |
| `projects.csv`   | Project details, hours, and completion status |

---

## 🛠️ **Technologies Used**

- **Python**
- **Pandas**
- **Data Cleaning**
- **Data Aggregation**
- **CSV File Processing**

---

## 🚀 **Features Implemented**

### **1️⃣ Data Cleaning**
- Converted dates to datetime format  
- Checked missing values  
- Filled missing work hours with `0`  

### **2️⃣ Merging Multiple Data Sources**
- Employee + Salary  
- Employee + Salary + Projects  
- Attendance + Average Work Hours  

### **3️⃣ Salary Analysis**
- Calculated final salary:

  - Found **Top 3 highest salaries**
- Calculated **salary spent per department**

### **4️⃣ Attendance Analysis**
- Created an attendance summary table  
- Computed average work hours per employee  

### **5️⃣ Project Analysis**
- Total hours spent per project  
- List of pending projects  

### **6️⃣ Performance Score Formula**

Performance score is calculated using weighted features:


### **7️⃣ Final Output**
A complete employee performance table exported as:


---

## ▶️ **How to Run the Project**

1. Download all CSV files:  
   - employees.csv  
   - salary.csv  
   - attendance.csv  
   - projects.csv  

2. Update their path inside the Python script.

3. Run the Python file:

```bash
python hr_analysis.py
```



## Code

```
import pandas as pd

employees=pd.read_csv('C:/Users/Apple/Documents/employees.csv')
salary=pd.read_csv('C:/Users/Apple/Documents/salary.csv')
attendance=pd.read_csv('C:/Users/Apple/Documents/attendance.csv')
projects= pd.read_csv('C:/Users/Apple/Documents/projects.csv')

employees['join_date']=pd.to_datetime(employees['join_date'])
attendance['date']=pd.to_datetime(attendance['date'])

print("\nEmployee Information :")
print(employees.info)

print("\n Attendance missing values : ")
print(attendance.isna().sum())

attendance['work_hours']=attendance['work_hours'].fillna(0)

emp_salary=employees.merge(salary, on='emp_id', how='left')
emp_salary_projects=emp_salary.merge(projects,on='emp_id', how='left')

emp_salary_projects['final_salary']=(emp_salary_projects['base_salary']+
                                     emp_salary_projects['bonus']-
                                     emp_salary_projects['deductions'])

top_salary=emp_salary_projects.nlargest(3, 'final_salary')
print("\n Top 3 Salary")
print(top_salary[['name','final_salary']])

department_salary=emp_salary_projects.groupby('department')['final_salary'].sum()
print("\n Salary spent per department", department_salary)

attendance_summary=attendance.groupby(['emp_id','status']).size().unstack(fill_value=0)
print("\n Attendance summary:\n",attendance_summary)

avg_hours=attendance.groupby('emp_id')['work_hours'].mean().reset_index()
print("\n Average hours per employee:\n",avg_hours)

project_hours_sum=projects.groupby('project_name')['project_hours'].sum()
print("\n Project hours :\n",project_hours_sum)

pending = projects[projects['completion_status'] == 'Pending']
print("\nPending Projects:\n", pending)

final = emp_salary_projects.merge(avg_hours, on='emp_id', how='left')

final['performance_score'] = (
    (final['work_hours'] / final['work_hours'].max()) * 40 +
    (final['final_salary'] / final['final_salary'].max()) * 30 +
    (final['project_hours'] / final['project_hours'].max()) * 30
)

print("\nFinal Employee Performance Table:\n")
print(final[['name','department','performance_score']])

final.to_csv("Final_HR_Report.csv", index=False)
```


## 👩‍💻 Author

Aswini Kathirvel

Python Developer
