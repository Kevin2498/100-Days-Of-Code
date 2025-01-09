# Given a CSV file with columns EmployeeID, Name, Department, and Salary, 
# write a Python script using pandas to load the data, 
# calculate the average salary per department, and 
# save the result to a new CSV file.

# df = pd.read_csv('fgh.csv')

# df.createTemp("view1")

# empid, name, dept, salary

# select *, AVG(salary) OVER(PARTITION BY dept) as avg_sal from employees

# df.to_csv("s3://")

# For example, if the input is a list of dictionaries with keys Department and Salary, 
# group the data by Department and calculate the total Salary per department.

l1 = [
    {
        "Dept": "ADMIN", 
        "Salary": 100
    },
    {
        "Dept": "ADMIN", 
        "Salary": 100
    },
    {
        "Dept": "SALES", 
        "Salary": 100
    }
]

dept_l1 = [i.get("Dept") for i in l1]
dept_l1 = list(set(dept_l1))

dict1 = {}

for i in deptl1:
    dept_total = 0
    for j in l1:
        if i == j.get("Dept"):
            dept_total += j.get("Salary")
    
    dept_total,i


