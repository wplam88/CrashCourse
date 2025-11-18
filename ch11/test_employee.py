from city_functions import Employee # type: ignore

def employee():
    "New Employee"
    return Employee('Will', 'Lam', 65000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 70000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.salary == 75000

