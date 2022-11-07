import argparse

from main import RandomProfile
from enums.gender import Gender


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", help="Number of random profiles", type=int, default=1)

    gender_arg_group = parser.add_mutually_exclusive_group()
    gender_arg_group.add_argument(
        "-ma",
        "--male",
        help="Get only male profiles",
        action="store_true"
    )
    gender_arg_group.add_argument(
        "-fe",
        "--female",
        help="Get only female profiles",
        action="store_true"
    )

    output_form_arg_group = parser.add_mutually_exclusive_group()
    output_form_arg_group.add_argument(
        "-f",
        "--firstname",
        help="Get only first name",
        action="store_true",
    )
    output_form_arg_group.add_argument(
        "-l",
        "--lastname",
        help="Get last name instead of first name",
        action="store_true",
    )
    output_form_arg_group.add_argument(
        "-F",
        "--fullname",
        help="Get full name instead of first name",
        action="store_true",
    )
    output_form_arg_group.add_argument(
        "-ip",
        "--ipv4",
        help="Get an ipv4 IP address",
        action="store_true",
    )
    output_form_arg_group.add_argument(
        "-j",
        "--jobtitle",
        help="Get job title",
        action="store_true",
    )
    output_form_arg_group.add_argument(
        "-p",
        "--profile",
        help="Get full profile instead of first name",
        action="store_true",
    )

    args = parser.parse_args()

    gender = None
    if args.male:
        gender = Gender.MALE
    elif args.female:
        gender = Gender.FEMALE

    rp = RandomProfile(args.n, gender)
    if args.fullname:
        print(*rp.full_names(), sep="\n")
    elif args.profile:
        print(*rp.full_profiles(), sep="\n")
    elif args.lastname:
        print(*rp.last_names(), sep="\n")
    elif args.jobtitle:
        print(*rp.job_title(), sep="\n")
    elif args.ipv4:
        print(*rp.ipv4(), sep="\n")
    else:
        print('Type `random_profile -h` for help')


if __name__ == "__main__":
    main()
