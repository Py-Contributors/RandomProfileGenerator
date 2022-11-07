'''
python Random Profile generator module
author : codeperfectplus
language : python 3.0 ++
github : codeperfectplus
'''

import os
import uuid
import random
import utils

from enums.gender import Gender

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
    def __init__(self, num: int = 1, gender: Gender = None):
        """
        num = Total No. of Name You Want To Print
        default is 1
        To Print More Than one Name Change value of num
        """
        self.num = num
        self.gender = gender

    def first_names(self, num: int = None, gender: Gender = None) -> list:
        if num is None:
            num = self.num
        if gender is None:
            gender = self.gender

        if gender is None:
            names = fname_female + fname_male
        elif gender.value == Gender.MALE.value:
            names = fname_male
        else:
            names = fname_female

        first_name_list = [random.choice(names) for _ in range(num)]
        return first_name_list

    def last_names(self, num: int = None) -> list:
        if num is None:
            num = self.num

        last_name_list = [random.choice(lname) for _ in range(num)]
        return last_name_list

    def full_names(self, num: int = None, gender: Gender = None) -> list:
        if num is None:
            num = self.num

        if gender is None:
            gender = self.gender

        if gender is None:
            names = fname_female + fname_male
        elif gender.value == Gender.MALE.value:
            names = fname_male
        else:
            names = fname_female

        full_name_list = [random.choice(names) + ' ' + random.choice(lname) for _ in range(num)]
        return full_name_list

    def full_profiles(self, num: int = None, gender: Gender = None) -> list:
        if num is None:
            num = self.num

        profile_list = []

        for _ in range(num):
            unique_id = uuid.uuid4().hex

            # random gender for every profile in list
            this_gender = utils.generate_random_gender() if gender is None else gender
            first = random.choice(fname_male if this_gender.value == Gender.MALE.value else fname_female)

            last = random.choice(lname)
            hair_color = random.choice(hair_colors)
            blood_type = random.choice(blood_types)
            full_name = first + ' ' + last
            phone = f'+1-{random.randint(300, 500)}-{random.randint(800, 999)}-{random.randint(1000,9999)}'

            ip_address = utils.ipv4_gen()

            dob, age = utils.generate_dob_age()
            height, weight = utils.generate_random_height_weight()

            job_title = random.choice(job_titles)
            job_experience = utils.generate_random_job_level(age, job_levels)

            street_num = random.randint(100, 999)
            street = random.choice(street_names)
            city, coords = utils.generate_random_city_coords(cities_name)
            coords_pretty = utils.coords_string(coords)
            state = random.choice(states_names)
            zip_code = random.randint(10000, 99999)

            address = f'{street_num} {street} St. {city} {state} {zip_code}'
            email = first.lower() + last.lower() + '@example.com'

            mother = self.first_names(1, Gender.FEMALE)[0] + ' ' + last
            father = self.first_names(1, Gender.MALE)[0] + ' ' + last

            card = utils.generate_random_card()

            profile_dict = {}
            profile_dict['id'] = unique_id
            profile_dict['gender'] = this_gender.value
            profile_dict['first_name'] = first
            profile_dict['last_name'] = last
            profile_dict['hair_color'] = hair_color
            profile_dict['blood_type'] = blood_type
            profile_dict['full_name'] = full_name
            profile_dict['DOB'] = dob
            profile_dict['age'] = age
            profile_dict['height'] = height
            profile_dict['weight'] = weight
            profile_dict['phone'] = phone
            profile_dict['address'] = address
            profile_dict['coordinates'] = coords_pretty
            profile_dict['email'] = email
            profile_dict['job_title'] = job_title
            profile_dict['job_job_experience'] = job_experience
            profile_dict['ip_address'] = ip_address
            profile_dict['mother'] = mother
            profile_dict['father'] = father
            profile_dict['payment_card'] = card

            profile_list.append(profile_dict)

        return profile_list

    def ipv4(self) -> list:
        ip_list = [utils.ipv4_gen() for _ in range(self.num)]
        return ip_list

    def job_title(self) -> list:
        job_title_list = [random.choice(job_titles) for _ in range(self.num)]
        return job_title_list
