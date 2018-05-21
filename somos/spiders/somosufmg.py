# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
import scrapy
from somos.items import Prof


class SomosUfmgSpider(CrawlSpider):
    #aqui e definido o nome da spider que sera chamado pelo comando "scrapy crawl -o output.xml NOME_DA_SPIDER"
    name = 'somosufmg'
    
    def start_requests(self):
        #inicia-se um loop que percorre todas as paginas da pasta 'professores' 
    	for x in range(1, 4000):
            #a cada pagia e chamada a funcao para parsear o item
        	yield scrapy.Request("http://somos.ufmg.br/professores/view/%d" % (x),self.parse_item)

    def parse_item(self, response):
        # uma lista que recebe todos os elementos do item e criada
        litem = []

        # i e definido como o item Prof cuja classa e definida no arquivo items
        i = Prof()
        #o nome do professor e extraido a partir da sua identificacao na pagina 
        litem.append(response.xpath('//div[@class="span8"]/h2/text()').extract_first())

        #desc recebe todas as palavras chaves listadas na pagina
        desc = response.xpath('//div[@class="span6 cloud palavrasChave"]/a')

        #cada palavra chave presente em desc e extraida 
        for item in desc:
        	litem.append(item.xpath('./span/text()').extract_first())

        #o item Prof recebe a lista convertida para string
        i['content'] = ",".join(litem)

        yield i



        