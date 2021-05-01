import PYGescom.db.database as bd
import PYGescom.entity.profil as p


def create_Profil(profil):
    db = bd.Database()
    query = "INSERT INTO profils ({0}) VALUES ({1});".format(profil.get_columns(),profil.get_data())
    db.query(query)
    print(query)
    
def update_Profil(profil):
    db = bd.Database()
    query=''' UPDATE profils
              SET libelle = ?,
                  status = ?
              WHERE id = ?'''
    db.update(query,profil.get_alldatas())
    print(query)
    
def delete_Profil(profil):
    db = bd.Database()
    query=''' UPDATE profils
              SET libelle = ?,
                  status = ?
              WHERE id = ?'''
    db.update(query,profil.get_alldatas())
    print(query)

def active_Profil(profil):
    db = bd.Database()
    query=''' UPDATE profils
              SET libelle = ? ,
                  status = ?
              WHERE id = ?'''
    db.update(query,profil.get_alldatas())
    print(query)

def getAll():
    db = bd.Database()
    query= "SELECT * FROM profils"
    cur = db.query(query)
    
    rows = cur.fetchall()
    return rows

def getAll2():
    db = bd.Database()
    query= "SELECT libelle, id FROM profils"
    cur = db.query(query)
    rows = cur.fetchall()
    return rows


def main():
    client = p.Profil(0,"profil 1",1)
    create_Profil(client)
    client2 = p.Profil(4,"profil 1",1)
    delete_Profil(client2)
    client1 = p.Profil(4,"profil 1",1)
    active_Profil(client1)
