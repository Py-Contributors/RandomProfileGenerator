
import sys
import argparse
from pprint import pprint

sys.path.append('.')
from random_profile.main import RandomProfile
from random_profile.main import VERSION
from random_profile.api import start_server

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--version', action='version', version=VERSION)
parser.add_argument('--server', help='Start server', action='store_true')
parser.add_argument('--port', help='Port number', type=int, default=8000)
parser.add_argument('-n', help='Number of random profiles', type=int, default=1)

group = parser.add_mutually_exclusive_group()
group.add_argument('-p', '--profile', help='Get full profile', action='store_true')
group.add_argument('-f', '--firstname', help='Get first name', action='store_true')
group.add_argument('-l', '--lastname', help='Get last name instead of first name', action='store_true')
group.add_argument('--fullname', help='Get full name instead of first name', action='store_true')
group.add_argument('--ip', help='Get an ipv4 IP address', action='store_true')
group.add_argument('--job', help='Get job title', action='store_true')
group.add_argument('--address', help='Get address', action='store_true')
args = parser.parse_args()


def main():
    rp = RandomProfile(args.n)
    if args.server:
        start_server(args.port)
    elif args.fullname:
        pprint(rp.full_name())
    elif args.firstname:
        pprint(rp.first_name())
    elif args.lastname:
        pprint(rp.last_name())
    elif args.job:
        pprint(rp.job_title())
    elif args.ip:
        pprint(rp.ip_address())
    elif args.address:
        pprint(rp.generate_address())
    elif args.profile:
        pprint(rp.full_profile())
    else:
        pprint('Type `rp -h` for help')


if __name__ == '__main__':
    main()
