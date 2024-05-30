from scrapy import Spider
from scrapy.selector import Selector
from tutorial.items import CrawlerItem

class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["thegioididong.com"]
    start_urls = [
        "https://www.thegioididong.com/dtdd/samsung-galaxy-a50",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//li[contains(@class, "par")]')

        for question in questions:
            item = CrawlerItem()

            item['User'] = question.xpath(
                'div[@class="cmt-top"]/p[@class="cmt-top-name"]/text()').extract_first()
            item['Comment'] = question.xpath(
                'div[@class="cmt-content "]/p[@class="cmt-txt"]/text()').extract_first()
            item['Time'] = question.xpath(
                'div[@class="cmt-command"]/span[@class="cmtd dot-line"]/text()').extract_first()

            yield item

        # Tìm liên kết đến trang tiếp theo và theo dõi nó nếu có
        next_page = response.xpath('//a[@class="next"]/@href').extract_first()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield response.follow(next_page_url, self.parse)
