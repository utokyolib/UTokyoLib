import unittest

import library


class TestLibraryMethods(unittest.TestCase):

    # 総合図書館
    def test_sogo(self):
        self.assertEqual(
            ("本館休館(平日)", "別館(Annex) 8:30-22:30 ※本学在籍者のみ利用可 / UTokyo Members Only"),
            library.fetch_opening_info(100001, year=2020, month=9, day=24)
        )

    # 駒場図書館
    def test_komaba(self):
        self.assertEqual(
            ("短縮開館（本学在籍者のみ）", "10:00-20:00"),
            library.fetch_opening_info(300300, year=2020, month=9, day=24)
        )

    # 柏図書館
    def test_kashiwa(self):
        self.assertEqual(
            ("短縮開館(本学在籍者のみ利用可)", "9:00-17:00"),
            library.fetch_opening_info(500840, year=2020, month=9, day=24)
        )