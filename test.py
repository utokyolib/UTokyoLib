import unittest

import library


class TestLibraryMethods(unittest.TestCase):

    # 総合図書館
    def test_sogo(self):
        lib_num = 100001

        self.assertEqual(
            ("平日", "全館(Main and Annex) 9:00-22:30 ※在籍者のみ"),
            library.fetch_opening_info(lib_num, year=2021, month=7, day=1)
        )
        self.assertEqual(
            ("土・日・祝日", "全館(Main and Annex) 9:00-19:00 ※在籍者のみ"),
            library.fetch_opening_info(lib_num, year=2021, month=7, day=22)
        )
        self.assertEqual(
            ("本館休館(平日)", "別館(Annex) 9:00-22:30 ※在籍者のみ"),
            library.fetch_opening_info(lib_num, year=2021, month=7, day=29)
        )
        self.assertEqual(
            ("別館休館(平日)", "本館(Main bldg.) 9:00-22:30 ※在籍者のみ"),
            library.fetch_opening_info(lib_num, year=2021, month=7, day=30)
        )

    # 駒場図書館
    def test_komaba(self):
        lib_num = 300300

        self.assertEqual(
            ("短縮開館", "10:00-20:00"),
            library.fetch_opening_info(lib_num, year=2021, month=7, day=1)
        )
        self.assertEqual(
            ("短縮開館（土・日・祝日）", "10:00-19:00"),
            library.fetch_opening_info(lib_num, year=2021, month=7, day=22)
        )
        self.assertEqual(
            ("短縮開館（試験期間）", "9:30-20:00"),
            library.fetch_opening_info(lib_num, year=2021, month=7, day=29)
        )

    # 柏図書館
    def test_kashiwa(self):
        lib_num = 500840

        self.assertEqual(
            ("平日", "9:00-21:00"),
            library.fetch_opening_info(lib_num, year=2021, month=7, day=1)
        )
        self.assertEqual(
            ("閉館", "閉館"),
            library.fetch_opening_info(lib_num, year=2021, month=7, day=22)
        )
        self.assertEqual(
            ("土曜(本学在籍者のみ利用可)", "10:00-17:00"),
            library.fetch_opening_info(lib_num, year=2021, month=7, day=31)
        )
