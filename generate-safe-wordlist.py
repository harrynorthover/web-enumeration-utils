import argparse
from distutils.log import error
from io import TextIOWrapper

parser = argparse.ArgumentParser("password_enum")

parser.add_argument(
    "--validUser", help="A valid username", type=str)

parser.add_argument(
    "--validPassword", help="A valid username", type=str)

parser.add_argument(
    "--user", help="Username wordlist", type=str)

parser.add_argument(
    "--users", help="Username wordlist", type=str)

parser.add_argument(
    "--password", help="Password wordlist", type=str)

parser.add_argument(
    "--passwords", help="Password wordlist", type=str)

args = parser.parse_args()

usernames = ""
passwords = ""

newUsers = []
newPasswords = []

if args.users:
    try:
        usWlFile: TextIOWrapper = open(args.users, "r")
    except FileNotFoundError:
        error("Wordlist does not exist!")
    else:
        values = usWlFile.read()
        usernames = values.split('\n')
        usWlFile.close()
else:
    usernames = [args.user]

if args.passwords:
    try:
        pwWlFile: TextIOWrapper = open(args.passwords, "r")
    except FileNotFoundError:
        error("Wordlist does not exist!")
    else:
        values = pwWlFile.read()
        passwords = values.split('\n')
        pwWlFile.close()
else:
    passwords = [args.password]

adjustedUsers = open('./adjusted-users.txt', 'w')
adjustedPassword = open('./adjusted-passwords.txt', 'w')

# Brute-force A User: Single user, with multiple passwords.
if args.user and args.passwords:
    for pwd in passwords:
        adjustedUsers.write(args.validUser + '\n')
        adjustedUsers.write(usernames[0] + '\n')

        adjustedPassword.write(args.validPassword + '\n')
        adjustedPassword.write(pwd + '\n')

# Password Spray: Single password, with multiple users.
if args.password and args.users:
    for user in args.users:
        adjustedUsers.write(args.validUser + '\n')
        adjustedUsers.write(user + '\n')

        adjustedPassword.write(args.validPassword + '\n')
        adjustedPassword.write(passwords[0] + '\n')

# Cluster Attack. Every account, can be tried against every password, with a valid credential in between each row.
if args.passwords and args.users:
    for user in args.users:
        for pwd in args.password:
            adjustedUsers.write(args.validUser + '\n')
            adjustedUsers.write(user + '\n')

            adjustedPassword.write(args.validPassword + '\n')
            adjustedPassword.write(pwd + '\n')
