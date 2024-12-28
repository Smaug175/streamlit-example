import os
from bin.utils.normal_sql_centences import create_sentences, insert_sentences_list
import sqlite3

class SQLiteControl:
    def __init__(self, logger):
        self.logger = logger

        # 按照不同的机床设置不同的数据文件
        self.database_path = {
            "DC0124": "database/mold/DC0124.db",
            "DC0121": "database/mold/DC0121.db",
            "DC0125": "database/mold/DC0125.db",
        }

        # 创建数据的保存文件夹
        if not os.path.exists('database'):
            os.makedirs('database')
        if not os.path.exists('database/mold'):
            os.makedirs('database/mold')

        for key in self.database_path:
            if not os.path.exists(self.database_path[key]):
                # self.logger.error(self.database_path[key] + ' 数据库不存在')
                conn = sqlite3.connect(self.database_path[key])
                cursor = conn.cursor()
                for table_name in create_sentences[key]:
                    cursor.execute(create_sentences[key][table_name])
                conn.commit()
                conn.close()
                # self.logger.info(self.database_path[key] + ' 数据库创建成功')
                print(self.database_path[key] + ' 数据库创建成功')

    def insert_data(self, data: dict):
        keys = data.keys()
        for key in keys:
            if key == '管件参数':
                continue
            machine = key[:6]
            table_name = key[7:-4]
            numbers = int(key[-4:])
            key_data = data[key]
            machine_table_tuple = insert_sentences_list[machine][table_name][0]
            machine_table_insert_sentences = insert_sentences_list[machine][table_name][1]
            input = []
            for mtt in machine_table_tuple:
                if mtt == '%%Cd0':
                    # 转换回来
                    mtt = '%%Cd'
                if mtt == '图号': # 转换为数字保存
                    input.append(numbers)
                else:
                    input.append(str(key_data[mtt]))
            # print(machine, table_name, key_data,machine_table_tuple, input)
            conn = sqlite3.connect(self.database_path[machine])
            cursor = conn.cursor()
            # print(machine_table_insert_sentences)
            cursor.execute(machine_table_insert_sentences, input)
            conn.commit()
            conn.close()

    def query(self, query):
        # TODO
        pass

    def delete(self, delete):
        # TODO
        pass

    def update(self, update):
        # TODO
        pass


if __name__ == '__main__':
    SQLiteControl(logger = None)