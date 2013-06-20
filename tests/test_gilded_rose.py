# -*- coding: utf-8 -*-
import unittest
import os
import sys
parentDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parentDir)
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

if __name__ == '__main__':
    unittest.main()
