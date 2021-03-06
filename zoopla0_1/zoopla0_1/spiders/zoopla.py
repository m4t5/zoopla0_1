from scrapy.selector import Selector
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from zoopla0_1.items import Zoopla01Item

class ZooplaSpider(CrawlSpider):
    name = 'zoopla'
    allowed_domains = ['zoopla.co.uk']
    start_urls = ['http://www.zoopla.co.uk/for-sale/property/leicester/?include_retirement_homes=false&include_shared_ownership=false&new_homes=include&q=leicester&results_sort=lowest_price&page_size=10&pn=1']


    '''
    Root search page (leicester)
    http://www.zoopla.co.uk/for-sale/property/leicester/?page_size=10&q=leicester&new_homes=include&results_sort=lowest_price&radius=0&pn=6

    Property details
    allow
    http://www.zoopla.co.uk/for-sale/details/37029463?search_identifier=e8afc4c50465cb273f7aec21c2a4d97c


    deny
    http://www.zoopla.co.uk/for-sale/details/37188576?featured=1&utm_content=featured_listing
    '''

    rules = (
        Rule(LinkExtractor(allow=r'for-sale\/details\/\d+\?search_identifier=.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = Zoopla01Item()
        item['itemId'] = response.xpath('descendant-or-self::li/@data-listing-id').extract()
        item['address'] = response.xpath('//span[@itemprop="address"]/a[@href]/text()').extract()
        return item 
