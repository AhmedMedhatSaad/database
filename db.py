import cx_Oracle



class Database:
    def __init__(self):
        self.conn = cx_Oracle.connect('username/password@//localhost:1521/xe')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE Account (ACCOUNTUSERNAME	VARCHAR2(15) NOT NULL,ACCOUNTPASSWORD VARCHAR2(15) NOT NULL,AUTOFILLING	NUMBER(1,0)	NOT NULL,AUTOGENERATING	NUMBER(1,0) NOT NULL,PRIMARY KEY (ACCOUNTUSERNAME))")
        self.cur.execute("CREATE TABLE FOLDER (FOLDERNAME VARCHAR2(15) NOT NULL,FOLDERACCOUNT VARCHAR2(15) NOT NULL,PRIMARY KEY (FOLDERNAME),FOREIGN KEY (FOLDERACCOUNT) REFERENCES Account(ACCOUNTUSERNAME))")
        self.cur.execute("CREATE TABLE APPACCOUNT (APPUSERNAME VARCHAR2(15) NOT NULL,APPPASSWORD VARCHAR2(15) NOT NULL,APPNAME VARCHAR2(15) NOT NULL,URL VARCHAR2(50) NOT NULL,NOTE	VARCHAR2(100),APPFOLDERNAME VARCHAR2(15) NOT NULL,PRIMARY KEY (APPUSERNAME),FOREIGN KEY (APPFOLDERNAME) REFERENCES FOLDER(FolderName))")
        #self.cur.execute("CREATE TABLE SECURENOTE (NOTETITLE VARCHAR2(15) NOT NULL,TXT VARCHAR2(100) NOT NULL,APPFOLDERNAME VARCHAR2(15) NOT NULL,PRIMARY KEY (NOTETITLE),FOREIGN KEY (APPFOLDERNAME) REFERENCES FOLDER(FolderName)")
        self.conn.commit()


    # Account 
    # Sign Up
 
    def InsertIntoAccount(self,AccountUserName,AccountPassword,AutoFilling,AutoGenerating):
        self.cur.execute("INSERT INTO ACCOUNT (AccountUserName, AccountPassword, AutoFilling, AutoGenerating) VALUES ("+AccountUserName+","+AccountPassword +","+str(AutoFilling)+","+str(AutoGenerating)+")")
        self.conn.commit()

    def RemoveFromAccount(self, AccountUserName):
        self.cur.execute("DELETE FROM ACCOUNT WHERE AccountUserName = "+AccountUserName)
        self.conn.commit()

    def UpdatePasswordAccount(self,AccountUserName,AccountPassword):
        self.cur.execute("UPDATE ACCOUNT SET AccountPassword = "+AccountPassword+" WHERE AccountUserName = "+AccountUserName)
        self.conn.commit()
    
    def FetchAccountPassword(self,AccountUserName):
        checkPass = self.cur.execute("SELECT AccountPassword FROM Account WHERE AccountUserName = "+AccountUserName)
        return checkPass   

    # Folder
    def InsertIntoFolder(self,FolderName,FolderAccount):
        self.cur.execute("INSERT INTO FOLDER (FolderName,FolderAccount) VALUES ("+FolderName+","+FolderAccount+")")
        self.conn.commit()

    def RemoveFromFolder(self, FolderName):
        self.cur.execute("DELETE FROM APPACCOUNT WHERE APPFOLDERNAME = "+FolderName)
        #self.cur.execute("DELETE FROM SECURENOTE WHERE APPFOLDERNAME = "+FolderName)
        self.cur.execute("DELETE FROM FOLDER WHERE FolderName = "+FolderName)
        self.conn.commit()

    # AppAccount

    def InsertIntoAppAccount(self,AppUserName,AppPassword,AppName,URL,Note,AppFolderName):
        self.cur.execute("INSERT INTO APPACCOUNT (AppUserName, AppPassword,AppName, URL,Note, AppFolderName) VALUES ("+AppUserName+","+AppPassword+","+AppName+","+URL+","+Note+","+AppFolderName+")")
        self.conn.commit()

    def RemoveFromAppAccount(self, AppAccountUserName):
        self.cur.execute("DELETE FROM APPACCOUNT WHERE AppAccountUserName = "+AppAccountUserName)
        self.conn.commit()

    def UpdatePasswordAppAccount(self,AppAccountUserName,AppAccountPassword):
        self.cur.execute("UPDATE APPACCOUNT SET AppAccountPassword = "+AppAccountPassword+" WHERE AppAccountUserName = "+AppAccountUserName)
        self.conn.commit()
    
    def FetchAppAccountRecord(self,AppAccountUserName):
        rows = self.cur.execute("SELECT * FROM AppAccount WHERE AppAccountUserName = "+AppAccountUserName)
        return rows
    
    """
    #SecureNote

    def InsertIntoSN(self,NOTETITLE,TXT,APPFOLDERNAME):
        self.cur.execute("INSERT INTO SECURENOTE (NOTETITLE, TXT,APPFOLDERNAME) VALUES ("+NOTETITLE+","+TXT+","+APPFOLDERNAME+")")
        self.conn.commit()

    def RemoveFromSN(self,NOTETITLE):
        self.cur.execute("DELETE FROM SECURENOTE WHERE NOTETITLE = "+NOTETITLE)
        self.conn.commit()

    def FetchSN(self,table,AppAccountUserName):
        rows = self.cur.execute("SELECT * FROM " +table+" WHERE AppAccountUserName = "+AppAccountUserName)
        return rows
    """
    
    def Fetchall(self,table):
        self.cur.execute("SELECT * FROM "+table)
        rows = self.cur.fetchall()
        return rows

    def __del__(self):
        self.conn.close()


db = Database()