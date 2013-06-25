# -*- coding: utf-8 -*-

class ItemUpdaterFactory(object):
    aged_brie = "Aged Brie"
    sulfuras = "Sulfuras, Hand of Ragnaros"
    backstage = "Backstage passes to a TAFKAL80ETC concert"

    @classmethod
    def is_sulfuras(cls, item):
        return item.name == cls.sulfuras

    @classmethod
    def is_aged_brie(cls, item):
        return item.name == cls.aged_brie

    @classmethod
    def is_backstage(cls,item):
        return item.name == cls.backstage

    @classmethod
    def create(cls, item):
        pass


class GildedRose(object):

    max_quality = 50
    
    days_threshold_min = 10
    days_threshold_max = 5

    def __init__(self, items):
        self.items = items

    def is_sulfuras(self, item):
        return ItemUpdaterFactory.is_sulfuras(item)

    def is_aged_brie(self, item):
        return ItemUpdaterFactory.is_aged_brie(item)

    def is_backstage(self, item):
        return ItemUpdaterFactory.is_backstage(item)

    def decrease_quality(self, item):
        if item.quality > 0:
                item.quality = item.quality - 1

    def reset_quality(self, item):
        item.quality = 0

    def increase_quality(self, item):
        if item.quality < self.max_quality:
                item.quality = item.quality + 1

    def decrease_sell_in(self, item):
        item.sell_in = item.sell_in - 1

    def update_backstage_quality(self, item):
        if self.is_backstage(item):
            if item.sell_in <= self.days_threshold_min:
                self.increase_quality(item)
            if item.sell_in <= self.days_threshold_max:
                self.increase_quality(item)

    def update_item_quality(self, item):
        if self.is_aged_brie(item) or self.is_backstage(item):
            self.increase_quality(item)
            self.update_backstage_quality(item)
        else:
            self.decrease_quality(item)
        
        self.decrease_sell_in(item)

        if item.sell_in < 0:
            if self.is_aged_brie(item):
                self.increase_quality(item)
            elif self.is_backstage(item):
                self.reset_quality(item)
            else:
                self.decrease_quality(item)

    def update_quality(self):
        for item in self.items:
            if not self.is_sulfuras(item):
                self.update_item_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
