import unittest
import os

from main import RandomProfile
import utils
from enums.gender import Gender

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
        ipv4 = utils.ipv4_gen()

        self.assertRegex(ipv4, "^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(\\.(?!$)|$)){4}$")

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

    def test_height_range(self):
        height_weight = utils.generate_random_height_weight()

        self.assertTrue(140 <= height_weight[0] <= 200)

    def test_weight_range(self):
        height_weight = utils.generate_random_height_weight()

        self.assertTrue(40 <= height_weight[1] <= 110)

    def test_weight_height(self):
        height, weight = utils.generate_random_height_weight()

        min_, max_ = 0, 0
        if height < 150:
            min_, max_ = 40, 60
        elif height < 160:
            min_, max_ = 50, 70
        elif height < 170:
            min_, max_ = 60, 80
        elif height < 180:
            min_, max_ = 70, 90
        elif height < 190:
            min_, max_ = 80, 100
        else:
            min_, max_ = 90, 110

        self.assertTrue(min_ <= weight <= max_)


if __name__ == "__main__":
    unittest.main()
