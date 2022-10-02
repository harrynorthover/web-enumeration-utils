# web-enumeration-utils

A collection of utils to aid in enumeration web sites.

### generate-safe-wordlist.py

This is when we are targeting an authentication system that locks you out after so many failed attempted. This script allows you to generate different kinds of wordlists, with correct credentials injected into every-other row. This makes sure there is only every one failed attempt in a row.

_Brute Force A User_

`python generate-safe-wordlist.py -user=USERNAME -passwords=/path/to/wordlist.txt`

_Password Spraying_

`python generate-safe-wordlist.py -users=USERNAME -password=password`

_Cluster Attack_

`python generate-safe-wordlist.py -users=/path/to/wordlist.txt -passwords=/path/to/wordlist.txt`

The generated wordlists can then be used in BurpSuite or elsewhere to execute the attack.
