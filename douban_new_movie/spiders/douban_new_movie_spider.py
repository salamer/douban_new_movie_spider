from scrapy.spiders import Spider
from scrapy.selector import Selector

from douban_new_movie.items import DoubanNewMovieItem

class DoubanNewMovieSpider(Spider):
	name="douban_new_movie_spider"

	allowed_domains=["www.movie.douban.com"]

	start_urls=[
		'http://movie.douban.com/chart'
	]

	def parse(self,response):
		sel=Selector(response)

#		movie_name=sel.xpath("//div[@class='wrapper']/div[@class='content']/div[@class='clearfix']/div[@class='indent']/div/table/tbody/tr[@class='item']/td[@valign='top']/div[@class='pl2']/a/text()").extract()
		movie_name=sel.xpath("//div[@class='pl2']/a/text()").extract()
		movie_url=sel.xpath("//div[@class='pl2']/a/@href").extract()
		movie_star=sel.xpath("//div[@class='pl2']/div/span[@class='rating_nums']/text()").extract()

#		//*[@id="content"]/div/div[1]/div/div/table[1]/tbody/tr/td[2]/div/a
#		//*[@id="content"]/div/div[1]/div/div/table[2]/tbody/tr/td[2]/div/a
		item=DoubanNewMovieItem()

		item['movie_name']=[n.encode('utf-8') for n in movie_name]
		item['movie_star']=[n for n in movie_star]
		item['movie_url']=[n for n in movie_url]

		yield item

		print movie_name,movie_star,movie_url