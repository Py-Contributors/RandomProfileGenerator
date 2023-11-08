
import sys
import random
import argparse
from pprint import pprint

sys.path.append('.')

from random_profile.main import RandomProfile
from random_profile.__about__ import __version__
from random_profile.api import start_server
from random_profile.enums.gender import Gender

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', action='version', version=__version__)
parser.add_argument('--repeat', help='Repeat the output', action='store_true')
parser.add_argument('--server', help='Start server', action='store_true')
parser.add_argument('--port', help='Port number', type=int, default=8000)
parser.add_argument('-n', '--number', help='Number of random profiles', type=int, default=1)

gender_arg_group = parser.add_mutually_exclusive_group()

gender_arg_group.add_argument("-ma", "--male", help="Get only male profiles", action="store_true")
gender_arg_group.add_argument("-fe", "--female", help="Get only female profiles", action="store_true")

output_form_arg_group = parser.add_mutually_exclusive_group()
output_form_arg_group.add_argument('-p', '--profile', help='Get full profile', action='store_true')
output_form_arg_group.add_argument('-f', '--firstname', help='Get first name', action='store_true')
output_form_arg_group.add_argument('-l', '--lastname', help='Get last name instead of first name', action='store_true')
output_form_arg_group.add_argument('-F', '--fullname', help='Get full name instead of first name', action='store_true')
output_form_arg_group.add_argument('-ip', '--ip_address', help='Get an ipv4 IP address', action='store_true')
output_form_arg_group.add_argument('-j', '--job', help='Get job title', action='store_true')
output_form_arg_group.add_argument('-a', '--address', help='Get address', action='store_true')
args = parser.parse_args()

if args.repeat:
    random.seed(0)


def main():
    gender = None
    if args.male:
        gender = Gender.MALE
    elif args.female:
        gender = Gender.FEMALE
    rp = RandomProfile(args.number, gender)
    if args.server:
        start_server(args.port)
    elif args.fullname:
        pprint(rp.full_names())
    elif args.firstname:
        pprint(rp.first_names())
    elif args.lastname:
        pprint(rp.last_names())
    elif args.job:
        pprint(rp.job_title())
    elif args.ip_address:
        pprint(rp.ip_address())
    elif args.address:
        pprint(rp.generate_address())
    elif args.profile:
        pprint(rp.full_profiles())
    else:
        pprint('Type `rp -h` for help')


if __name__ == '__main__':
    main()
