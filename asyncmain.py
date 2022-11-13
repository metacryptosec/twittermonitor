import sqlite3
import config
import argparse
def main():
    parser = argparse.ArgumentParser(description="process some integers.")
    parser.add_argument("-A","--addUser",type=str,help="add twitter user name")
    parser.add_argument("-D", "--deleteUser", type=str, help="delete twitter user name")
    parser.add_argument("-M","--monitor",help="enable monitor",default=False,action='store_true')
    args = parser.parse_args()
    if not args.monitor and args.addUser!=None:
        addUser(args.addUser)
    if not args.monitor and args.deleteUser!=None:
        deleteUser(args.deleteUser)

    if args.monitor:
        pass

def deleteUser(username):
    deleteUserSql="delete from users where username='"+username+"'"
    con = sqlite3.connect(config.dbname)
    cur = con.cursor()
    cur.execute(deleteUserSql)
    con.commit()
    con.close()
def addUser(username):
    addUserSql="insert into users('username') values('"+username+"')"
    con = sqlite3.connect(config.dbname)
    cur = con.cursor()
    cur.execute(addUserSql)
    con.commit()
    con.close()

def initDB():
    userTableSql = "create table if not exists users(id INTEGER PRIMARY KEY AUTOINCREMENT,username VARCHAR(255) unique )";
    tweetsTableSql = "create table if not exists tweets(id INTEGER PRIMARY KEY AUTOINCREMENT,userid INTEGER ,tweet text unique)";
    con = sqlite3.connect(config.dbname)
    cur = con.cursor()
    cur.execute(userTableSql)
    cur.execute(tweetsTableSql)
    con.commit()
    con.close()


if __name__ == '__main__':
    initDB()
    main()

