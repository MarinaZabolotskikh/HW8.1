import requests

url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
heroes = ["Hulk", "Captain America", "Thanos"]
response = requests.get(url = url)
print(response)
res = response.json()
smart_dict = {}
for dictionary in res:
    for hero in heroes:
        if hero == dictionary["name"]:
            smart_dict[hero] = dictionary["powerstats"]["intelligence"]
            smart_hero = max(smart_dict.values())
def get_hero(smart_dict, value):
    for k, v in smart_dict.items():
        if v == value:
            return k
print(smart_dict)
print(f"Самый умный герой: {get_hero(smart_dict, smart_hero)}")