import scrapy
import urllib
from amazon.items import AmazonItem
import os


class amazonSpider(scrapy.Spider):
    imgcount = 1
    name = "amazon"
    allowed_domains = ["amazon.com"]
    
    start_urls = ["https://www.amazon.com/gp/search/ref=a9_asi_1?rh=i%3Aaps%2Ck%3Aoculus+rift&keywords=oculus+rift&ie=UTF8&qid=1477188748",
	
	]
    
    def parse(self,response):
        costlist = response.xpath('.//*[starts-with(@id,"result_")]/ul/li[1]/div/a/span/text()').extract()
        namelist = response.xpath('//a[@class="a-link-normal s-access-detail-page s-overflow-ellipsis a-text-normal"]/@title').extract()
        htmllist = response.xpath('//a[@class="a-link-normal s-access-detail-page s-overflow-ellipsis a-text-normal"]/@href').extract()
        imglist = response.xpath('//img[@class="s-access-image cfMarker"]/@src').extract()
        listlength = len(namelist)

        pwd = os.getcwd()+'/'

        if not os.path.isdir(pwd+'crawlImages/'):
            os.mkdir(pwd+'crawlImages/')

        for i in range(0,listlength):
            item = AmazonItem()
            item['Name'] = namelist[i]
            item['Source'] = htmllist[i]
            item['Cost'] = costlist[i]
        
            urllib.urlretrieve(imglist[i],pwd+"crawlImages/"+str(amazonSpider.imgcount)+".jpg")
            item['Path'] = pwd+"crawlImages/"+str(amazonSpider.imgcount)+".jpg"
            amazonSpider.imgcount = amazonSpider.imgcount + 1
            yield item
