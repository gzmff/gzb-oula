from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request
import threading
import sqlite3
import os
import datetime
from selenium.webdriver.common.keys import Keys
import time
import MySQLdb
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

def insert(mark,price,note,src1,src2):
    try:
        conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='admin',db='scraping',charset='utf8')
        cur = conn.cursor()
        cur.execute("INSERT INTO testmodel_phone(wMark,wPrice,wNote,wSrc1,wSrc2) VALUES(%s,%s,%s,%s,%s)",(mark,price,note,src1,src2))
        cur.close()
        conn.commit()
        conn.close()
    except Exception as err:
        print(err)

class MySpider:
    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre)Gecko/2008072421 Minefield/3.0.2pre"}
    def startUp(self,url,key):
    # Initializing Chrome browser
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        self.driver.get(url)
        keyInput=self.driver.find_element_by_id("key")
        keyInput.send_keys(key)
        keyInput.send_keys(Keys.ENTER)

    def processSpider(self):
        try:
            time.sleep(1)
            print(self.driver.current_url)
            lis =self.driver.find_elements_by_xpath("//div[@id='J_goodsList']//li[@class='gl-item']")
            for li in lis:
                    # We find that the image is either in src or in data-lazy-img attribute
                try:
                    src1 = li.find_element_by_xpath(".//div[@class='p-img']//a//img").get_attribute("src")
                except:
                    src1=""
                try:
                    src2 = li.find_element_by_xpath(".//div[@class='p-img']//a//img").get_attribute("data-lazy-img")
                except:
                    src2=""
                try:
                    price = li.find_element_by_xpath(".//div[@class='p-price']//i").text
                except:
                    price="0"
                try:
                    note = li.find_element_by_xpath(".//div[@class='p-name p-name-type-2']//em").text
                    mark = note.split(" ")[0]
                    mark = mark.replace("爱心东东\n", "")
                    mark = mark.replace(",", "")
                    note = note.replace("爱心东东\n", "")
                    note = note.replace(",", "")
                except:
                    note="11"
                print(src1,src2)
                '''
                try:
                    conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='admin',db='scraping',charset='utf8')
                    cur = conn.cursor()
                    cur.execute("INSERT INTO testmodel_src(src,srce) VALUES(%s,%s)",(src1,src2))
                    cur.close()
                    conn.commit()
                    conn.close()
                except Exception as err:
                    print(err)
                    '''
                insert(mark,price,note,src1,src2)
                
            try:
                self.driver.find_element_by_xpath("//span[@class='p-num']//a[@class='pn-next disabled']")
            except:
                nextPage = self.driver.find_element_by_xpath("//span[@class='p-num']//a[@class='pn-next']")
                nextPage.click()
                self.processSpider()
        except Exception as err:
            print(err)
    def executeSpider(self, url,key):
        starttime = datetime.datetime.now()
        print("Spider starting......")
        self.startUp(url,key)
        self.processSpider()
        print("Spider completed......")
        endtime = datetime.datetime.now()
        elapsed = (endtime - starttime).seconds
        print("Total ", elapsed, " seconds elapsed")


url = "http://www.jd.com"
spider = MySpider()
while True:
    spider.executeSpider(url,"手机")
    break
