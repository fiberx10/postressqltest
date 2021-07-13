
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
        cursor = self.conn.cursor()
        # prepare sql query
        select_query = "SELECT cne , admission.nom , admission.prenom , phase , code_ministere FROM diplome "
        join_query = "INNER JOIN filiere ON diplome.id=diplome INNER JOIN offre_formation ON filiere.id=filiere INNER JOIN admissin ON offre_formation.id=offre_formation"
        condition_query = "where etat='pr_inscrit'"
        ndata_1 = []
        for i in range(len(data)):
            if data[i] != None:
                ndata_1.append(data[i])
                condition_query = condition_query + \
                    " AND " + data[i][0] + "=%s "
        query = select_query + join_query + condition_query + " ;"
        ndata_2 = []
        for i in range(len(ndata_1)):
            ndata_2.append(ndata_1[i][1])
        try:
            cursor.execute(query, tuple(ndata_2))
            gdata = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
            return []
        return gdata

    def get_student_info(self, cne: int):
        cursor = self.conn.cursor()
        # get fisrt infos
        first_query = "SELECT cne , cin , nom , prenom , nom_ar , prenom_ar , sexe , naissance_date , naissance_lieu , naissance_lieu_ar , e-mail ,telephone , bac_type_etablissement , bac_annee , bac_mention  FROM admission WHERE cne =%s"
        try:
            cursor.execute(first_query, (cne,))
            first_data = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
            return

        cursor = self.conn.cursor()
        # get  naissance_province
        second_query = "SELECT province.nom FROM province INNER JOIN admission ON province.id=naissance_province WHERE cne=%s"
        try:
            cursor.execute(second_query, (cne,))
            second_data = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
            return

        cursor = self.conn.cursor()
        # get  naissance_pays
        third_query = "SELECT pays.pays FROM pays INNER JOIN admission ON pays.id=naissance_pays WHERE cne=%s"
        try:
            cursor.execute(third_query, (cne,))
            third_data = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
            return
        cursor = self.conn.cursor()
        # get  naissance_pays
        forth_query = "SELECT pays.pays FROM pays INNER JOIN admission ON pays.id=nationalite WHERE cne=%s"
        try:
            cursor.execute(forth_query, (cne,))
            forth_data = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
            return
        cursor = self.conn.cursor()
        # get  bac_ser
        fifth_query = "SELECT serie_baccalaureat.code_ministere FROM serie_baccalaureat INNER JOIN admission ON serie_baccalaureat.id=bac_serie WHERE cne=%s"
        try:
            cursor.execute(fifth_query, (cne,))
            fifth_data = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
            return
        cursor = self.conn.cursor()
        # get  bac_province
        sixth_query = "SELECT province.nom FROM province INNER JOIN admission ON province.id=bac_province WHERE cne=%s"
        try:
            cursor.execute(sixth_query, (cne,))
            sixth_data = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
            return
        cursor = self.conn.cursor()
        # get  bac_acadeie
        seventh_query = "SELECT academie.nom FROM academie INNER JOIN admission ON academie.id=bac_academie WHERE cne=%s"
        try:
            cursor.execute(seventh_query, (cne,))
            seventh_data = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
            return
        # return all dat
        return_data = [first_data, second_data, third_data, forth_data]
        return return_data
    def student_data(self, data):
        data_schema = {
            "persone": data[0],
            "cne": data[1],
            "code_apogee": data[2],
            "bac_type_etablissement": data[3],

            "bac_annee": data[4],
            "bac_serie": data[5],
            "bac_province": data[6],
            "bac_academie": data[7],

            "bac_mention": data[8],
            "nom_prenom_mere": data[9],
            "nom_prenom_pere": data[10],
            "csp_mere": data[11],

            "csp_pere": data[12],
            "adresse_parents": data[13],
            "adresse_province_parents": data[14],
            "adresse_pays_parents": data[15],

            "email_parents": data[16],
            "telephone_parents": data[17],
        }
        pays_id = self.get_pays_id(data_schema['adresse_pays_parents'])

        data_list = []
        for key, value in data_schema.items():
            a = [key, value]
            data_list.append(a)
            a = []
        cursor = self.conn.cursor()

        query = "INSERT INTO etudent VALUES (%s , %s , %s ,%s ,%s , %s , %s ,%s ,%s , %s , %s ,%s ,%s , %s , %s ,%s ,%s ,%s);"
        try:
            cursor.execute(sixth_query, (cne,))
            sixth_data = cursor.fetchall()
        except (Exception, Error) as _config_error:
            print(_config_error)
            return
    def get_pays_id(self , pays_name) :
        cursor = self.conn.cursor()
        query = "select id from pays where nom=%s ;"
        try  : 
            cursor.execute(query, (pays_name))
            data = cursor.fetchone()
        except (Exception , Error) as _config_error : 
            print(_config_error)
            return 
        return data
    def get_province_id(self , province_name) :
        cursor = self.conn.cursor()
        query = "select id from province where nom=%s ;"
        try  : 
            cursor.execute(query, (province_name))
            data = cursor.fetchone()
        except (Exception , Error) as _config_error : 
            print(_config_error)
            return 
        return data
    def get_pays_id(self , acad_name) :
        cursor = self.conn.cursor()
        query = "select id from pays where nom=%s ;"
        try  : 
            cursor.execute(query, (pays_name))
            data = cursor.fetchone()
        except (Exception , Error) as _config_error : 
            print(_config_error)
            return 
        return data
    def get_pays_id(self , pays_name) :
        cursor = self.conn.cursor()
        query = "select id from pays where nom=%s ;"
        try  : 
            cursor.execute(query, (pays_name))
            data = cursor.fetchone()
        except (Exception , Error) as _config_error : 
            print(_config_error)
            return 
        return data
    def get_pays_id(self , pays_name) :
        cursor = self.conn.cursor()
        query = "select id from pays where nom=%s ;"
        try  : 
            cursor.execute(query, (pays_name))
            data = cursor.fetchone()
        except (Exception , Error) as _config_error : 
            print(_config_error)
            return 
        return data



    def person_data(self, data):
        data_schema = {
            "cin": data[0],
            "nom": data[1],
            "prenom": data[2],
            "nom_ar": data[3],
            "prenom_ar": data[4],
            "nationalite": data[5],
            "naissance_date": data[6],
            "naissance_a_letranger": data[7],
            "naissance_lieu": data[8],
            "naissance_lieu_ar": data[9],
            "naissance_province": data[10],
            "naissance_pays": data[11],
            "sexe": data[12],
            "telephone": data[13],
            "e-mail": data[14],
            "handicap": data[15],
            "situation_familiale": data[16],
            "csp": data[17],
            "adresse": data[18],
            "adresse_province": data[19],
            "email_usmba": data[20],
            "photo": data[21],
        }




# select cne , nom ,  prenom , moyenne , phase from diplome inner join id =
