# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc

class MokoPostSpider(scrapy.Spider):
    name = "moko_post"
    allowed_domains = ["moko.cc"]
    start_urls = (
        'http://www.moko.cc/',
    )

    def parse(self, response):
    	base_url = get_base_url(response)
        for sel in response.xpath('//a'):
        	url = sel.xpath('@href').extract_first().encode('utf-8')
        	real_url = urljoin_rfc(base_url, url)
        	
