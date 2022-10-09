'''
python Random Profile generator module
author : codeperfectplus
language : python 3.0 ++
github : codeperfectplus
   ______            __         ____               ____             __     ____   __            
  / ____/____   ____/ /___     / __ \ ___   _____ / __/___   _____ / /_   / __ \ / /__  __ _____
 / /    / __ \ / __  // _ \   / /_/ // _ \ / ___// /_ / _ \ / ___// __/  / /_/ // // / / // ___/
/ /___ / /_/ // /_/ //  __/  / ____//  __// /   / __//  __// /__ / /_   / ____// // /_/ /(__  ) 
\____/ \____/ \__,_/ \___/  /_/     \___//_/   /_/   \___/ \___/ \__/  /_/    /_/ \__,_//____/  

'''
import random
fname = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura',
         'Jennifer', 'Maria', 'Adam', 'Sturt', 'Nikolson', 'Tom', 'Harry', 'Ruskin', 'Thor', 'Rocky', 'Ravid', 'David', 'Harris', 'Eion', 'Elon', 'Mark', 'Will', 'Chris', 'Laura', 'Samara', 'Darren', 'Jim', 'Jeremy', 'Dylan', 'Jake', 'Patti', 'Paget', 'Mira', 'Maude', 'Katie', 'Rob',
         'Brian', 'Kerry', 'Chad', 'Nicola']
        
lname = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown',
         'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin', 'Potter', 'Jukerberg', 'Smith', 'Nebula', 'Downy', 'Downy Jr',
         'Brewster', 'Amberg', 'Kaye', 'Harrier', 'Criss', 'Parsons', 'McDermott', 'Picking', 'Hudson']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park',
                'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield',
               'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS',
          'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']


class RandomProfile:
    def __init__(self, num=1):
        '''
        num = Total No. of Name You Want To Print
        deafult is 1
        To Print More Than one Name Change value of num
        '''
        self.num = num

    def first_name(self):
        # print first name
        first_name_list = [random.choice(fname) for _ in range(self.num)]
        return first_name_list

    def last_name(self):
        # print last name
        last_name_list = [random.choice(lname) for _ in range(self.num)]
        return last_name_list

    def full_name(self):
        # print full name
        full_name_list = [random.choice(
            fname) + ' ' + random.choice(lname) for _ in range(self.num)]
        return full_name_list

    def full_profile(self):
        # print full profile
        profile_list = []
        for _ in range(self.num):
            first = random.choice(fname)
            last = random.choice(lname)
            phone = f'+ +{random.randint(1, 999)}-{random.randint(300, 500)}{random.randint(800, 999)}{random.randint(1000,9999)}'

            street_num = random.randint(100, 999)
            street = random.choice(street_names)
            city = random.choice(fake_cities)
            state = random.choice(states)
            zip_code = random.randint(10000, 99999)

            address = f'{street_num} {street} St. {city} {state} {zip_code}'
            email = first.lower() + last.lower() + '@bogusemail.com'

            profile_dict = {}
            profile_dict['first_name'] = first
            profile_dict['last_name'] = last
            profile_dict['phone'] = phone
            profile_dict['address'] = address
            profile_dict['email'] = email
            profile_list.append(profile_dict)

        return profile_list
