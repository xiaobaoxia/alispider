# -*- coding: utf-8 -*-

import scrapy, json
import re
import sys
from alibaba.items import AlibabaItem
reload(sys)
sys.setdefaultencoding("utf-8")


class AliSpider(scrapy.Spider):
    name = 'ali'
    allowed_domains = ['1688.com']
    start_urls = ['https://dcms.1688.com/open/query.json?resourceId=405457&dataId=236']
    cookies = {
    '_bl_uid':'hhjanbj3r2jum8h05rqp415nqep6',
    ' __sw_newuno_count__':'1',
    ' JSESSIONID':'8L78KCuu1-2lnY1rZWwEHMrgy3tB-DibbAfQ-U28k2',
    ' UM_distinctid':'160a0af003f82a-07f24a15cb5128-16386656-13c680-160a0af0040800',
    ' ali_ab':'14.130.112.43.1514524299165.0',
    ' cna':'i7zMEmbzkzsCAQ6CcCu/rrhj',
    ' alisw':'swIs1200%3D1%7C',
    ' cookie2':'183f3a5d42f38037992e2f2dfc247793',
    ' t':'7f6e962937ec065c8842e087244147ce',
    ' _tb_token_':'cb9efcbecc193',
    ' __cn_logon__':'true',
    ' __cn_logon_id__':'%E8%AF%B7%E5%8F%AB%E6%88%91%E4%B8%81%E8%90%8C%E8%90%8C',
    ' ali_apache_track':'"c_ms=1|c_mid=b2b-2090139374|c_lid=%E8%AF%B7%E5%8F%AB%E6%88%91%E4%B8%81%E8%90%8C%E8%90%8C"',
    ' ali_apache_tracktmp':'"c_w_signed=Y"',
    ' cn_tmp':'"Z28mC+GqtZ2d50/9KWYHvx9RKh+3FppbipmQDS1QEctm0mFHnnzBB/A5TSVl8l4eet4318IxeOpuhMkExUU+9FnKd8y4FpT1+vwdHkRv0J+emWWTTs4QLQBsucL93Ou0War1LFoMmyWXtPkDWH8eqdv8CgciuVWqUgFgQfjxKSdPKf7AnZ5Mrm3Ps3+XQmt64gHoP6pu4/ftOuP+Kkfc+7ZeCGhjX6ky3qihh8xpdBrNgYNgR7gVVf2hLJjgT95E"',
    ' _cn_slid_':'"GK0hmyV%2FAj"',
    ' tbsnid':'c9qJhupw3WIr9fIE4gDWIQVkLeEG4cZXKHuo8a4iBTQ6sOlEpJKl9g%3D%3D',
    ' LoginUmid':'"QQ7XmLzwGJ6u5o%2BSWdL7oLuU6yCxJSdPbr6VBxU0jnoogBSl%2FbuCDg%3D%3D"',
    ' userID':'"JaCKZywO%2BacHNIO%2BsAOtURoj2UuMHOwZzuM%2BCORwF3I6sOlEpJKl9g%3D%3D"',
    ' last_mid':'b2b-2090139374',
    ' __last_loginid__':'"%E8%AF%B7%E5%8F%AB%E6%88%91%E4%B8%81%E8%90%8C%E8%90%8C"',
    ' _csrf_token':'1514549649412',
    ' h_keys':'"%u7eff%u8336#%u7eb1%u7ebf"',
    ' userIDNum':'"WpETjrD4DJXxC0EBmttZ0Q%3D%3D"',
    ' alicnweb':'homeIdttS%3D83587493878907318813853460950243548445%7ChomeIdttSAction%3Dtrue%7Chp_newbuyerguide%3Dtrue%7Ctouch_tb_at%3D1514560965380%7Clastlogonid%3D%25E8%25AF%25B7%25E5%258F%25AB%25E6%2588%2591%25E4%25B8%2581%25E8%2590%258C%25E8%2590%258C%7Cshow_inter_tips%3Dfalse',
    ' ad_prefer':'"2017/12/29 23:55:06"',
    ' _tmp_ck_0':'"7cwO7li88Ou0ZQAlVK%2BCjQoI7euLfJCkXzshW%2BpyEf7NhoYQ0VbESRwtfRXMvxLqSNmRRbxYyuOz8rP9G8EXax2cFZohPmOKLP7Vt7rsnNYGXyyOMMaIQfPwFBuiwJd%2FdYmHB%2FAqvqz2uPPcTBNLwWz12Gr80C99F0zpDNCvRcljIL89w%2FINL%2F4IrSk2R8F2rRA9EuvrqXxFS6MeYqxIpvndXDBrI7CebFdCnW2dyiYb%2BcEd7GwZlaEZmljeV2Qde5TiqLJYkYqGXz3kNwL3phAcChQbMhhz%2FNNMtRsyzZiw6esJ%2B%2BGWzLeGqWu7Z4zTOdiqhcYSsdm1I8FGBoxNJQMquk7MlgSVxb9PDCQpl7g1ErAuCsdwazd6540e%2FADOHR2B98%2BMoMMZpNbY7hw6jlYTpJoZ5nt10mMxfhCkRa%2Fs9xIwVVM7V0STKey2LXgN3kcv6KOUTuvigUdLdDjvuPShe8KDQmfsKheoDcQ%2BJzD7i7zB92r0QqAVeSHZc2CgW%2B8K6jpH2kW%2BSIAlQ8Epxw%3D%3D"',
    ' isg':'Avz8C4BXism0_74X91h5esigzZxuXaEbyapDM9Z9SufUoZwr_gVwr3Lb9f8i'
    }

    headers_first = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	':authority':'www.1688.com',
	'Upgrade-Insecure-Requests':'1',
	':method':'GET',
	':scheme':'https'}

    headers_secend = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Cache-Control':'max-age=0',
	'Connection':'keep-alive',
	':authority':'www.1688.com',
	'Upgrade-Insecure-Requests':'1',
	':method':'GET',
	':scheme':'https'}

    def parse(self, response):

        pattern = re.compile(r'\\"(https://s\.1688\.com/selloffer/offer_search\.htm.*?)\\"')
        print pattern.findall(response.body)

        for url in pattern.findall(response.body):
        	self.headers_first[':path'] = url.replace('https://s.1688.com', '')
        	self.headers_first['referer'] = 'https://www.1688.com/'
        	# new_url = re.sub(r'spm=a260k.635.1998214977.14.5Wm1tI&uniqfield=pic_tag_id', 'descendOrder=true&sortType=va_rmdarkgmv30&uniqfield=userid', url)
        	yield scrapy.Request(url=url, cookies=self.cookies, meta={'referer':url}, callback=self.parse_classify, headers=self.headers_first)
    

    def parse_classify(self, response):
    	# print response.xpath
    	good_urls = response.xpath('//*[starts-with(@id,"offer")]/div[2]/div[3]/a/@href').extract()
    	for good_url in good_urls:
    		self.headers_secend['referer'] = response.meta['referer']
    		self.headers_secend[':path'] = good_url.replace('https://s.1688.com', '')

    		yield scrapy.Request(url=good_url, headers=self.headers_secend, cookies=self.cookies, callback=self.parse_item)


    def parse_item(self, response):
    	item = AlibabaItem()
        # 获取不同页面的最低价格

        if response.xpath(
                '//*[@id="mod-detail-price"]/div/table/tbody/tr[1]/td[2]/span[2]/text()').extract_first():

            item['unit'] = ''.join(response.xpath('//*[@id="mod-detail-price"]/div/table/tbody/tr[2]/td/span/text()').extract())

            item['price'] = response.xpath(
                '//*[@id="mod-detail-price"]/div/table/tbody/tr[1]/td[2]/span[2]/text()').extract_first()
        else:
            item['price'] = response.xpath(
                '//*[@id="mod-detail-price"]/div/table/tbody/tr[1]/td[2]/div[1]/span[2]/text()').extract_first()
            item['unit'] = ''.join(
                response.xpath('//*[@id="mod-detail-price"]/div/table/tbody/tr[2]/td/span/text()').extract())

        item['sales'] = response.xpath('//*[@id="mod-detail-bd"]/div[2]/div[9]/div/div/div[2]/p/a/em/text()').extract()[0]
        item['comment'] = response.xpath('//*[@id="mod-detail-bd"]/div[2]/div[9]/div/div/div[2]/p/a/em/text()').extract()[1]
        item['area'] = response.xpath('//*[@id="mod-detail-bd"]/div[2]/div[8]/div/div/div[2]/div[1]/p[1]/span/text()').extract_first()
        item['name'] = response.xpath('//*[@id="mod-detail-title"]/h1/text()').extract_first()
        index = 0
        details = []
        while True:
            try:
                details.append({response.xpath('//*[@id="mod-detail-attributes"]/div[1]/table/tbody/tr/td[@class="de-feature"]/text()').extract()[index]:response.xpath('//*[@id="mod-detail-attributes"]/div[1]/table/tbody/tr/td[@class="de-value"]/text()').extract()[index]})
            except Exception as e:
                break
            index += 1
            if index == 40:
                break

        item['detail'] = details
        item['img_url'] = response.xpath('//*[@id="mod-detail-bd"]/div[1]/div/div/div/div/div[1]/div/a/img/@src').extract_first()

        yield item
















