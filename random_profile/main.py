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
from dataclasses import dataclass, asdict

    # Ensure the current directory is in the path to import local modules
# Adjust your path as needed
sys.path.append('.')

from random_profile.enums import gender
from random_profile.enums.gender import Gender
from random_profile import utils
from random_profile.__about__ import __version__

# Asset file paths
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

# Load text data
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

@dataclass
class Profile:
    id: str
    gender: str
    first_name: str
    last_name: str
    full_name: str
    hair_color: str
    blood_type: str
    job_title: str
    dob: str
    age: int
    phone_number: str
    email: str
    height: int
    weight: int
    ip_address: str
    address: dict
    full_address: str
    job_experience: str
    mother: str
    father: str
    payment_card: dict
    coordinates: str

class RandomProfile:
    """
    Random Profile Generator

    Args:
        num (int, optional): Number of profiles to generate. Defaults to 1.
        gender (Gender, optional): Specify a gender. Defaults to None for random.

    Methods:
        full_profiles: Generate a list of full profiles.
        first_names: Generate first names.
        last_names: Generate last names.
        full_names: Generate full names (first + last).
        email: Generate email addresses.
        phone_number: Generate phone numbers.
        dob_age: Generate date of birth and age.
        height_weight: Generate height and weight.
        address: Generate address data.
        ip_address: Generate IP addresses.
        hair_color: Generate hair color(s).
        blood_type: Generate blood type(s).
        job_title: Generate job title(s).
    """

    def __init__(self, num: int = 1, gender: Gender = Gender.UNSPECIFIED):
        if num < 1:
            raise ValueError("Number of profiles must be greater than 0.")
        self.num = num
        self.gender = gender

    def __str__(self) -> str:
        return f"Random Profile Generator version {__version__}"

    def __repr__(self) -> str:
        return f"RandomProfile(num={self.num}, gender={self.gender})"

    def __call__(self, num: int = None) -> List[dict]:
        return self.full_profiles(num)  # Call to generate full profiles

    def __iter__(self):
        yield self.full_profiles()

    def __next__(self):
        yield self.full_profiles()

    def __len__(self):
        return self.num

    def __getitem__(self, index):
        profiles = self.full_profiles()
        return profiles[index]

    def _resolve_count(self, num):
        return self.num if num is None else num

    def ip_address(self, num: int = None) -> List[str]:
        """Generate one or more IPv4 addresses."""
        count = self.num if num is None else num
        if count == 1:
            return [utils.ipv4_gen()]
        return [utils.ipv4_gen() for _ in range(count)]

    def job_title(self, num: int = None) -> List[str]:
        """Generate one or more job titles."""
        count = self.num if num is None else num
        if count == 1:
            return [random.choice(job_titles)]
        return random.choices(job_titles, k=self._resolve_count(num))

    def blood_type(self, num: int = None) -> List[str]:
        """Generate one or more blood types."""
        count = self.num if num is None else num
        if count == 1:
            return [random.choice(blood_types)]
        return random.choices(blood_types, k=self._resolve_count(num))

    def hair_color(self, num: int = None) -> List[str]:
        """Generate one or more hair colors."""
        count = self.num if num is None else num
        if count == 1:
            return [random.choice(hair_colors)]
        return random.choices(hair_colors, k=self._resolve_count(num))

    def dob_age(self, num: int = None) -> List[Tuple[str, int]]:
        """Generate DOB and age tuples."""
        count = self.num if num is None else num
        if count == 1:
            return [utils.generate_dob_age()]
        return [utils.generate_dob_age() for _ in range(count)]

    def height_weight(self, num: int = None) -> List[Tuple[int, int]]:
        """Generate height and weight tuples."""
        count = self.num if num is None else num
        if count == 1:
            return [utils.generate_random_height_weight()]
        return [utils.generate_random_height_weight() for _ in range(count)]

    def generate_address(self, num: int = None) -> List[dict]:
        """
        Generate one or more addresses.
        Returns a list of dictionaries with address components.
        """
        count = self.num if num is None else num
        address_list = []
        for _ in range(count):
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

    def first_names(self, num: int = None, gender: Gender = None) -> List[str]:
        """Generate one or more first names based on gender."""
        count = self.num if num is None else num
        gen = self.gender if gender is None else gender

        if gen is None:
            names_pool = fname_female + fname_male
        elif gen.value == Gender.MALE.value:
            names_pool = fname_male
        else:
            names_pool = fname_female

        if count == 1:
            return [random.choice(names_pool)]
        return random.choices(names_pool, k=self._resolve_count(num))

    def last_names(self, num: int = None) -> List[str]:
        """Generate one or more last names."""
        count = self.num if num is None else num
        if count == 1:
            return [random.choice(lname)]
        return random.choices(lname, k=self._resolve_count(num))

    def full_names(self, num: int = None, gender: Gender = None) -> List[str]:
        """Generate one or more full names (first + last)."""
        count = self.num if num is None else num
        gen = self.gender if gender is None else gender

        if gen is None:
            first_pool = fname_female + fname_male
        elif gen.value == Gender.MALE.value:
            first_pool = fname_male
        else:
            first_pool = fname_female

        names = []
        for _ in range(count):
            f_name = random.choice(first_pool)
            l_name = random.choice(lname)
            names.append(f"{f_name} {l_name}")
        return names

    def full_profiles(self, num: int = None, gender: Gender = None) -> List[dict]:
        """
        Generate one or more full profiles.
        Each profile is a dictionary containing various personal details.
        """
        count = self.num if num is None else num
        profile_list = []

        for _ in range(count):
            this_gender = utils.generate_random_gender() if gender is None else gender

            # Generate names
            f_name = random.choice(fname_male if this_gender.value == Gender.MALE.value else fname_female)
            l_name = random.choice(lname)
            full_name = f"{f_name} {l_name}"

            # Generate personal data
            hair = random.choice(hair_colors)
            blood = random.choice(blood_types)
            phone_number = f"+1-{random.randint(300, 500)}-{random.randint(800, 999)}-{random.randint(1000, 9999)}"
            dob, age = utils.generate_dob_age()
            height, weight = utils.generate_random_height_weight()
            job_experience = utils.generate_random_job_level(age, job_levels)
            city, coords = utils.generate_random_city_coords(cities_name)
            coords_pretty = utils.coords_string(coords)

            # Generate address
            street_num = random.randint(100, 999)
            street = random.choice(street_names)
            state = random.choice(states_names)
            zip_code = random.randint(10000, 99999)
            address_dict = {
                'street_num': street_num,
                'street': street,
                'city': city,
                'state': state,
                'zip_code': zip_code
            }
            full_address = f"{street_num} {street}, {city}, {state} {zip_code}"

            # Generate parents
            mother = f"{random.choice(fname_female)} {l_name}"
            father = f"{random.choice(fname_male)} {l_name}"

            # Generate payment card info
            card = utils.generate_random_card()

            # Compose the profile dict
            # profile = {
            #     'id': str(uuid.uuid4()),
            #     'gender': this_gender.value,
            #     'first_name': f_name,
            #     'last_name': l_name,
            #     'full_name': full_name,
            #     'hair_color': hair,  # matching the list return type from hair_color()
            #     'blood_type': blood,  # matching the list return type from blood_type()
            #     'job_title': random.choice(job_titles),
            #     'dob': dob,
            #     'age': age,
            #     'phone_number': phone_number,
            #     'email': f"{f_name.lower()}{l_name.lower()}@example.com",
            #     'height': height,
            #     'weight': weight,
            #     'ip_address': utils.ipv4_gen(),  # typically returns a list
            #     'address': address_dict,
            #     'full_address': full_address,
            #     'job_experience': job_experience,
            #     'mother': mother,
            #     'father': father,
            #     'payment_card': card,
            #     'coordinates': coords_pretty
            # }

            # profile_list.append(profile)
            profile = Profile(
                id=str(uuid.uuid4()),
                gender=this_gender.value if this_gender.value is not None else "",
                first_name=f_name,
                last_name=l_name,
                full_name=full_name,
                hair_color=hair,
                blood_type=blood,
                job_title=random.choice(job_titles),
                dob=dob,
                age=age,
                phone_number=phone_number,
                email=f"{f_name.lower()}{l_name.lower()}@example.com",
                height=height,
                weight=weight,
                ip_address=utils.ipv4_gen(),
                address=address_dict,
                full_address=full_address,
                job_experience=job_experience,
                mother=mother,
                father=father,
                payment_card=card,
                coordinates=coords_pretty
            )
            profile_list.append(asdict(profile))

        return profile_list
