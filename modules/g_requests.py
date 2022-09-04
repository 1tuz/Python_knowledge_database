import grequests

sites = ["https://www.yandex.ru" for x in range(10)]
response = (grequests.get(url) for url in sites)
resp = grequests.map(response)

for num, r in enumerate(resp):
    print(f"{num} - {r.status_code} - ")
