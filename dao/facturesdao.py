import alino.db.database as bd
import alino.entity.factures as f


def create_Facture(facture):
    db = bd.Database()
    query = "INSERT INTO factures ({0}) VALUES ({1});".format(facture.get_columns(),facture.get_data())
    db.query(query)
    print(query)
    


def getAll():
    db = bd.Database()
    query= "SELECT * FROM factures"
    cur = db.query(query)
    
    rows = cur.fetchall()
    return rows

def getAll2():
    db = bd.Database()
    query= "SELECT montant, id FROM factures"
    cur = db.query(query)
    rows = cur.fetchall()
    return rows


def main():
    facture = f.Facture(0,1045000)
    create_Facture(facture)
