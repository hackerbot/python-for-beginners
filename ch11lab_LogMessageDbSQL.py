import sqlite3
def createDb():
    db = sqlite3.connect('database.db')
    db.execute('drop table if exists table1')
    db.execute('drop table if exists table2')
    db.execute('create table table1 (field1 text)')
    db.execute('insert into table1 (field1) values ("value1")')
    db.commit()
createDb()

class LogMessageDbSQL:
    def __init__(self,dbname):
        self.dbname = dbname
        db = sqlite3.connect(self.dbname)
        print(dbname, 'has been successfully initialized.')
    def read(self): #read and print
        print(self.dbname, 'now contains this data:')
        db = sqlite3.connect(self.dbname)
        db.row_factory = sqlite3.Row
        table = db.execute('select * from table1')
        for each in table:
            print(dict(each))
        return '' #to clear none message
    def write(self): #copy and write
        db = sqlite3.connect(self.dbname)
        data = input("What would you like to add to field1 of table1?\n")
        db.execute('insert into table1 (field1) values ("{}")'.format(data))
        db.commit()
        print('\n')
        print(self.dbname, 'has been added with new data: "{}"'.format(data))
        return '' #to clear none message

database1 = LogMessageDbSQL('database.db')
print(database1.dbname)
print(database1.read())
print(database1.write())
#checking work
print(database1.read())