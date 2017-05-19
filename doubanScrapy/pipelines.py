# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class DoubanscrapyPipeline(object):
    def process_item(self, item, spider):
    	
    	with open('D:/workspace4/doubanScrapy/douban_movie.json', 'at') as f:
    		f.write('url:' + item['url'] + '\n')
        # return item
