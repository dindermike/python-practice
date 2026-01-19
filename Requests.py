# Various Request Operations
from http.client import HTTPConnection

# Read contents of a generic URL GET Response
print('Generic GET Connection Response')

print('www.mikedinder.com')
conn = HTTPConnection('www.mikedinder.com')
conn.request('GET', '/')
result = conn.getresponse()
contents = result.read()

print(contents)

print('www.amazon.com')
conn = HTTPConnection('www.amazon.com')
conn.request('GET', '/')
result = conn.getresponse()
contents = result.read()

print(contents)

print('www.google.com')
conn = HTTPConnection('www.google.com')
conn.request('GET', '/')
result = conn.getresponse()
contents = result.read()

# print(contents)

print('--------------------------------------------------')
