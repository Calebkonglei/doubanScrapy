# from scrapy.contrib.spiders import CrawlSpider, Rule
# from doubanScrapy.items import DoubanscrapyItem  
# from scrapy.loader import ItemLoader
# from scrapy.linkextractors import LinkExtractor

# class Doubanscrapy(CrawlSpider):
# 	"""docstring for Doubanscrapy"""
# 	name = 'douban_movie'
# 	allowed_domains = ["douban.com"]
# 	start_urls = [
# 		"https://movie.douban.com/top250"
# 	]
# 	rules = [
# 		Rule(LinkExtractor(allow=(r"https://movie.douban.com/top250")), callback = "parse"),	
# 	]

# 	def parse(self, response):
# 		for msg in response.xpath('//div[@class="item"]'):
# 			item = DoubanscrapyItem()
# 			item[url] = msg.xpath('div[@class="pic"]/a/@href').extract()
# 			item[rank] = msg.xpath('div[@class="pic"]/em/text()')
# 			item[movie_name] = msg.xpath('div[@class="pic"]/a/@alt').extract()
# 			item[price] = msg.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')
# 			item[comment] = msg.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()')
# 		return item
# 		# 	yield item

# 		# next_page = response.xpath('//span[@class="next"]/a/@href').extract_first()

# 		# if next_page is not None:
# 		# 	request_url = response.urljoin(next_page)
# 		# 	yield scrapy.Request(request_url, self.parse)
# 		