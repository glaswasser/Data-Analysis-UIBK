# 1. write a pattern that matches IPv4-Addresses:


import re
import os

# extract a valid IP adress from a string:
test = "blabla this is an address: 192.68.100.1, and this is no valid address: 138.277.0.9"

ip = re.search('''(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)''', test)

print(ip.group(0))

# source: https://www.geeksforgeeks.org/python-program-to-validate-an-ip-address/



# 2. Write a pattern that matches all occurrences of the word “visit” (i.e. “visits”, “visited”...)

# directory containing text files:
directory = "/Users/alexanderheinz/Library/Mobile Documents/com~apple~CloudDocs/UIBK/Data Analysis 2/homework-1/"

# get file names
file_names = os.listdir(directory)

# get content
books = str()
for file in file_names:
    new = open(directory + file, "r").read()
    books = books + new

# now we want to detect the pattern of the word "visit"

result = re.findall(r"\s[Vv]isit[a-z]*", books)

# remove \n:
result = [word.replace('\n', '') for word in result]

print(result)



# Search in internet for a pattern for domain names.

# https://mkyong.com/regular-expressions/domain-name-regular-expression-example/
domain = "www.mkyong.com"

name = re.search("^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\\.)+[A-Za-z]{2,6}$", domain)

print(name.group(0))

print(re.search("^((?!-)[A-Za-z0-9-]{1,63}(?<!-)\\.)+[A-Za-z]{2,6}$", "mkyong,com"))



# Search in internet for a pattern for email addresses.
# https://stackoverflow.com/questions/8022530/how-to-check-for-valid-email-address

email = "glaswasser@gmail.com"

if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
    print("VALID MAIL ADDRESS")


# Find a pattern for Austrian phone numbers and replace it with the normalized way of phone numbers.
# (I.e. “0512 507-45010” should become “+43 (512) 507-45010”

number = "0512 507-45010"

def replace_number(number):

    digits = re.findall(r'\S+', number)

    digits[0] = re.sub(r"^0", r"+43 (", digits[0])

    digits[0] = re.sub(r"$", r")", digits[0])

    new_number = " ".join(digits)

    return new_number


print(replace_number(number))

print(replace_number("0532 15-9273"))

