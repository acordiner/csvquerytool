import csvquerytool
import os
import StringIO
import unittest


class QueryTests(unittest.TestCase):

    def setUp(self):
        data_path = os.path.join(os.path.dirname(__file__), "data")
        self.departments_csv = os.path.join(data_path, "departments.csv")
        self.employees_csv = os.path.join(data_path, "employees.csv")

    def test_select(self):
        stdout = StringIO.StringIO()
        csvquerytool.run_query("SELECT * FROM employees ORDER BY department_id, surname", [self.employees_csv], stdout)
        self.assertEqual(stdout.getvalue(), "\r\n".join(["surname,department_id", "John,None", "Rafferty,31", "Jones,33", "Steinberg,33", "Robinson,34", "Smith,34", ""]))

    def test_join(self):
        stdout = StringIO.StringIO()
        csvquerytool.run_query("SELECT d.department_name, e.surname FROM departments d JOIN employees e ON d.department_id = e.department_id ORDER BY d.department_id, e.surname", [self.departments_csv, self.employees_csv], stdout)
        self.assertEqual(stdout.getvalue(), "\r\n".join(["department_name,surname", "Sales,Rafferty", "Engineering,Jones", "Engineering,Steinberg", "Clerical,Robinson", "Clerical,Smith", ""]))

if __name__ == "__main__":
    unittest.main()
