# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from shiyanlougithub.models import Repository,engine
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ShiyanlougithubPipeline(object):
    def process_item(self, item, spider):
        item['commits'] = int(''.join(item['commits'].split(',')))
        item['branches'] = int(item['branches'])
        item['releases'] = int(item['releases'])
        self.session.add(Repository(**item))
        return item

    def open_spider(self,spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()
    
    def close_spider(self,spider):
        self.session.commit()
        self.session.close()
