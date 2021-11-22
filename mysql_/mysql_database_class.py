from common.constants import *
from mysql_table_class import *

class MysqlDatabase:

    def __init__(self, connector, cursor, db_name):
        self.__connector = connector
        self.__cursor = cursor
        self.__cursor.execute(USE + db_name)
        self.__cursor.execute(SHOW + TABLES)
        self.__tables = [i["Tables_in_" + db_name] for i in self.__cursor]

    def create_table(self, table_name, params):
        if table_name not in self.__tables:
            params = ','.join([key+' '+params[key] for key in params])
            self.__cursor.execute(CREATE + TABLE + table_name + '(' + params + ')')
            self.__tables.append(table_name)


    def drop_table(self, table_name):
        if table_name in self.__tables:
            self.__cursor.execute(DROP + TABLE + table_name)
            self.__tables.pop(self.__tables.index(table_name))


    def use_table(self, table_name):
        if table_name in self.__tables:
            return MysqlTable(self.__connector, self.__cursor, table_name)


    def show_tables(self):
        return self.__tables

