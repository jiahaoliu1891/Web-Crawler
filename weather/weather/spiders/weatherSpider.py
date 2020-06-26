import scrapy
from weather.items import weatherItem


def refineDate(preDate):
    """
    26日（今天） -->  26日
    """
    return preDate[0:-4]


class weatherSpider(scrapy.spiders.Spider):
    name = "weather"
    allowed_domains = ["weather.com"]
    start_urls = (
       "http://www.weather.com.cn/weather/101020100.shtml", 
        "http://www.weather.com.cn/weather/101210101.shtml",
        "http://www.weather.com.cn/weather/101010100.shtml",
        "http://www.weather.com.cn/weather/101190101.shtml",
        "http://www.weather.com.cn/weather/101280101.shtml",
        "http://www.weather.com.cn/weather/101280601.shtml",
        "http://www.weather.com.cn/weather/101190401.shtml",
        "http://www.weather.com.cn/weather/101280601.shtml",
        "http://www.weather.com.cn/weather/101230201.shtml",
        "http://www.weather.com.cn/weather/101220101.shtml"
    )

    def parse(self, response):
        """
        with open("tmp.html", 'wb') as f:
            f.write(response.body)
        """
        items = []
        # city
        city = response.xpath("//div[@class='crumbs fl']/a")[-1].xpath("text()").extract()[0]
        # weather
        for each in response.xpath("//li[contains(@class,'sky skyid lv')]"):
            item = weatherItem()
            date = each.xpath('h1/text()').extract()[0]
            temper = each.xpath("p[@class='tem']/i/text()").extract()[0][0:-1]
            #humidity = each.xpath('').extract()
            windSpeed = each.xpath("p[@class='win']/i/text()").extract()[0]
            weather = each.xpath("p[@class='wea']/text()").extract()[0]
            #rainProb = each.xpath('').extract()

            item['city'] = city
            item['date'] = refineDate(date)
            item['temper'] = temper
            item['windSpeed'] = windSpeed
            item['weather'] = weather
            items.append(item)

        return items



