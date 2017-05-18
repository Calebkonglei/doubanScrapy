from scrapy import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from doubanScrapy.items import DoubanscrapyItem  
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor

class DoubanScrapy(CrawlSpider):
	"""docstring for DoubanScrapy"""
	name = 'douban'
	start_urls = ["https://movie.douban.com/top250"]

	#定义抓取规则
	rules = [
		Rule(LinkExtractor(allow = (r"https://movie.douban.com/top250\?start=\d+\&filter=")), callback = 'parse'),
		Rule(LinkExtractor(allow = (r"https://movie.douban.com/top250")), follow = True)	
	]

	def parse(self, response):
		for msg in response.xpath('//div[@class="item"]'):
			item = DoubanscrapyItem()
			item['url'] = msg.xpath('div[@class="pic"]/a/@href').extract()[0]
			item['rank'] = msg.xpath('div[@class="pic"]/em/text()').extract()[0]
			item['movie_name'] = msg.xpath('div[@class="pic"]/a/img/@alt').extract()[0]
			item['price'] = msg.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
			comment = msg.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
			if comment:
				item['comment'] = comment[0]

			yield item

		next_page = response.xpath('//span[@class="next"]/a/@href').extract_first()

		if next_page:
			request_url = response.urljoin(next_page)
			print (request_url)
			yield Request(request_url, callback = self.parse)
		