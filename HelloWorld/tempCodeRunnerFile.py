def forecastCity(self,city):
    if city not in self.cityCode.keys():
        print (city+"code cannot be found")
        return

    url="http://www.weather.com.cn/weather/"+self.cityCode[city]+".shtml"
    try:
        req = urllib.request.Request(url,headers=self.headers)
        data = urllib.request.urlopen(req)
        data = data.read()
        dammit = UnicodeDammit(data,["utf-8","gbk"])
        data = dammit.unicode_markup
        soup = BeautifulSoup(data,"lxml")
        lis = soup.select("ul[class='t clearfix'] li")
        for li in lis:
            try:
                date = li.select('h1')[0].text
                weather = li.select('p[class="wea"]')[0].text
                temp = li.select('p[class="tem"] span')[0].text + "/" + li.select('p[class="tem"] i')[0].text
                print(city,date,weather,temp)
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)