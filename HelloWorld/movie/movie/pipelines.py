# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class MoviePipeline(object):
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost','root','admin','newdb',charset='utf8')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        # insert_sql ="insert into tb_news(content) VALUES(%s)"
        self.cursor.execute("INSERT INTO meiju(name) VALUES(%s)",(item['name']))
        self.conn.commit()
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
                # return item
