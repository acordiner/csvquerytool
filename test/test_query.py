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
        csvquerytool.run_query("SELECT * FROM csv ORDER BY department_id, surname", [self.employees_csv], stdout)
        self.assertEqual(stdout.getvalue(), "\r\n".join(["surname,department_id", "John,None", "Rafferty,31", "Jones,33", "Steinberg,33", "Robinson,34", "Smith,34", ""]))

    def test_join(self):
        stdout = StringIO.StringIO()
        csvquerytool.run_query("SELECT csv.department_name, csv2.surname FROM csv JOIN csv2 ON csv.department_id = csv2.department_id ORDER BY csv.department_id, csv2.surname", [self.departments_csv, self.employees_csv], stdout)
        self.assertEqual(stdout.getvalue(), "\r\n".join(["department_name,surname", "Sales,Rafferty", "Engineering,Jones", "Engineering,Steinberg", "Clerical,Robinson", "Clerical,Smith", ""]))

if __name__ == "__main__":
    unittest.main()
