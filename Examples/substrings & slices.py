name = "Jack Booth"

# substring_name = original_variable[start:stop:step] start = beginning of substring inclusive, stop = end of substring
# exclusive, step = default is 1, every x character (negative is reverse)
first_name = name[:4]
last_name = name[5:]
silly_name = name[::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(silly_name)
print(reversed_name)

website_a = "https://google.com"
website_b = "https://wikipedia.com"

# slice(start, stop, step) start = beginning of slice inclusive, stop = end of slice exclusive (negative is counting
# back from end of string), step = default is 1, every x character
website_slice = slice(8, -4)

print(website_a[website_slice])
print(website_b[website_slice])
