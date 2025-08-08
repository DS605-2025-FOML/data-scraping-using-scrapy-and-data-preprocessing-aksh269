import scrapy
from ..items import Lab02ScraperItem

class QuotesSpider(scrapy.Spider):
  name = "quotes"
  start_urls = [
    'http://quotes.toscrape.com/page/1/',
  ]

  def parse(self,response):
    all_div_quotes=response.css('div.quote')


    item=Lab02ScraperItem()

    for quote_div in all_div_quotes:
      text=quote_div.css('span.text::text').extract_first()
      author=quote_div.css('.author::text').extract_first()
      tags=quote_div.css('.tag::text').extract()


      item['text']=text
      item['author']=author
      item['tag']=tags

      yield item

    next_page=response.css('li.next a::attr(href)').get()

    if next_page is not None:
      yield response.follow(next_page,callback=self.parse)