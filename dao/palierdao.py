import alino.db.database as bd
import alino.entity.palier as p


def create_Palier(profil):
    db = bd.Database()
    query = "INSERT INTO paliers ({0}) VALUES ({1});".format(profil.get_columns(),profil.get_data())
    db.query(query)
    print(query)
    


def getAll():
    db = bd.Database()
    query= "SELECT * FROM paliers"
    cur = db.query(query)
    
    rows = cur.fetchall()
    return rows

def getAll2():
    db = bd.Database()
    query= "SELECT montant_min,montant_max, id FROM paliers"
    cur = db.query(query)
    rows = cur.fetchall()
    return rows


def main():
    client = p.Palier(0,500000,1000000)
    create_Palier(client)
