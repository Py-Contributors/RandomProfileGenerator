from datetime import datetime
import random
import os
import json

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
    return f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"


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

    return (dob, age)


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
    return (height, weight)
