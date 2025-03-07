# Scraping Data from Airbnb Delhi


import requests
import pandas as pd
from bs4 import BeautifulSoup

# getting the html from url.
hostname = "https://www.airbnb.co.in/"
url="https://www.airbnb.co.in/s/New-Delhi--India/homes?place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&refinement_paths%5B%5D=%2Fhomes"
response = requests.get(url=url)

# Making soup and parsing the collected html.
soup = BeautifulSoup(response.text, "lxml")

name_list = []
rate_list = []
reviews_list = []

while True:
    names = soup.find_all("div", {"class": "t1jojoys atm_g3_1kw7nm4 atm_ks_15vqwwr atm_sq_1l2sidv atm_9s_cj1kg8 atm_6w_1e54zos atm_fy_1vgr820 atm_7l_jt7fhx atm_cs_10d11i2 atm_w4_1eetg7c atm_ks_zryt35__1rgatj2 dir dir-ltr"})
    for n in names:
        name_list.append(n.text.strip())

    rates = soup.find_all("span", {"class": "_hb913q"})
    for r in rates:
        rate_list.append(r.text.strip())

    reviews = soup.find_all("span", {"class": "a8jt5op atm_3f_idpfg4 atm_7h_hxbz6r atm_7i_ysn8ba atm_e2_t94yts atm_ks_zryt35 atm_l8_idpfg4 atm_vv_1q9ccgz atm_vy_t94yts au0q88m atm_mk_stnw88 atm_tk_idpfg4 dir dir-ltr"})
    for review in reviews:
        reviews_list.append(review.text.strip())


    nextPage = soup.find("a", {"aria-label": "Next"})

    if nextPage: 
        nextPageLink = nextPage.get("href")
        completeNP = hostname + nextPageLink
        url = completeNP 
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
    else:
        print("No more Pages....")
        break

# we can add a logic checking that if len of any list is less then extend that list with dummy values



reviews_list.extend(["New"] * (len(name_list) - len(reviews_list)))
df = pd.DataFrame({"Name":name_list, "Prices":rate_list, "Rate&Reviews":reviews_list})
df.to_csv("D:\Jalaj-Python\PythonAutomation\BeautifulSoup\Airbnb-Delhi.csv")