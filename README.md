                                                    Data Modeling with Postgres
                                                    ===========================

Purpose of this Project
------------------------
Building a Data Model out of log files using python in Postgres database server. 

Description
------------
In present world everything is data, but not in a particular shape. Making shape out of it gives it a life and allows us to make business out of it and decisions based on meaning we get out of data.
Sparkify is a start up company provides music streaming app. They have collected data about their users activity. Analytics team wanted to understand about songs users are listening to. Currently, they have data in Json logs on user activity on the app but there is no way to query the data in that format. Here is the project how to transform the Json log file to a strucured format where their team can query and get Analysis out of it.

Script files need to develop to reach the goal
-----------------------------------------------
1.Sql_queries.py - Contains the definations for select, insert and drop queries. Those are required to build the model in Postgres.
2.Create_table.py - Contains the definations for creating database and tables.Utilises the definations build in sql_queries script.
3.etl.py - It is the pipeline between source Json logs and Postgres Tables. Contains the definations to transform the log files to tablular format and other changes to data.
4.test.ipynb - It is file where to see result of the scripts we developed.

Steps to execute the scripts
-----------------------------
1.Run the create_table.py in a terminal (Make sure to restart the kernal if you open any other file like etl.ipynb or test.ipynb because connection will be open and cannot run create_tables.py successfully).

2.Run etl.py in same terminal.

3.Run test.ipynb to see the results.

