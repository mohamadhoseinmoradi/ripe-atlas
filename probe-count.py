import pycountry
import requests

probe_count_dict = {}

for country in pycountry.countries:
    url = f"https://atlas.ripe.net:443/api/v2/probes/?country_code={country.alpha_2}"
    with requests.get(url) as response:
        response = response.json()
    probe_count_dict[country.name] = [response["count"]]

sort_top_10 = sorted(probe_count_dict.items(), key= lambda item: item[1], reverse=True)[:10]}
print ("here are the top 10 countries hosting probes: ", *sort_top_10)
