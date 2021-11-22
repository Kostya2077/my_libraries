from common.constants import *


class MysqlTable:


    def __init__(self, connector, cursor, table_name):
        self.__connector = connector
        self.__cursor = cursor
        self.__table_name = table_name
        self.__cursor.execute(SHOW + COLUMNS + FROM + table_name)
        self.__columns = [i['Field'] for i in self.__cursor]


    def show_columns(self):
        return self.__columns


    def insert_one(self, data):
        self.__cursor.execute(INSERT + INTO + self.__table_name +
                            '(' +','.join([key for key in self.__columns]) + ')' +
                              VALUES +
                              '(' + ','.join(['"'+value+'"' for value in data]) + ')')

    def insert_many(self, data):
        data = ['('+','.join(['"'+value+'"' for value in data_])+')' for data_ in data]
        self.__cursor.execute(INSERT + INTO + self.__table_name +
                            '(' +','.join([key for key in self.__columns]) + ')' +
                              VALUES +
                              ','.join(data))

    def commit(self):
        self.__connector.commit()