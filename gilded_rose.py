# -*- coding: utf-8 -*-


class GildedRose(object):

    max_quality = 50
    aged_brie = "Aged Brie"


    def __init__(self, items):
        self.items = items

    def is_aged_brie(self, item):
        return item.name == self.aged_brie  

    def is_backstage(self,item):
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def decrease_quality(self, item):
        if item.quality > 0:
                item.quality = item.quality - 1

    def increase_quality(self, item):
        if item.quality < self.max_quality:
                item.quality = item.quality + 1

    def update_backstage_quality(self, item):
        if self.is_backstage(item):
            if item.sell_in < 11:
                self.increase_quality(item)
            if item.sell_in < 6:
                self.increase_quality(item)

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            if not self.is_aged_brie(item) and not self.is_backstage(item):
                self.decrease_quality(item)
            else:
                self.increase_quality(item)
                self.update_backstage_quality(item)
            
            item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                if not self.is_aged_brie(item):
                    if not self.is_backstage(item):
                        self.decrease_quality(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    self.increase_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
