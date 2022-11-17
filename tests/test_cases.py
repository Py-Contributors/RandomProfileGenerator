import unittest
import sys
import os

sys.path.append('.')
from typing import List, Tuple
from random_profile import RandomProfile
from random_profile import utils
from random_profile.enums.gender import Gender

random_profile = RandomProfile(num=1)


class RandomProfileTest(unittest.TestCase):
    # ----------------------------------------------------------------- #
    def test_fname_instance(self):
        self.assertIsInstance(random_profile.first_names(), str)

    def test_faname_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).first_names()), 10)

    def test_fname_with_num_instance(self):
        self.assertIsInstance(RandomProfile(num=10).first_names(), List)

    # ----------------------------------------------------------------- #
    def test_lname_instance(self):
        self.assertIsInstance(random_profile.last_names(), str)

    def test_lname_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).last_names()), 10)

    def test_lname_with_num_instance(self):
        self.assertIsInstance(RandomProfile(num=10).last_names(), List)

    # ----------------------------------------------------------------- #
    def test_full_names_instance(self):
        self.assertIsInstance(random_profile.full_names(), str)

    def test_full_names_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).full_names()), 10)

    def test_full_names_with_num_instance(self):
        self.assertIsInstance(RandomProfile(num=10).full_names(), List)

    # ----------------------------------------------------------------- #
    def test_full_profiles_instance(self):
        self.assertIsInstance(random_profile.full_profiles(), List)

    def test_full_profiles_with_num(self):
        self.assertEqual(len(RandomProfile(num=10).full_profiles()), 10)

    def test_full_profiles_with_num_instance(self):
        self.assertIsInstance(RandomProfile(num=10).full_profiles(), List)

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

    # ----------------------------------------------------------------- #
    def test_ipv4_format(self):
        ipv4 = utils.ipv4_gen()

        self.assertRegex(ipv4, "^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(.(?!$)|$)){4}$")

    # ----------------------------------------------------------------- #
    def test_random_gender(self):
        gender = utils.generate_random_gender()

        self.assertTrue(gender in [Gender.MALE, Gender.FEMALE])

    def test_gender_male(self):
        profiles = random_profile.full_profiles(100, gender=Gender.MALE)
        males = list(filter(lambda profile: profile["gender"] == "Male", profiles))

        self.assertEqual(len(profiles), len(males))

    def test_gender_female(self):
        profiles = random_profile.full_profiles(100, gender=Gender.FEMALE)
        females = list(filter(lambda profile: profile["gender"] == "Female", profiles))

        self.assertEqual(len(profiles), len(females))

    def test_gender_male_names(self):
        fname_male_txt = os.path.join(utils.ASSETS_DIR, "fnames_male.txt")
        fname_male = utils.load_txt_file(fname_male_txt)

        profiles = random_profile.full_profiles(100, gender=Gender.MALE)
        male_names = list(filter(lambda profile: profile["first_name"] in fname_male, profiles))

        self.assertEqual(len(profiles), len(male_names))

    def test_gender_female_names(self):
        fname_female_txt = os.path.join(utils.ASSETS_DIR, "fnames_female.txt")
        fname_female = utils.load_txt_file(fname_female_txt)

        profiles = random_profile.full_profiles(100, gender=Gender.FEMALE)
        female_names = list(filter(lambda profile: profile["first_name"] in fname_female, profiles))

        self.assertCountEqual(profiles, female_names)

    # ----------------------------------------------------------------- #
    def test_height_range(self):
        height, weight = utils.generate_random_height_weight()

        self.assertTrue(140 <= height <= 200)

    def test_weight_range(self):
        height, weight = utils.generate_random_height_weight()

        self.assertTrue(40 <= weight <= 110)

    def test_weight_height(self):
        height, weight = utils.generate_random_height_weight()

        min, max = 0, 0
        if height < 150:
            min, max = 40, 60
        elif height < 160:
            min, max = 50, 70
        elif height < 170:
            min, max = 60, 80
        elif height < 180:
            min, max = 70, 90
        elif height < 190:
            min, max = 80, 100
        else:
            min, max = 90, 110

        self.assertTrue(min <= weight <= max)


if __name__ == "__main__":
    unittest.main()
