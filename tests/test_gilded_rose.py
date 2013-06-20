# -*- coding: utf-8 -*-
import os
import sys
from copy import deepcopy
import unittest
parentDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parentDir)

from gilded_rose import GildedRose
from fixture import items


class GildedRoseTest(unittest.TestCase):
    def setUp(self):
        self.items = deepcopy(items)  # deepcopy fixture because of tests isolation
        self.basicItem = self.items[0]
        self.AgedBrie = self.items[1]
        self.SulfurasItem = self.items[3]
        self.BackstagePass = self.items[5]

    def test_item_as_a_sellIn_value(self):
        self.assertTrue(hasattr(self.basicItem, 'sell_in'))

    def test_item_as_a_quality_value(self):
        self.assertTrue(hasattr(self.basicItem, 'quality'))

    def test_item_quality_decreases_each_day(self):
        self._assertQualityDecreasesBy(self.basicItem)

    def test_item_sellIn_decreases_each_day(self):
        self._assertSellInDecreasesBy(self.basicItem)

    def test_once_the_sell_by_date_passed_quality_degrades_twice(self):
        self._go_to_last_sellIn_date(self.basicItem)
        self._assertQualityDecreasesBy(self.basicItem, 2)

    def test_quality_is_never_negative(self):
        self._deacreases_to_lowest_quality(self.basicItem)
        self._assertQualityDecreasesBy(self.basicItem, 0)

    def test_agedBrie_quality_increases_each_day(self):
        self._assertQualityIncreasesBy(self.AgedBrie, 1)

    def test_quality_is_never_more_than_50(self):
        self._increases_to_highest_quality(self.AgedBrie)
        self._assertQualityIncreasesBy(self.AgedBrie, 0)

    def test_Sulfuras_never_has_to_be_sold(self):
        self._assertSellInDecreasesBy(self.SulfurasItem, 0)

    def test_Sulfuras_never_decreases_in_quality(self):
        self._go_to_last_sellIn_date(self.SulfurasItem)
        self._assertQualityDecreasesBy(self.SulfurasItem, 0)

    def test_BackStage_pass_quality_increases_each_day(self):
        self._assertQualityIncreasesBy(self.BackstagePass, 1)

    def test_BackStage_pass_quality_increases_by_2_after_10_days_before_concert(self):
        self._go_10_days_before_concert(self.BackstagePass)
        self._assertQualityIncreasesBy(self.BackstagePass, 2)

    def test_BackStage_pass_quality_increases_by_3_after_5_days_before_concert(self):
        self._go_5_days_before_concert(self.BackstagePass)
        self._assertQualityIncreasesBy(self.BackstagePass, 3)

    def test_BackStage_pass_quality_drops_to_0_after_concert(self):
        self._go_to_last_sellIn_date(self.BackstagePass)
        self._update_quality_of(self.BackstagePass)
        self.assertEquals(0, self.BackstagePass.quality)

# Assertions :
    def _assertQualityIncreasesBy(self, item, gain=1):
        oldQuality = item.quality
        self._update_quality_of(item)
        self.assertEquals(oldQuality, item.quality - gain)

    def _assertQualityDecreasesBy(self, item, loss=1):
        oldQuality = item.quality
        self._update_quality_of(item)
        self.assertEquals(oldQuality, item.quality + loss)

    def _assertSellInDecreasesBy(self, item, loss=1):
        oldSellIn = item.sell_in
        self._update_quality_of(item)
        self.assertEquals(oldSellIn, item.sell_in + loss)

# Hide GildedRose usage :
    def _update_quality_of(self, *items):
        GildedRose(items).update_quality()

# Predefined properties setting :
    def _go_to_last_sellIn_date(self, item):
        item.sell_in = 0

    def _go_10_days_before_concert(self, item):
        item.sell_in = 10

    def _go_5_days_before_concert(self, item):
        item.sell_in = 5

    def _deacreases_to_lowest_quality(self, item):
        item.quality = 0

    def _increases_to_highest_quality(self, item):
        item.quality = 50

if __name__ == '__main__':
    unittest.main()
