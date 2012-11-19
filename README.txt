==============
CSV Query Tool
==============

This module provides a very simple command-line tool for running arbitrary SQL 
queries on CSV files. It's useful for situations where you need to quickly 
explore and manipulate CSV files, where using a full database is often overkill.

Say we have the following two files:

*employees.csv:*

::

    surname,department_id
    Rafferty,31
    Jones,33
    Steinberg,33
    Robinson,34
    Smith,34
    John,

*departments.csv:*

::

    department_id,department_name
    31,Sales
    33,Engineering
    34,Clerical
    35,Marketing

Let's load these two CSV files:

::

    $ csvquery employees.csv departments.csv

At this point, you will be presented with an interactive SQL console:

::

    * file 'employees.csv' loaded into table 'csv'
    * file 'departments.csv' loaded into table 'csv2'
    SQL Interactive Console
    =>

You can see that the file ``employees.csv`` was loaded into an SQL table named
``csv`` and the file ``departments.csv`` into a table named ``csv2``. From here,
you can start running whatever SQL queries you want.

Let's select all of the records from the employees table:

::

    => SELECT * FROM csv
    surname,department_id
    Rafferty,31
    Jones,33
    Steinberg,33
    Robinson,34
    Smith,34
    John,None

And now let's join the employees table to the departments table:

::

    => SELECT csv.surname, csv2.department_name FROM csv NATURAL JOIN csv2
    surname,department_name
    Rafferty,Sales
    Jones,Engineering
    Steinberg,Engineering
    Robinson,Clerical
    Smith,Clerical

Press ^D to exit the SQL console when you are done.

You can also specify an SQL query as an argument to ``csvquery`` (which is more 
useful for scripts, where you can't use the interactive console):

::

    $ csvquery -q "SELECT csv.surname, csv2.department_name FROM csv NATURAL JOIN csv2" departments.csv

The output of this command is CSV formatted, so it can be redirected to an 
output CSV file if required:

::

    $ csvquery -q "SELECT csv.surname, csv2.department_name FROM csv NATURAL JOIN csv2" departments.csv > employee_departments.csv

**Warning:** All of the input CSV files are loaded into memory to perform the 
queries. This means that this module is not appropriate for processing very 
large CSV files.
