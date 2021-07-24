
from typing import List
import psycopg2
from psycopg2 import Error
# import nmap , socket
class Dbconnect():
    def __init__(self, host, port, dbname):
        self._host = host
        self._port = port
        self._dbname = dbname
        self.authontification = []
        self.conn = None
    def _auth(self, username: str, password: str) -> bool:
        self.authontification.append(username)
        self.authontification.append(password)
        return True
    def connect(self):
        if len(self.authontification) == 0:
            return "postgres Auth. Error  : plaise login first  ! "
        try:
            self.conn = psycopg2.connect(
                database=self._dbname, user=self.authontification[0], sslmode='prefer', host=self._host, port=self._port, password=self.authontification[1])
            self.conn.set_session(autocommit=True)
            print(self.conn.get_dsn_parameters(), "\n")
        except(Exception, Error) as error:
            print("postgressql error : ",  error)

class getAllMatch(Dbconnect):
    def __init__(self, host, port, dbname):
        super().__init__(host, port, dbname)

    def get_admission_search(self, data: list):
        print(data)
        cursor = self.conn.cursor()
        # prepare sql query
        select_query = "SELECT admission.cne , admission.nom , admission.note_voeux , admission.prenom , offre_formation.phase , filiere.acronyme FROM filiere"
        join_query = " INNER JOIN offre_formation ON filiere.id=filiere INNER JOIN admission ON offre_formation.id=offre_formation "
        condition_query = " WHERE etat='pre_inscrit'"
        ndata_1 = []
        for i in range(len(data)):
            if data[i] != [] : 
                ndata_1.append(data[i])
                condition_query = condition_query + \
                    " AND " + data[i][0] +"='{}' ".format(data[i][1])         
        query = select_query + join_query + condition_query + " ;"
        print(ndata_1 , query)
        ndata_2 = []
        for i in range(len(ndata_1)):
            ndata_2.append(ndata_1[i][1])
        print(ndata_2)
        try:
            cursor.execute(query, tuple(ndata_2))
            gdata = cursor.fetchall()
            print("the data  : " , gdata)
        except (Exception, Error) as _config_error:
            print(_config_error)
            return []
      

    def get_student_info(self, cne ):
        cursor = self.conn.cursor()
        first_query = """SELECT admission.cne  , admission.cin , admission.nom , admission.prenom , admission.nom_ar , admission.prenom_ar , admission.naissance_date , admission.naissance_lieu   , province.nom , admission.sexe ,  pays.libelle , \"e-mail\" , admission.telephone FROM province INNER JOIN admission ON province.id=naissance_province INNER JOIN pays ON pays.id=naissance_pays  where cne='{}'""".format(cne) ;
        try:
            cursor.execute(first_query)
            data = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
            return

        first_query = "SELECT pays.libelle FROM pays INNER JOIN admission ON pays.id = nationalite where cne='{}' ; ".format(cne) ;
        try:
            cursor.execute(first_query)
            data_2 = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
            return
        data = data[0] 
        data_schema = {
            "cin": data[0],
            "cin": data[1],
            "nom": data[2],
            "prenom": data[3],
            "nom_ar": data[4],
            "prenom_ar": data[5],
            "naissance_date": data[6].strftime("%m/%d/%Y"),
            "naissance_lieu": data[7],
            "naissance_province": data[8],
            "sexe": data[9],
            "naissance_pays": data[10],
            "e-mail": data[11],
            "telephone": data[12],
            "nationalite": data_2[0][0],
        }
        print(data_schema)



    def get_student_info_bac(self, cne ):
        cursor = self.conn.cursor()
        first_query = "SELECT admission.bac_annee , admission.bac_mention , province.nom   , serie_baccalaureat.acronyme, admission.bac_type FROM province INNER JOIN admission ON province.id=bac_province INNER JOIN serie_baccalaureat ON serie_baccalaureat.id=bac_serie WHERE cne= '{}' ; ".format(cne) ;
        try:
            cursor.execute(first_query)
            data = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
            return
        data = data[0]
        data_schema = {
            "bac_annee": data[0],
            "bac_mention": data[1],
            "bac_province": data[2],
            "bac_serie": data[3],
            "bac_type": data[4],
        }
        print( "bac data  : " , data_schema)
  


getdata = getAllMatch('localhost' , 5432 , 'inscription2')
getdata._auth('fiberx01' , '0000')
getdata.connect()
getdata.get_all_pays()
#  , ['filiere.acronyme' , 'GE'] , ['diplome.acronyme' , 'DUT'] ]) 
# args : [data] :  any order exemple : [['cne' , 's138216469'] ,['phase' , None] , ['annee_universitere' , '2020'] 
#  , ['filiere.acronyme' , 'GE'] , ['diplome.acronyme' , 'DUT'] ]
# return : [cne , nom , note_voeux , prenom , phase , formation]
