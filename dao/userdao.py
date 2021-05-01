import PYGescom.db.database as bd
import PYGescom.entity.users as usr

class Userdao:
    iduser=0
    idoffice=0


def create_user(user):
    db = bd.Database()
    query = "INSERT INTO users ({0}) VALUES ({1});".format(user.get_columns(),user.get_data())
    # data="'{1}','{2}','{3}','{4}','{5}'"nom,prenom,adresse,phone,postalcode,salesrep
    db.query(query)
    print(query)
    
def update_user(user):
    db = bd.Database()
    query=''' UPDATE users
              SET login = ? ,
                  password = ? ,
                  idprofil = ? ,
                  status = ? ,
                  idoffice = ? 
              WHERE id = ?'''
    db.update(query,user.get_alldatas())
    print(query)
    
def delete_user(user):
    db = bd.Database()
    query=''' UPDATE users
              SET login = ? ,
                  password = ? ,
                  idprofil = ? ,
                  status = ? 
              WHERE id = ?'''
    db.update(query,user.get_alldatas())
    print(query)

def active_user(user):
    db = bd.Database()
    query=''' UPDATE users
              SET login = ? ,
                  password = ? ,
                  idprofil = ? , 
                  status = ? 
              WHERE id = ?'''
    db.update(query,user.get_alldatas())
    print(query)

def login(login,password):
    db = bd.Database()
    query= "SELECT * FROM users where login=? and password=?"
    cur = db.getquery(query,(login,password))
    rows = cur.fetchone()
    Userdao.iduser=rows[0]
    Userdao.idoffice=rows[6]
    print(rows)

    print('id user ',Userdao.iduser,' id office ',Userdao.idoffice)
    return rows
def getAll():
    db = bd.Database()
    query= "SELECT id,login,password,idprofil,status,idoffice FROM users"
    cur = db.query(query)
    rows = cur.fetchall()
    return rows

def main():
    login('test','test')
    print(Userdao.iduser,' ',Userdao.idoffice)


