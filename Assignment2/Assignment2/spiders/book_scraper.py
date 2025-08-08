import scrapy
from ..items import Assignment2Item

class BookSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        'http://books.toscrape.com',
    ]
    def parse(self, response):
        all_books=response.css("article.product_pod")
        for book in all_books:
            items= Assignment2Item()
            items['name']=book.css("h3 a::attr(title)").get()# Extracting book name from h3  html tag 
            items['rating_of_book']=book.css("p.star-rating::attr(class)").get().replace("star-rating ", "")# extracting rating from p html tag of class star-rating
            items['availbility_of_book']= " ".join(book.css(".availability::text").getall()).strip()
            #book availability from id availability
            items['price_of_book']=book.css(".price_color::text").get()
            # Extracting price from class price_color
            items['bookimage_url']= book.css("img::attr(src)").get()
            yield items
        next_page_book=response.css("li.next a::attr(href)").get() # next page element from the next button at the bottom of the page 
        if next_page_book is not None: # if it is not nom then we call the function again 
            yield response.follow(next_page_book, callback=self.parse)
