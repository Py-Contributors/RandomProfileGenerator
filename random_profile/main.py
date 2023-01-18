'''
python Random Profile generator module
author : codeperfectplus
language : python 3.0 ++
github : codeperfectplus
'''

import os
import sys
import uuid
import random
from typing import List, Tuple

sys.path.append('.')

from random_profile.enums.gender import Gender
from random_profile import utils
from random_profile.__about__ import __version__

lname_txt = os.path.join(utils.ASSETS_DIR, "lnames.txt")
fname_male_txt = os.path.join(utils.ASSETS_DIR, "fnames_male.txt")
fname_female_txt = os.path.join(utils.ASSETS_DIR, "fnames_female.txt")
hair_colors_txt = os.path.join(utils.ASSETS_DIR, "hair_colors.txt")
blood_types_txt = os.path.join(utils.ASSETS_DIR, "blood_types.txt")
street_names_txt = os.path.join(utils.ASSETS_DIR, "street_names.txt")
cities_name_txt = os.path.join(utils.ASSETS_DIR, "cities_name.txt")
states_names_txt = os.path.join(utils.ASSETS_DIR, "states_names.txt")
job_titles_txt = os.path.join(utils.ASSETS_DIR, "job_titles.txt")
job_levels_txt = os.path.join(utils.ASSETS_DIR, "job_levels.txt")

# loading data from txt files
lname = utils.load_txt_file(lname_txt)
fname_male = utils.load_txt_file(fname_male_txt)
fname_female = utils.load_txt_file(fname_female_txt)
hair_colors = utils.load_txt_file(hair_colors_txt)
blood_types = utils.load_txt_file(blood_types_txt)
states_names = utils.load_txt_file(states_names_txt)
cities_name = utils.load_txt_file(cities_name_txt)
street_names = utils.load_txt_file(street_names_txt)
job_titles = utils.load_txt_file(job_titles_txt)
job_levels = utils.load_txt_file(job_levels_txt)


class RandomProfile(object):
    """ Random Profile Generator

    Args:
        num (int, optional): Total No. of Name You Want To Print. Defaults to 1.
        gender(str, optional): default is None. if you want to generate define gender then pass

    Methods:
        full_profiles: Generate Full Profile
        first_names: Generate First Name
        last_names: Generate Last Name
        full_names: Generate Full Name
        email: Generate Email
        phone_number: Generate Phone Number
        dob_age: Generate Date of Birth and Age
        height_weight: Generate Height and Weight
        address: Generate Address
        ip_address: Generate IP Address
        hair_color: Generate Hair Color
        blood_type: Generate Blood Type
        job_title: Generate Job Title
    """
    def __init__(self, num: int = 1, gender: Gender = None):
        self.num = num
        self.gender = gender

    def __str__(self) -> str:
        return f'Random Profile Generator version {__version__}'

    def __repr__(self) -> str:
        return f'RandomProfile(num={self.num})'

    def __call__(self, num: int = None) -> List[dict]:
        return self.full_profile(num)

    def __iter__(self):
        yield self.full_profile()

    def __next__(self):
        yield self.full_profile()

    def __len__(self):
        return self.num

    def __getitem__(self, index):
        return self.full_profile()[index]

    def ip_address(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return utils.ipv4_gen()
        return [utils.ipv4_gen() for _ in range(num)]

    def job_title(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return random.choice(job_titles)
        return random.choices(job_titles, k=num)

    def blood_type(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return random.choice(blood_types)
        return random.choices(blood_types, k=num)

    def hair_color(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return random.choice(hair_colors)
        return random.choices(hair_colors, k=num)

    def dob_age(self, num: int = None) -> List[Tuple[str, int]]:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return utils.generate_dob_age()
        return [utils.generate_dob_age() for _ in range(num)]

    def height_weight(self, num: int = None) -> List[Tuple[int, int]]:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return utils.generate_random_height_weight()
        return [utils.generate_random_height_weight() for _ in range(num)]

    def generate_address(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        address_list = []
        for _ in range(num):
            street_num = random.randint(100, 999)
            street = random.choice(street_names)
            city = random.choice(cities_name)
            state = random.choice(states_names)
            zip_code = random.randint(10000, 99999)

            address = {
                'street_num': street_num,
                'street': street,
                'city': city,
                'state': state,
                'zip_code': zip_code
            }
            address_list.append(address)

        return address_list

    def first_names(self, num: int = None, gender: Gender = None) -> list:
        num = self.num if num is None else num
        gender = self.gender if gender is None else gender

        # DRY CODE
        if gender is None:
            names = fname_female + fname_male
        elif gender.value == Gender.MALE.value:
            names = fname_male
        else:
            names = fname_female

        if num == 1 or num is None:
            return random.choice(names)

        return random.choices(names, k=num)

    def last_names(self, num: int = None) -> list:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return random.choice(lname)

        return random.choices(lname, k=num)

    def full_names(self, num: int = None, gender: Gender = None) -> list:
        num = self.num if num is None else num
        gender = self.gender if gender is None else gender

        if gender is None:
            names = fname_female + fname_male
        elif gender.value == Gender.MALE.value:
            names = fname_male
        else:
            names = fname_female

        if num == 1 or num is None:
            return random.choice(names) + ' ' + random.choice(lname)

        return [random.choice(names) + ' ' + random.choice(lname) for _ in range(num)]

    def full_profiles(self, num: int = None, gender: Gender = None) -> list:
        num = self.num if num is None else num

        profile_list = []

        for _ in range(num):
            # random gender for every profile in list
            this_gender = utils.generate_random_gender() if gender is None else gender
            first = random.choice(fname_male if this_gender.value == Gender.MALE.value else fname_female)
            last = random.choice(lname)
            full_name = first + ' ' + last

            hair_color = random.choice(hair_colors)
            blood_type = random.choice(blood_types)

            phone_number = f'+1-{random.randint(300, 500)}-{random.randint(800, 999)}-{random.randint(1000,9999)}'

            dob, age = utils.generate_dob_age()
            height, weight = utils.generate_random_height_weight()
            job_experience = utils.generate_random_job_level(age, job_levels)

            street_num = random.randint(100, 999)
            street = random.choice(street_names)
            city, coords = utils.generate_random_city_coords(cities_name)
            coords_pretty = utils.coords_string(coords)
            state = random.choice(states_names)
            zip_code = random.randint(10000, 99999)

            address = {
                'street_num': street_num,
                'street': street,
                'city': city,
                'state': state,
                'zip_code': zip_code
            }

            full_address = f'{street_num} {street}, {city}, {state} {zip_code}'

            mother = self.first_names(1, Gender.FEMALE)[0] + ' ' + last
            father = self.first_names(1, Gender.MALE)[0] + ' ' + last

            card = utils.generate_random_card()

            profile = {}
            profile['id'] = str(uuid.uuid4())
            profile['gender'] = this_gender.value

            profile['first_name'] = first
            profile['last_name'] = last
            profile['hair_color'] = hair_color
            profile['blood_type'] = blood_type
            profile['full_name'] = full_name

            profile['job_title'] = self.job_title(num=1)
            profile['dob'] = dob
            profile['age'] = age
            profile['phone_number'] = phone_number
            profile['email'] = profile['first_name'].lower() + profile['last_name'].lower() + '@example.com'

            profile['blood_type'] = self.blood_type(num=1)
            profile['height'] = height
            profile['weight'] = weight
            profile['hair_color'] = self.hair_color(num=1)
            profile['ip_address'] = self.ip_address(num=1)

            profile['address'] = address
            profile['full_address'] = full_address
            profile['job_experience'] = job_experience
            profile['mother'] = mother
            profile['father'] = father
            profile['payment_card'] = card
            profile['coordinates'] = coords_pretty

            profile_list.append(profile)

        return profile_list
