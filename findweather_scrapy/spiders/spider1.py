import scrapy
from ..items import FindweatherScrapyItem


def date_list(start, end):
    """

    :param start: year start; format: 2017, int
    :param end: year end; format: 2019, int
    :return: a list include all the month
    """

    assert int(start / 1000) == 0 or type(start) is int, 'start error'
    assert int(end / 1000) == 0 or type(end) is int, 'end error'

    result = []
    years = end - start + 1
    for year in range(years):
        for i in range(12):
            result.append((start + year) * 100 + i + 1)
    return result


months = date_list(2017, 2018)


class WeatherSpider(scrapy.Spider):
    name = "weather"

    def start_requests(self):
        city = 'chengdu'
        url_model = 'http://www.tianqihoubao.com/lishi/{}/month/{}.html'
        urls = [url_model.format(city, month) for month in months]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        rows = response.xpath('//table/tr')
        for i, row in enumerate(rows):
            columns = row.xpath('td')
            if i == 0:
                pass
            else:
                [date, statu, temperature, wind] = columns
                item = FindweatherScrapyItem()
                item['date'] = date.xpath('normalize-space()').get()
                item['statu'] = statu.xpath('normalize-space()').get()
                item['temperature'] = temperature.xpath('normalize-space()').get()
                item['wind'] = wind.xpath('normalize-space()').get()
                # yield {
                #     'date': date,
                #     'statu': statu,
                #     'temperature': temperature,
                #     'wind': wind
                # }
                yield item

