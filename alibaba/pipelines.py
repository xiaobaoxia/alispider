# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo, scrapy, os, logging
from datetime import datetime
from scrapy.pipelines.images import ImagesPipeline
from settings import IMAGES_STORE


class AliImagePipeline(ImagesPipeline):
    # 发送图片请求,保存到settings配置的IMAGE_STORE目录下
    def get_media_requests(self, item, info):
        headers = {
            'upgrade-insecure-requests': 1,
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
        }
        yield scrapy.Request(item['img_url'], headers=headers)

    def item_completed(self, results, item, info):
        # 返回图片的原来的名字字符串
        image_path = [x['path'] for ok, x in results if ok][0]
        # print results
        # 设定好保存图片的路径和文件名

        new_name = IMAGES_STORE + item['name'] + ".jpg"

        item['img_path'] = new_name

        # 将原图片名，修改为新的图片名
        print "**" * 30
        print results
        try:
            os.rename(IMAGES_STORE + image_path, item['img_path'])
        except:
            logging.error("图片已被修改..")

        return item


class AlibabaPipeline(object):
    def open_spider(self, spider):
        db = pymongo.MongoClient('127.0.0.1', 27017).ali
        self.collection = db.item

    def process_item(self, item, spider):
        # 向集合中插入数据
        item['source'] = spider.name
        item['crawl_time'] = str(datetime.utcnow())

        self.collection.insert(dict(item))

        return item
