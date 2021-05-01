class Users:

    def __init__(self,id=0,login='',password='',nom='',idprofil=1):
        self.id=id
        self.login=login
        self.password=password
        self.nom=nom
        self.idprofil=idprofil

    def _get_id(self):
        return self.id

    def _set_id(self, id):
        self.id  =  id

    def _get_login(self):
        return self.login

    def _set_login(self, login):
        self.nom  =  login

    def _get_password(self):
        return self.password

    def _set_password(self, password):
        self.password  =  password

    def _get_idprofil(self):
        return self.idprofil

    def _set_idprofil(self, idprofil):
        self.idprofil  =  idprofil

    def _get_nom(self):
        return self.nom

    def _set_nom(self, nom):
        self.nom  =  nom
        
    def get_columns(self):
        return 'login,password,nom,idprofil'

    def get_data(self):
        return "'{0}','{1}','{2}',{3}".format(self.login,self.password,self.nom,self.idprofil)

    def get_alldatas(self):
        return (self.login,self.password,self.nom,self.idprofil)
    def get_alldatas2(self):
        return (self.id,self.login,self.password,self.nom,self.idprofil)
