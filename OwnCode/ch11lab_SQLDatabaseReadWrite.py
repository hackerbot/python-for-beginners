import sqlite3
db = sqlite3.connect('database.db')
db.execute('drop table if exists table1')
db.execute('drop table if exists table2')
db.execute('create table table1 (field1 text)')
db.execute('insert into table1 (field1) values ("value1")')
db.commit()

class SQLDatabaseReadWrite:
    def __init__(self,databasename):
        self.databasename = databasename
        db = sqlite3.connect(self.databasename)
        print(databasename, 'has been successfully initialized.')
    def read(self): #read and print
        db = sqlite3.connect(self.databasename)
        db.row_factory = sqlite3.Row
        table = db.execute('select * from table1')
        for each in table:
            print(dict(each))
        return '' #to clear none message
    def write(self): #copy and write
        db = sqlite3.connect(self.databasename)
        data = input("What would you like to add to field1 of table1?\n")
        db.execute('insert into table1 (field1) values ("{}")'.format(data))
        db.commit()
        print('\nInputed data has been added to the new database', self.databasename)
        return '' #to clear none message

database1 = SQLDatabaseReadWrite('database.db')
print(database1.databasename)
print(database1.read())
print(database1.write())
#checking work
print(database1.read())