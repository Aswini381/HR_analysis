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


# Merge salary with employees
emp_salary=employees.merge(salary, on='emp_id', how='left')
emp_salary_projects=emp_salary.merge(projects,on='emp_id', how='left')

#salary analysis
emp_salary_projects['final_salary']=(emp_salary_projects['base_salary']+emp_salary_projects['bonus']-emp_salary_projects['deductions'])

# TO get top 3 salary
top_salary=emp_salary_projects.nlargest(3, 'final_salary')
print("\n Top 3 Salary")
print(top_salary[['name','final_salary']])

#To get the total of each department
department_salary=emp_salary_projects.groupby('department')['final_salary'].sum()
print("\n Salary spent per department",department_salary)

#attendance analysis
attendance_summary=attendance.groupby(['emp_id','status']).size().unstack(fill_value=0)
print("\n Attendance summary:\n",attendance_summary)

avg_hours=attendance.groupby('emp_id')['work_hours'].mean().reset_index()
print("\n Average hours per employee:\n",avg_hours)

# project analysis
project_hours_sum=projects.groupby('project_name')['project_hours'].sum()
print("\n Project hours :\n",project_hours_sum)

pending = projects[projects['completion_status'] == 'Pending']
print("\nPending Projects:\n", pending)

# Merge avg hours with employee salary+project table
final = emp_salary_projects.merge(avg_hours, on='emp_id', how='left')

# Performance scoring system
final['performance_score'] = (
    (final['work_hours'] / final['work_hours'].max()) * 40 +
    (final['final_salary'] / final['final_salary'].max()) * 30 +
    (final['project_hours'] / final['project_hours'].max()) * 30
)

print("\nFinal Employee Performance Table:\n")
print(final[['name','department','performance_score']])

# Export final file
final.to_csv("Final_HR_Report.csv", index=False)
