Steps to import all tables(and data):
1.Install postgreSQL
2.Create SWPDB database in postgreSQL
(Can be done by opening psql and writing command 'CREATE DATABASE SWPDB;')
3.Download all files from database folder in github in folder "C:\swpdb"
(! 4.b) can't be executed if other folder choosen, but 4.a can be executed if path in command edited appropriately)
4.Execute such comand in shell:
	a)For tables only:
	psql -U postgres -d SWPDB -f "C:\swpdb\restore.sql"
	b)For data and tables 
	psql -U postgres -d SWPDB -f "C:\swpdb\restoreWithInsertedData.sql"
5.Write password for postgres user.
(Default password is chosen at start of installation)