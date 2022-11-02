import unittest
import re

from main import RandomProfile
from utils import *

random_profile = RandomProfile(num=1)

class RandomProfileTest(unittest.TestCase):
    def test_fname(self):
        self.assertEqual(len(random_profile.first_names()), 1)

    def test_faname_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).first_names()), 10)

    def test_lname(self):
        self.assertEqual(len(random_profile.last_names()), 1)

    def test_lname_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).last_names()), 10)

    def test_full_name(self):
        self.assertEqual(len(random_profile.full_names()), 1)

    def test_full_name_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).full_names()), 10)

    def test_full_profile(self):
        self.assertEqual(len(random_profile.full_profiles()), 1)

    def test_full_profile_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).full_profiles()), 10)

    def test_ipv4(self):
        self.assertEqual(len(random_profile.ipv4()), 1)

    def test_ipv4_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).ipv4()), 10)

    def test_job_title(self):
        self.assertEqual(len(random_profile.job_title()), 1)

    def test_job_title_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).job_title()), 10)

    # my tests
    def test_ipv4_format(self):
        ipv4 = ipv4_gen()
        reg = re.search("^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\.(?!$)|$)){4}$", ipv4)

        self.assertIsNotNone(reg)

    def test_gender_male(self):

    def test_gender_female(self):

if __name__ == "__main__":
    unittest.main()
