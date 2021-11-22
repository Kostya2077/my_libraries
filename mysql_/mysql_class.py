import pymysql
from mysql_.common.constants import *
from tqdm import tqdm
import time
import os

class Mysql:


    def __init__(self, host, user, password):
        self.__host = host
        self.__user = user
        self.__password = password


    def create_connection_2_mysql(self):
        try:
            self.connector = pymysql.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                cursorclass=pymysql.cursors.DictCursor
            )
            self.cursor = self.connector.cursor()
            self.cursor.execute(SHOW+DATABASES)
            self.databases = [i["Database"] for i in self.cursor]
            print('connection is successful')
        except:
            self.connector = None
            print('Error connection...')


    def show_databases(self):
        return self.databases


    def create_database(self, database_name):
        if database_name not in self.databases:
            self.cursor.execute(CREATE+DATABASE+database_name)
            self.databases.append(database_name)


    def drop_database(self, database_name):
        if database_name in self.databases:
            self.cursor.execute(DROP+DATABASE+database_name)
            self.databases.pop(self.databases.index(database_name))


    def use_database(self, database_name):
        return MysqlDatabase(self.connector, self.cursor, database_name)


    def dump(self, db_name, dump_db_name):
        if '.sql' not in dump_db_name:
            dump_db_name += '.sql'
        os.system('mysqldump' +
                  ' -u' + self.__user +
                  ' -p' + self.__password + ' ' +
                  db_name + ' > ' + dump_db_name)


    def load_database_into_mysql(self, db_name, path_to_db):
        if db_name not in self.databases:
            self.databases.append(db_name)
            self.create_database(db_name)
        os.system('mysql' +
                  ' -u' + self.__user +
                  ' -p' + self.__password + ' ' +
                  db_name + ' < ' + path_to_db)

# import pickle
# from mysql_.config import *
#
# params = db_config['mysql']
#
# user = params['user']
# host = params['host']
# password = params['password']
#
# with open('/home/kostya/PycharmProjects/my_project/parsers/parsers_rc/urbanus_parser/parsed_base.pickle_', 'rb') as f:
#     data = pickle.load(f)
#
# mysql_client = Mysql(user=user,host=host,password=password)
# mysql_client.create_connection_2_mysql()
# mysql_client.create_database('rc_base')
# database = mysql_client.use_database('rc_base')
#
# params = 'name url price salary offer_price offer_salary'.split()
# params_ = {}
# for i in params:
#     params_[i] = STR
#
# print(params_)
# database.create_table('data', params_)
# table = database.use_table('data')
#
# for i in data:
#     add__ = []
#     for j in i:
#         if isinstance(i[j], str):
#             add__.append(i[j])
#         else:
#             add__.append('|||'.join(i[j]))
#
#     table.insert_one(add__)
#     table.commit()


