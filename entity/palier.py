class Palier:

    def __init__(self,id=0,montant_min=0,montant_max=0,pourcentage=0):
        self.id=id
        self.montant_min =montant_min
        self.montant_max=montant_max
        self.pourcentage = pourcentage

    def _get_id(self):
        return self.id

    def _set_id(self, id):
        self.id  =  id

    def _get_montant_min(self):
        return self.montant_min

    def _set_montant_min(self, montant_min):
        self.montant_min  =  montant_min

    def _get_montant_max(self):
        return self.montant_max

    def _set_montant_max(self, montant_max):
        self.montant_max  =  montant_max

    def _get_pourcentage(self):
        return self.pourcentage

    def _set_pourcentage(self, pourcentage):
        self.pourcentage  =  pourcentage


    def get_columns(self):
        return 'montant_min,montant_max,pourcentage'

    def get_data(self):
        return "{0},{1},{2}".format(self.montant_min,self.montant_max,self.pourcentage)

    def get_alldatas(self):
        return (self.montant_min,self.montant_max,self.pourcentage,self.id)
