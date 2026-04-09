emp = {"Rahul":50000,"Sita":30000,"Nita":100000,"swastu":70000}

sorted_emp = sorted(emp.items(), key=lambda x:x[1])

print(sorted_emp)
