# -*- coding: utf-8 -*-
import scrapy


class MokoSpiderSpider(scrapy.Spider):
    name = "moko_spider"
    allowed_domains = ["moko.cc"]
    start_urls = (
        'http://www.moko.cc/post/1167806.html',
        'http://www.moko.cc/post/1167769.html',
    )

    def parse(self, response):
    	imgArr = []
        for sel in response.xpath('//div[@class="pic dBd"]'):
        	imgSrc = sel.xpath('p/img/@src2').extract_first().encode('utf-8')
        	imgArr.append(imgSrc)
        # return a dict with image_urls ,will call image downloaders
        return {'image_urls':imgArr}
