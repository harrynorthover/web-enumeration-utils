# web-enumeration-utils

A collection of utils to aid in enumeration web sites.

### generate-safe-wordlist.py

This is when we are targeting an authentication system that locks you out after so many failed attempted. This script allows you to generate different kinds of wordlists, with correct credentials injected into every-other row. This makes sure there is only every one failed attempt in a row.

Brute Force A User
-user=USERNAME -passwords=/path/to/wordlist.txt

Password Spraying
-users=USERNAME -password=password.

Cluster Attack
-users=/path/to/wordlist.txt -passwords=/path/to/wordlist.txt

The generated wordlists can then be used in BurpSuite or elsewhere to execute the attack.
