import math
import sys
from datetime import datetime
import random
import os
import json

sys.path.append('.')

from random_profile.enums.gender import Gender

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(ROOT_DIR, "random_profile", "assets")


def load_json(file_name: str) -> dict:
    """ function to load json file into dict

    args:
        file_name (str): file name to load

    returns:
        dict: dict of data from file
    """
    with open(file_name, "r") as f:
        data = json.load(f)
    return data


# radius of the earh in meters
M_PER_DEGREE = 111319.5


def generate_random_gender() -> Gender:
    return random.choice(list(Gender))


def load_txt_file(file_name: str) -> list:
    """ function to load txt file into list

    args:
        file_name (str): file name to load

    returns:
        list: list of data from file
    """
    with open(file_name, "r") as f:
        data = f.read().splitlines()
    return data


def ipv4_gen() -> str:
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"


def generate_dob_age() -> tuple:
    month = random.randint(1, 12)
    if month == 2:  # if month is feb
        day = random.randint(1, 28)
    elif month in [4, 6, 9, 11]:  # if month has 30 days
        day = random.randint(1, 30)
    elif month in [1, 3, 5, 7, 8, 10, 12]:  # if month has 31 days
        day = random.randint(1, 31)

    current_year = datetime.now().year
    year = random.randint(current_year - 80, current_year - 18)

    dob = datetime(day=day, month=month, year=year)
    age = (datetime.now() - dob).days // 365
    dob = dob.strftime("%d/%m/%Y")

    return dob, age


def generate_random_height_weight() -> tuple:
    height = random.randint(140, 200)
    if height < 150:
        weight = random.randint(40, 60)
    elif height < 160:
        weight = random.randint(50, 70)
    elif height < 170:
        weight = random.randint(60, 80)
    elif height < 180:
        weight = random.randint(70, 90)
    elif height < 190:
        weight = random.randint(80, 100)
    elif height <= 200:
        weight = random.randint(90, 110)
    return height, weight


def generate_random_card() -> dict:
    card_type = random.choice(("Credit", "Debit"))
    number = f"{random.randint(1, 9999):04}-{random.randint(1, 9999):04}-{random.randint(1, 9999):04}-{random.randint(1, 9999):04}"

    expiration_year = random.randint(datetime.today().year, datetime.today().year + 10)
    expiration_month = random.randint(1, 12)
    expiration = f"{expiration_month:02}/{str(expiration_year)[-2:]}"

    card = {
        "type": card_type,
        "number": number,
        "expiration": expiration
    }

    return card


def generate_random_job_level(age: int, levels) -> str:
    levels_with_ranges = [level.split(';') for level in levels]
    applicable_level = list(filter(lambda level: (int(level[1]) <= age <= int(level[2])), levels_with_ranges))

    level = ""

    try:
        level = applicable_level[0][0]
    except Exception:
        print(applicable_level)
        print(age)

    return level


def random_coords_from_point(lat: float, lon: float, max_distance: float = 1000) -> tuple:
    angle = random.random() * 2 * math.pi
    offset = random.random() * max_distance

    lat_ = lat + math.cos(angle) * offset / M_PER_DEGREE
    lon_ = lon + math.sin(angle) * offset / M_PER_DEGREE

    return lat_, lon_


def generate_random_city_coords(cities) -> tuple:
    city = random.choice(cities)

    city_data = city.split(';')

    name = city_data[0]
    lat = float(city_data[1])
    lon = float(city_data[2])

    coords = random_coords_from_point(lat, lon)
    return name, coords


def decdeg2dms(dd):
    mult = -1 if dd < 0 else 1
    mnt, sec = divmod(abs(dd) * 3600, 60)
    deg, mnt = divmod(mnt, 60)
    return mult * deg, mult * mnt, mult * sec


def coords_string(coords: tuple) -> str:
    dms_lat = decdeg2dms(abs(coords[0]))
    dms_lon = decdeg2dms(abs(coords[1]))

    return f"{dms_lat[0]:.0f}° {dms_lat[1]:.0f}' {dms_lat[2]:.4f}'' {'N' if coords[0] > 0 else 'S'} {dms_lon[0]:.0f}° {dms_lon[1]:.0f}' {dms_lon[2]:.4f}'' {'E' if coords[1] > 0 else 'W'}"
