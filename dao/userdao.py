import alino.db.database as bd
import alino.entity.users as usr

class Userdao:
    idprofil=1


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
                  nom = ? ,
                  idprofil = ? 
              WHERE id = ?'''
    db.update(query,user.get_alldatas())
    print(query)

def login(login,password):
    db = bd.Database()
    query= "SELECT * FROM users where login=? and password=?"
    cur = db.getquery(query,(login,password))
    rows = cur.fetchone()
    Userdao.idprofil=rows[4]
    print(rows)
    return rows
def getAll():
    db = bd.Database()
    query= "SELECT id,login,password,nom,idprofil FROM users"
    cur = db.query(query)
    rows = cur.fetchall()
    return rows

def main():
    login('test','test')
    print(Userdao.iduser,' ',Userdao.idoffice)


