import unittest
import sys

sys.path.append('.')
from typing import List, Tuple
from random_profile import RandomProfile
random_profile = RandomProfile(num=1)


class RandomProfileTest(unittest.TestCase):
    # ----------------------------------------------------------------- #
    def test_fname_instance(self):
        self.assertIsInstance(random_profile.first_name(), str)

    def test_faname_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).first_name()), 10)

    def test_fname_with_num_instance(self):
        self.assertIsInstance(RandomProfile(num=10).first_name(), List)

    # ----------------------------------------------------------------- #
    def test_lname_instance(self):
        self.assertIsInstance(random_profile.last_name(), str)

    def test_lname_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).last_name()), 10)

    def test_lname_with_num_instance(self):
        self.assertIsInstance(RandomProfile(num=10).last_name(), List)

    # ----------------------------------------------------------------- #
    def test_full_name_instance(self):
        self.assertIsInstance(random_profile.full_name(), str)

    def test_full_name_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).full_name()), 10)

    def test_full_name_with_num_instance(self):
        self.assertIsInstance(RandomProfile(num=10).full_name(), List)

    # ----------------------------------------------------------------- #
    def test_full_profile_instance(self):
        self.assertIsInstance(random_profile.full_profile(), List)

    def test_full_profile_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).full_profile()), 10)

    def test_full_profile_with_num_instance(self):
        self.assertIsInstance(RandomProfile(num=10).full_profile(), List)

    # ----------------------------------------------------------------- #
    def test_ipv4_instance(self):
        self.assertIsInstance(random_profile.ip_address(), str)

    def test_ipv4_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).ip_address()), 10)

    def test_ipv4_with_num_instance(self):
        self.assertIsInstance(RandomProfile(num=10).ip_address(), List)

    # ----------------------------------------------------------------- #
    def test_job_title_instance(self):
        self.assertIsInstance(random_profile.job_title(), str)

    def test_job_title_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).job_title()), 10)

    def test_job_title_with_num_instance(self):
        self.assertIsInstance(RandomProfile(num=10).job_title(), List)

    # ----------------------------------------------------------------- #
    def test_blood_type_instance(self):
        self.assertIsInstance(random_profile.blood_type(), str)

    def test_blood_type_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).blood_type()), 10)

    def test_blood_type_with_num_instance(self):
        self.assertIsInstance(RandomProfile(num=10).blood_type(), List)

    # ----------------------------------------------------------------- #
    def test_hair_color_instance(self):
        self.assertIsInstance(random_profile.hair_color(), str)

    def test_hair_color_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).hair_color()), 10)

    def test_hair_color_with_num_instance(self):
        self.assertIsInstance(RandomProfile(num=10).hair_color(), List)

    # ----------------------------------------------------------------- #
    def test_dob_age_instance(self):
        self.assertIsInstance(random_profile.dob_age(), Tuple)

    def test_dob_age_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).dob_age()), 10)

    def test_dob_age_with_num_instance(self):
        self.assertIsInstance(RandomProfile(num=10).dob_age(), List)

    # ----------------------------------------------------------------- #
    def test_address_instance(self):
        self.assertIsInstance(random_profile.generate_address(), List)

    def test_address_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).generate_address()), 10)

    def test_address_with_num_instance(self):
        self.assertIsInstance(RandomProfile(num=10).generate_address(), List)


if __name__ == "__main__":
    unittest.main()
