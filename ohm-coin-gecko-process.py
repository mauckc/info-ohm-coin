import urllib, json, requests, time
#import inflect

headers = {
    'accept': 'application/json',
}

params = (
    ('localization', 'en'),
)

response = requests.get('https://api.coingecko.com/api/v3/coins/ohm-coin', headers=headers, params=params)
#response = requests.get('https://api.coingecko.com/api/v3/coins/ohm-coin', headers=headers)
print("Status Code: " + str(response.status_code))
print(response.headers)

with open('response-data.json', 'w') as outfile:
    json.dump(response.json(), outfile)

time.sleep(1)

# Curl command to retrieve information
#curl -X GET "https://api.coingecko.com/api/v3/coins/ohm-coin" -H "accept: application/json" -o ohmcexchanges.json
# Read ticker information from coingecko and ask user to input data field
# information by specific coins using their coin index (i.e. Ethereum = 1027)

# Set up coin interface index json functionality
json_coin_index_data = open("ohmcurlinfo.json").read()
coin_index_data = json.loads(json_coin_index_data)
print(len(coin_index_data.keys()))
for x in (1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20):
    print(str(coin_index_data.keys()[x]))
    print(coin_index_data[str(coin_index_data.keys()[x])])
    print(len(coin_index_data.keys()[x]))


last_updated = coin_index_data['last_updated']
developer_data = coin_index_data['developer_data']
community_data = coin_index_data['community_data']
community_data

print(last_updated)
print(developer_data)
print(community_data)

#print(coin_index_data['description'])
#user_coin_choice = raw_input("What coin would you like info for?: ")
#coinkeys = coin_index_data.keys()
for key in coin_index_data.keys():
    print(key)

user_key_choice = raw_input("What key would you like to search for??: ")

if user_key_choice in coin_index_data.keys():
    #getticker(coin_index_data[user_coin_choice])
    for key in coin_index_data.keys():
        if key in user_key_choice:
            print(key)
            print(coin_index_data[key])
else:
    print("That is not a valid choice. Please use full name with caps. (i.e. Ethereum)\nPlease Try again.\n")
    user_key_choice = raw_input("What key would you like to search for??: ")
    if user_key_choice in coin_index_data.keys():
        print(coin_index_data[user_key_choice])
    else:
        print("I'm sorry that is still not an accepable key name")


'''
for key in coin_index_data.keys():
    print(key)
    print(coin_index_data[key])
'''
