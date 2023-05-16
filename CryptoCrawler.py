import scrapy
from datetime import datetime
from datetime import date
import pytz

lista = []
completa = []
DadosCrypto = ""
escrever = ""
preco = ""
texto = ""

class MeuItem(scrapy.Item):
    nome = scrapy.Field()
    Preco = scrapy.Field()

class MySpider(scrapy.Spider):
    name = "CryptoCrawler"
    allowed_domains = ['br.financas.yahoo.com']
    start_urls = ["https://br.financas.yahoo.com/criptomoedas/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAB0M38277lIW-gCZPiXeQWwr4ACorCbZUGkIQq6MDedrcYJ6GiAAWnYZ6z8r2KUyHkqSmm4xvOzHbSSj1wrDe1Ye1AmkmMiym_98LKoaQGrO9nvI1NRJATfJh3edV_4D_Mfp5N2iq8583jotpHmG6QuJnYh-5Jg_XGE_vbF3Edvu"]

    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.item_buffer = []

    def parse(self, response): 
        
        body = response.xpath('//div[@class="Ovx(a) Ovx(h)--print Ovy(h) W(100%) "]').getall()
        
        #print(body)
        
        for row in response.xpath('//div[@class="Ovx(a) Ovx(h)--print Ovy(h) W(100%) "]'):
            item = MeuItem()
            
            nome = row.xpath('//td').getall()
            
            #print("Nome : ", nome)
            n=1
            
            fuso_horario_local = pytz.timezone('America/Sao_Paulo')
            hoje = date.today()
            agora = datetime.now(fuso_horario_local)
            hora_minuto = agora.strftime("%H:%M")
            
            while n < len(nome):
                nome[n] = nome[n].replace('<td colspan="" class="Va(m) Ta(start) Px(10px) Fz(s)" aria-label="Nome">', "")
                nome[n] = nome[n].replace('</td>', "")
                nome[n] = nome[n].replace('USD', "")
                print("Nome moneda:",nome[n])
                completa.append(nome[n])
                preco = nome[n+1]
                lista = preco.split(">")
                texto = lista[2].replace("</fin-streamer", "")
                completa.append(texto)
                print("preco :",texto)
                completa.append
                n = n + 12
        x = 0
        while x < len(completa)-1:
            escrever = completa[x] + ";" + completa[x+1] + ";" + str(hoje) + ";" + str(hora_minuto) + ";\r\n"
            with open('CryptoDataSet.csv', 'a+') as f:
                f.write(escrever)
            print(escrever)
            x = x + 2      

                    
                
            
            #adosCrypto = row.getall()

            #print(DadosCrypto)
            
            #self.item_buffer.append(item)

            #yield item
            


