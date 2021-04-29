import unittest

import library


class TestLibraryMethods(unittest.TestCase):

    test_year  = 2021
    test_month = 4
    test_day   = 22

    # 総合図書館
    def test_sogo(self):
        self.assertEqual(
            ("本館休館(平日)", "別館(Annex) 9:00-22:30 ※在籍者のみ"),
            library.fetch_opening_info(100001, year=self.test_year, month=self.test_month, day=self.test_day)
        )

    # 駒場図書館
    def test_komaba(self):
        self.assertEqual(
            ("短縮開館", "10:00-20:00"),
            library.fetch_opening_info(300300, year=self.test_year, month=self.test_month, day=self.test_day)
        )

    # 柏図書館
    def test_kashiwa(self):
        self.assertEqual(
            ("平日", "9:00-21:00"),
            library.fetch_opening_info(500840, year=self.test_year, month=self.test_month, day=self.test_day)
        )