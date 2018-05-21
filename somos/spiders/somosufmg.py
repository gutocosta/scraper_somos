# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
import scrapy
from somos.items import Prof


class SomosUfmgSpider(CrawlSpider):
    #aqui e definido o nome da spider que sera chamado pelo comando "scrapy crawl -o output.xml NOME_DA_SPIDER"
    name = 'somosufmg'
    #e definido a url que sera de inicio, ou seja, a pagina principal do site
    #start_urls = ['http://www1.folha.uol.com.br/']

    #as regras sao estabelecidas para restringir o scrapy aos links do cabecalho
    #rules = [
     #   Rule(LinkExtractor(restrict_xpaths= '//div[@class="l-header__nav c-site-nav"]'), callback= 'parse_sec'),
    #]
    
    def start_requests(self):
    	for x in range(1, 4000):
        	yield scrapy.Request("http://somos.ufmg.br/professores/view/%d" % (x),self.parse_item)

    def parse_item(self, response):
        litem = []
        i = Prof()
        litem.append(response.xpath('//div[@class="span8"]/h2/text()').extract_first())
        desc = response.xpath('//div[@class="span6 cloud palavrasChave"]/a')
        for item in desc:
        	litem.append(item.xpath('./span/text()').extract_first())

        i['content'] = ",".join(litem)

        yield i



        