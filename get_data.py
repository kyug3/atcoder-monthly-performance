import requests
import json
from collections import defaultdict

user = "Eguy"
url = "https://atcoder.jp/users/" + user + "/history/json"


def get_data(url):
    r = requests.get(url)
    data = r.json()
    data_dict = defaultdict(list)
    for x in data:
        if not x['IsRated']:
            continue
        month = x["EndTime"][:7]
        data_dict[month].append(x["Performance"])

    data_list = [[] for _ in range(len(data_dict))]
    for i, (key, values) in enumerate(data_dict.items()):
        data_list[i].append(key)
        data_list[i].append(len(values))
        data_list[i].append('{:.2f}'.format(sum(values) / len(values)))
        data_list[i].append(max(values))
        data_list[i].append(min(values))
    
    data_list.sort(reverse=True)

    return data_list

if __name__ == "__main__":
    print(get_data(url))
    