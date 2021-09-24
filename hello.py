#!/usr/bin/env python3

import os, json
 
# printing environment variables
print(os.environ)

# printing as json
json_object = json.dumps(dict(os.environ), indent = 1)
print(json_object)

# print(os.environ["QUERY_STRING"])
# Print query strings if any
# print(os.environ["BROWSER"])

# Print out browser info
if "HTTP_USER_AGENT" in os.environ.keys():
    print('-----------------')
    print(os.environ["HTTP_USER_AGENT"])



