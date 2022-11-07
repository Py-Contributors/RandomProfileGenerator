'''
python Random Profile generator module
author : codeperfectplus
language : python 3.0 ++
github : codeperfectplus
'''

import os
import uuid
import random
from typing import List, Tuple

from random_profile.utils import ipv4_gen
from random_profile.utils import load_txt_file
from random_profile.utils import generate_dob_age
from random_profile.utils import generate_random_height_weight
from random_profile.utils import ASSETS_DIR

VERSION = '2.0.0'

fname_txt = os.path.join(ASSETS_DIR, 'fnames.txt')
lname_txt = os.path.join(ASSETS_DIR, 'lnames.txt')
hair_colors_txt = os.path.join(ASSETS_DIR, 'hair_colors.txt')
blood_types_txt = os.path.join(ASSETS_DIR, 'blood_types.txt')
street_names_txt = os.path.join(ASSETS_DIR, 'street_names.txt')
cities_name_txt = os.path.join(ASSETS_DIR, 'cities_name.txt')
states_names_txt = os.path.join(ASSETS_DIR, 'states_names.txt')
job_titles_txt = os.path.join(ASSETS_DIR, 'job_titles.txt')
states_hash_json = os.path.join(ASSETS_DIR, 'states_hash.json')

# loading data from txt files
fname = load_txt_file(fname_txt)
lname = load_txt_file(lname_txt)
hair_colors = load_txt_file(hair_colors_txt)
blood_types = load_txt_file(blood_types_txt)
states_names = load_txt_file(states_names_txt)
cities_name = load_txt_file(cities_name_txt)
street_names = load_txt_file(street_names_txt)
job_titles = load_txt_file(job_titles_txt)


class RandomProfile(object):
    ''' Random Profile Generator '''
    def __init__(self, num: int = 1):
        self.num = num

    def __str__(self) -> str:
        return f'Random Profile Generator version {VERSION}'

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

    def first_name(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return random.choice(fname)
        return random.choices(fname, k=num)

    def last_name(self, num: int = None) -> list:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return random.choice(lname)
        return random.choices(lname, k=num)

    def full_name(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return f'{random.choice(fname)} {random.choice(lname)}'
        return [random.choice(fname) + ' ' + random.choice(lname) for _ in range(num)]

    def ip_address(self, num: int = None) -> List[str]:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return ipv4_gen()
        return [ipv4_gen() for _ in range(num)]

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
            return generate_dob_age()
        return [generate_dob_age() for _ in range(num)]

    def height_weight(self, num: int = None) -> List[Tuple[int, int]]:
        num = self.num if num is None else num
        if num == 1 or num is None:
            return generate_random_height_weight()
        return [generate_random_height_weight() for _ in range(num)]

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

    def full_profile(self, num: int = None) -> List[dict]:
        num = self.num if num is None else num
        profile_list = []
        for _ in range(num):
            phone_number = f'+1-{random.randint(300, 500)}-{random.randint(800, 999)}-{random.randint(1000,9999)}'
            dob, age = self.dob_age(num=1)
            height, weight = self.height_weight(num=1)
            address = self.generate_address()[0]
            full_address = '{} {} {}, {} {}'.format(address['street_num'],
                                                    address['street'],
                                                    address['city'],
                                                    address['state'],
                                                    address['zip_code'])

            profile = {}
            profile['id'] = str(uuid.uuid4())
            profile['first_name'] = self.first_name(num=1)
            profile['last_name'] = self.first_name(num=1)
            profile['full_name'] = profile['first_name'] + ' ' + profile['last_name']
            profile['job_title'] = self.job_title(num=1)
            profile['dob'] = dob
            profile['age'] = age
            profile['phone_number'] = phone_number
            profile['email'] = profile['first_name'].lower() + profile['last_name'].lower() + '@example.com'
            profile['address'] = address
            profile['full_address'] = full_address
            profile['blood_type'] = self.blood_type(num=1)
            profile['height'] = height
            profile['weight'] = weight
            profile['hair_color'] = self.hair_color(num=1)
            profile['ip_address'] = self.ip_address(num=1)

            profile_list.append(profile)

        return profile_list
