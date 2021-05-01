class Facture:

    def __init__(self,id=0,montant=0):
        self.id=id
        self.montant =montant

    def _get_id(self):
        return self.id

    def _set_id(self, id):
        self.id  =  id

    def _get_libelle(self):
        return self.montant

    def _set_libelle(self, montant):
        self.montant  =  montant

    def get_data(self):
        return "{1}".format(self.montant)

    def get_alldatas(self):
        return (self.montant,self.id)
