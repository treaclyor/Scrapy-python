import scrapy
from scrapy import Request

from lianjia.items import LianjiaItem


class DemoSpider(scrapy.Spider):
    name = "demo"  # 爬虫名称
    #用户代理
    headers  ={
        'USER-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }

    def start_requests(self):
        #url = 'https://dl.lianjia.com/ershoufang/'  # URL列表
        #url = 'https://bj.lianjia.com/ershoufang/'
        #url = 'https://cc.lianjia.com/ershoufang/'
        #url = 'https://cs.lianjia.com/ershoufang/'
        #url = 'https://cd.lianjia.com/ershoufang/'
        #url = 'https://sz.lianjia.com/ershoufang/'
        #url = 'https://sh.lianjia.com/ershoufang/'
        #url = 'https://nj.lianjia.com/ershoufang/'
        #url = 'https://sy.lianjia.com/ershoufang/'
        url = 'https://xm.lianjia.com/ershoufang/'

        yield  Request(url, headers=self.headers)

    def parse(self, response):
        item = LianjiaItem()
        #使用xpath语法
        for info in response.xpath('//ul[@class="sellListContent"]/li'):
            # 获取地点

            price = str(info.xpath('./div[@class="info clear"]/div[@class="priceInfo"]/div[@class="totalPrice"]/span/text()').extract())
            #extract()返回一个SelectorList对象
            item['price'] = self.str_format(price)

            per_price = str(info.xpath('./div[@class="info clear"]/div[@class="priceInfo"]/div[@class="unitPrice"]/span/text()').extract())
            per_price = str(self.str_format(per_price)).split("单价")
            i = 0
            sec_per_price = ''
            for per in per_price:
                i+=1
                if i == 2:
                    sec_per_price = per
            sec_per_price = sec_per_price.split("元/平米")
            item['per_price'] = sec_per_price[0]

            description = str(info.xpath('./div[@class="info clear"]/div[@class="address"]/div[@class="houseInfo"]/text()').extract())
            style = description[2:6]
            item['style'] = style

            house_size = str(self.get_size(description)).split("平米")
            item['house_size'] = house_size[0].strip()

            region = str(info.xpath('./div[@class="info clear"]/div[@class="flood"]/div[@class="positionInfo"]/a[1]/text()').extract())
            item['region'] = self.str_format(region)

            focus = str(info.xpath('./div[@class="info clear"]/div[@class="followInfo"]/text()').extract())
            focus =  self.str_format(focus)

            focus = str(self.get_focus(focus)).split("人关注")
            item['focus'] = focus[0]

            establish_year = str(self.get_establish_year(description)).split("年建")
            item['establish_year'] = establish_year[0].strip()

            item['floor'] = self.get_floor(description)
            yield item  # 返回数据


        for i in range(2, 100):
            #next_page = "https://dl.lianjia.com/ershoufang/pg%s" % str(i)
            #next_page = "https://bj.lianjia.com/ershoufang/pg%s" % str(i)
            #next_page = "https://cc.lianjia.com/ershoufang/pg%s" % str(i)
            #next_page = "https://cs.lianjia.com/ershoufang/pg%s" % str(i)
            #next_page = "https://cd.lianjia.com/ershoufang/pg%s" % str(i)
            #next_page = "https://sz.lianjia.com/ershoufang/pg%s" % str(i)
            #next_page = "https://sh.lianjia.com/ershoufang/pg%s" % str(i)
            #next_page = "https://nj.lianjia.com/ershoufang/pg%s" % str(i)
            #next_page = "https://sy.lianjia.com/ershoufang/pg%s" % str(i)
            next_page = "https://xm.lianjia.com/ershoufang/pg%s" % str(i)

            yield Request(next_page, self.parse)
    #数据处理函数
    def get_establish_year(self,description):
        d_list = description.split('|')
        i = 0
        for year in d_list:
            i+=1
            if i == 6:
                return year
    def get_floor(self,description):
        d_list = description.split('|')
        i = 0
        for floor in d_list:
            i += 1
            if i == 5:
                return floor
    def get_focus(self,focus):
        i = 0
        for str in focus:
            if str == '/':
                return focus[0:i]
            i+=1

    def get_size(self,description):
         i = 0
         j = 0
         for str in description:
             if str == '|':
                 j+=1
             if j == 2:
                 return description[8:i]
             i += 1
    def str_format(self,string_format):
        str_len = len(string_format)
        return string_format[2:str_len-2]

# nodename	选取此节点的所有子节点。
# /	从根节点选取。
# //	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
# .	选取当前节点。
# ..	选取当前节点的父节点。
# @	选取属性。
# bookstore	选取 bookstore 元素的所有子节点。
# /bookstore
# 选取根元素 bookstore。
# 注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！
# bookstore/book	选取属于 bookstore 的子元素的所有 book 元素。
# //book	选取所有 book 子元素，而不管它们在文档中的位置。
# bookstore//book	选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。
# //@lang	选取名为 lang 的所有属性。