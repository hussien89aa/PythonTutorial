



import sqlite3

def main():
    db=sqlite3.connect("information.db")
    db.row_factory=sqlite3.Row
    db.execute("create table if not exists Admin(Name text,age int)")
    db.execute("insert into Admin (Name,age) values (? , ?)",("Hussein",26))
    db.execute("insert into Admin (Name,age) values (? , ?)",("Jena",1))
    db.commit()
    #db.execute("delete from Admin where name='Jena'")
    #db.execute("Update Admin set age=2 where name='Jena'")
    cusror=db.execute("select * from Admin")
    for row in cusror:
        print("Name:{}, Age:{}".format(row["Name"],row["age"]))




if __name__ == '__main__':main()
