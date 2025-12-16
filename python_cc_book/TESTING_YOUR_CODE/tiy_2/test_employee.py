from emp import Employee
import pytest

@pytest.fixture
def new_employee():
    return Employee('tom', 'holand', 2300)

def test_give_default_raise(new_employee):
    new_employee.give_raise()
    assert new_employee.annual_salary == 7300  # 2300 + 5000

def test_give_custom_raise(new_employee):
    new_employee.give_raise(5400)
    assert new_employee.annual_salary == 7700  # 2300 + 5400
