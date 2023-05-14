import requests
import json


def get_metadata(searchkey="all"):
    metadata_url = "http://169.254.169.254/metadata/instance?api-version=2021-02-01"
    headers = {'Metadata': 'true'}
    response = requests.get(metadata_url, headers=headers)

    if response.status_code == 200:
        # if True :
        metadata = response.json()
        # with open('sampledata.json') as f: # for test
        #    metadata = json.load(f) # for test
        if searchkey != "all":
            value = metadata.get(searchkey)
            if value:
                print(searchkey, ":", value)
                return value
            else:
                return "key not found"
        else:
            return metadata
    else:
        print("Failed to retrieved to code with API : ", response.status_code)


# example call function
print(get_metadata("network"))
