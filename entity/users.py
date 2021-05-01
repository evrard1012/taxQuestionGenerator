class Users:

    def __init__(self,id=0,login='',password='',idprofil=1,status=1,idoffice=0):
        self.id=id
        self.login=login
        self.password=password
        self.idprofil=idprofil
        self.status=status
        self.idoffice=idoffice

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

    def _get_status(self):
        return self.status

    def _set_status(self, status):
        self.status  =  status
    def _get_idoffice(self):
        return self.idoffice

    def _set_idoffice(self, idoffice):
        self.idoffice  =  idoffice
        
    def get_columns(self):
        return 'login,password,idprofil,status,idoffice'

    def get_data(self):
        return "'{0}','{1}',{2},{3},{4}".format(self.login,self.password,self.idprofil,self.status,self.idoffice)

    def get_alldatas(self):
        return (self.login,self.password,self.idprofil,self.status,self.idoffice,self.id)
    def get_alldatas2(self):
        return (self.id,self.login,self.password,self.idprofil,self.status,self.idoffice)
