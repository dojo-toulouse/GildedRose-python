# -*- coding: utf-8 -*-

if __name__ == "__main__":
    import sys
    from tests.fixture import items
    from tests.texttest_gilded_rose import GildedRoseTextTest

    days = 2
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1

    GildedRoseTextTest(items).run(days)
