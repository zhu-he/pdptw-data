import os
import re
import shutil
from urllib.request import urlopen, Request

base_url = "https://www.sintef.no"
index_path = "/projectweb/top/pdptw/li-lim-benchmark/%s-customers/"
num_customers_list = ["100", "200", "400", "600", "800", "1000"]
pattern = re.compile('"(/contentassets/.*?/(l(c|r|rc)\d+(_\d+_\d+)?).*?\.txt)"')
headers = {"User-Agent": ""}

for num_customers in num_customers_list:
    url = base_url + index_path % num_customers
    with urlopen(Request(url, headers=headers), timeout=10) as response:
        body = response.read().decode()
    for path, instance_name, *_ in pattern.findall(body):
        print(path)
        file_path = os.path.join(num_customers, instance_name + ".sol")
        with urlopen(Request(base_url + path, headers=headers), timeout=10) as response:
            with open(file_path, "wb") as file:
                shutil.copyfileobj(response, file)
