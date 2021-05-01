class Profil:

    def __init__(self,id=0,libelle='',status=0):
        self.id=id
        self.libelle =libelle
        self.status=status

    def _get_id(self):
        return self.id

    def _set_id(self, id):
        self.id  =  id

    def _get_libelle(self):
        return self.libelle

    def _set_libelle(self, libelle):
        self.libelle  =  libelle

    def _get_status(self):
        return self.status

    def _set_status(self, status):
        self.status  =  status

    def get_columns(self):
        return 'libelle,status'

    def get_data(self):
        return "'{0}',{1}".format(self.libelle,self.status)

    def get_alldatas(self):
        return (self.libelle,self.status,self.id)
