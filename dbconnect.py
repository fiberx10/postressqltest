import psycopg2
from psycopg2 import Error
import nmap , socket
class Dbconnect() :
    def __init__(self ,host , port , dbname) : 
        self._host = host 
        self._port = port
        self._dbname = dbname
        self.authontification = []
        self.conn = None
     
    def _auth(self, username:str, password:str)->bool :
        self.authontification.append(username)
        self.authontification.append(password)
        return True
    def connect(self) : 
        if len(self.authontification) == 0 : return "Authontification Error  : plaise login first  ! "
        try :
            self.conn = psycopg2.connect(database=self._dbname , user=self.authontification[0], sslmode='prefer' , host=self._host , port=self._port , password=self.authontification[1])
            self.conn.set_session(autocommit=True)
            #cursor = self.conn.cursor()
            # Print PostgreSQL details
            #print("PostgreSQL server information")
            print(self.conn.get_dsn_parameters(), "\n")
        except(Exception , Error) as error : 
            print("postgressql error : " ,  error)
    def put(self , data :list ) -> bool : 
        cursor = self.conn.cursor()
        if len(data) != 4 : return False
        try : 
            # check if already exists
            cursor.execute("select * from test where fisrt_name=%s and second_name=%s;" , (data[0] , data[1]))
            gdata = cursor.fetchall()
            print(gdata)
            if len(gdata) != 0 : return False 
            cursor.execute("insert into test(fisrt_name  ,second_name , date , nationality) values (%s , %s , %s , %s) ;", (data[0] , data[1] , data[2] , data[3]))
            self.conn.commit()
        except (Exception , Error) as _config_error : 
            print(_config_error)
            return False
        return True
    def check(self , data :list )->bool : 
        cursor = self.conn.cursor()
        gdata = ""
        if len(data) != 2 : return 0 
        try : 
            cursor.execute("select date , nationality from test where fisrt_name = '"+data[0]+"' and second_name ='"+data[1]+"';")
            self.conn.commit()
            gdata = cursor.fetchall()
            #for i in ndata : 
             #   print(i , '\n')
            ndata = []
            ndata.append(gdata[0][0].strftime("%m/%d/%Y"))
            ndata.append(gdata[0][1])
            #print(ndata[0])
        except (Exception , Error) as _config_error : 
            print(_config_error)
            return 0
        return ndata
    def update(self , olddata , ndata ) : 
        cursor = self.conn.cursor()
        try : 
            cursor.execute("UPDATE test SET fisrt_name='"+ndata[0]+"' , second_name='"+ndata[1]+"' , date='"+ndata[2]+"' , nationality='"+ndata[3]+"' where fisrt_name='"+olddata[0]+"' and second_name='"+olddata[1]+"' and date='"+olddata[2]+"' and nationality='"+olddata[3]+"' ;")
            self.conn.commit()
            cursor.execute("select fisrt_name , second_name , date , nationality from test where fisrt_name = '"+ndata[0]+"' and second_name ='"+ndata[1]+"';")
            self.conn.commit()
            gdata = cursor.fetchall()
            ndata = []
            ndata.append(gdata[0][0])
            ndata.append(gdata[0][1])
            ndata.append(gdata[0][2].strftime("%m/%d/%Y"))
            ndata.append(gdata[0][3])
            print(ndata)
        except (Exception , Error) as _config_error : 
            print(_config_error)
            return 0
        return ndata
dbconnect = Dbconnect(host ='localhost'  , port=5432 , dbname="test" )
dbconnect._auth(username='fiberx01' ,password="0000")
dbconnect.connect()
# exemple for update()edit data : update(list : olddata , list : ndata )

# data = dbconnect.update(olddata = ['ali' , 'hamza' , '11/06/2001' , 'algi'] , ndata =['ali' , 'hamza' , '11/06/2001' , 'maroc'])


# exemple for check() :  check(list : data) // search for the date and nationality 
# data = dbconnect.check(['ali' , 'hamza'])
# data 
# > ['1/2/2002' , 'moroc']



# exemple for put() : put(list : data) // create a new row : add data to the db
#status = dbconnect.put(['la' , 'ali' , '11/07/2003' , 'maroc'])
# if user already exists status == False
# print(status)
# plaise check if status == True or False
