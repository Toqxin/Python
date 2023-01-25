from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
import sys

SERVER_NAME='Your Desktop'
DATABASE_NAME='DB Name'

def createConnection():
    conn=f'DRIVER={{SQL Server}};'\
         f'SERVER={SERVER_NAME};'\
         f'DATABASE={DATABASE_NAME}'

    global db 
    db = QSqlDatabase.addDatabase('QODBC')
    db.setDatabaseName(conn)

    if db.open():
        print('connected to SQL Server')
        return True
    else:
        print('connection failed')
        return False

def displayData(sqlStmt):
    print('processing...')
    qry=QSqlQuery(db)
    qry.prepare(sqlStmt)
    qry.exec()

    model=QSqlQueryModel()
    model.setQuery(qry)
    
    view=QTableView()
    view.setModel(model)
    return view

if __name__=='__main__':
    app=QApplication(sys.argv)
    
    if createConnection():
        SQL_STATEMENT='SELECT * FROM Table Name'
        dataView = displayData(SQL_STATEMENT)
        dataView.show()

    app.exit()
    sys.exit(app.exec_())

