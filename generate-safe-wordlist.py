import argparse
from distutils.log import error
from io import TextIOWrapper

parser = argparse.ArgumentParser("password_enum")

parser.add_argument(
    "--validUser", help="A valid username", type=str)

parser.add_argument(
    "--validPassword", help="A valid username", type=str)

parser.add_argument(
    "--users", help="Username wordlist", type=str)

parser.add_argument(
    "--password", help="Password wordlisr", type=str)

args = parser.parse_args()

correctLogin = ""
correctPassword = ""
usernames = ""
passwords = ""

try:
    usWlFile: TextIOWrapper = open(args.users, "r")
except FileNotFoundError:
    error("Wordlist does not exist!")
else:
    values = usWlFile.read()
    usernames = values.split('\n')
    usWlFile.close()

try:
    pwWlFile: TextIOWrapper = open(args.users, "r")
except FileNotFoundError:
    error("Wordlist does not exist!")
else:
    values = pwWlFile.read()
    passwords = values.split('\n')
    pwWlFile.close()

for user in usernames:
