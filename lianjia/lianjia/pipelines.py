# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class LianjiaPipeline(object):
    #连接数据库
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost", user="root", password="taistrive0900",
            database="house", port=3306, charset='utf8'
        )
    #数据库操作
    def process_item(self, item, spider):
        #分别插入每个城市的数据，一共十个城市
        # insert_sql = "insert into dalian_salehouse(price,per_price,style,house_size,region,focus,establish_year,floor) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        # insert_sql = "insert into beijing_salehouse(price,per_price,style,house_size,region,focus,establish_year,floor) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        # insert_sql = "insert into changchun_salehouse(price,per_price,style,house_size,region,focus,establish_year,floor) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        # insert_sql = "insert into changsha_salehouse(price,per_price,style,house_size,region,focus,establish_year,floor) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        # insert_sql = "insert into chengdu_salehouse(price,per_price,style,house_size,region,focus,establish_year,floor) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        # insert_sql = "insert into shenzhen_salehouse(price,per_price,style,house_size,region,focus,establish_year,floor) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        # insert_sql = "insert into shanghai_salehouse(price,per_price,style,house_size,region,focus,establish_year,floor) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        # insert_sql = "insert into nanjing_salehouse(price,per_price,style,house_size,region,focus,establish_year,floor) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        # insert_sql = "insert into shenyang_salehouse(price,per_price,style,house_size,region,focus,establish_year,floor) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        insert_sql = "insert into xiamen_salehouse(price,per_price,style,house_size,region,focus,establish_year,floor) values(%s,%s,%s,%s,%s,%s,%s,%s)"

        try:
            cursor = self.conn.cursor()
            # 一条一条进行插入
            row = cursor.execute(insert_sql, (
                # 获取对应键的值
                float(item.get("price")), float(item.get("per_price")), item.get("style"),
                float(item.get("house_size")),
                str(item.get("region")), int(item.get("focus")), int(item.get("establish_year")), item.get("floor")
            ))
            #数据库操作最后要commit，要不然数据无法插入数据库
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        pass
        return item