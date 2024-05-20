import employee_info

def test_get_employees_by_age_range():
    expected_result=[]
    expected_result=[{"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    result=employee_info.get_employees_by_age_range(20, 24)
    assert (result==expected_result)
def test_calculate_average_salary():
    expected_result=60166.666666666664
    result=employee_info.calculate_average_salary()
    assert (result==expected_result)
    
def test_get_employees_by_dept():
    expected_result=[]
    expected_result=[{"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    result=employee_info.get_employees_by_dept("Sales")
    assert (result==expected_result)