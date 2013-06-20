# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import sys
    from ..gilded_rose import GildedRose
    from fixture import items
    days = 2
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1

    print "OMGHAI!"
    for day in range(days):
        print "-------- day %s --------" % day
        print "name, sellIn, quality"
        for item in items:
            print item
        print
        GildedRose(items).update_quality()
