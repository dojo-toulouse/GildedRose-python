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
        if cls.is_aged_brie(item):
            return AgedBrieUpdater(item)
        if cls.is_backstage(item):
            return BackStageUpdater(item)
        if cls.is_sulfuras(item):
            return SulfurasUpdater(item)
        return DefaultUpdater(item)


class DefaultUpdater(object):
    max_quality = 50

    def __init__(self, item):
        self.item = item

    def increase_quality(self):
        if self.item.quality < self.max_quality:
            self.item.quality = self.item.quality + 1

    def update_quality(self):
        pass


class AgedBrieUpdater(DefaultUpdater):
    def update_quality(self):
        pass

class BackStageUpdater(DefaultUpdater):
    pass


class SulfurasUpdater(DefaultUpdater):
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
        self.increase_quality(item)
        if item.sell_in <= self.days_threshold_min:
            self.increase_quality(item)
        if item.sell_in <= self.days_threshold_max:
            self.increase_quality(item)
        self.decrease_sell_in(item)
        if item.sell_in < 0:
            self.reset_quality(item)

    def update_aged_brie(self, item):
        self.increase_quality(item)
        self.decrease_sell_in(item)
        if item.sell_in < 0:
            self.increase_quality(item)

    def update_item_quality(self, item):
        if self.is_aged_brie(item):
            self.update_aged_brie(item)
        else:
            if self.is_backstage(item):
                self.update_backstage_quality(item)
            else:
                self.decrease_quality(item)
                self.decrease_sell_in(item)

                if item.sell_in < 0:
                    self.decrease_quality(item)

    def update_quality(self):
        for item in self.items:
            itemUpdater = ItemUpdaterFactory.create(item)
            if not self.is_sulfuras(item):
                self.update_item_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
