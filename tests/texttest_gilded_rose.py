# -*- coding: utf-8 -*-
import os
import sys
parentDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parentDir)
from gilded_rose import GildedRose


class GildedRoseTextTest(object):
    def __init__(self, items):
        self.items = items
        self.GildedRose = GildedRose(self.items)

    def run(self, days):
        self.printHead()
        for day in range(days):
            self.printDay(day)
            self.next_day()

    def next_day(self):
        self.GildedRose.update_quality()

    def printDay(self, day):
        print "-------- day %s --------" % day
        print "name, sellIn, quality"
        for item in self.items:
            print item
        print

    def printHead(self):
        print "OMGHAI!"
