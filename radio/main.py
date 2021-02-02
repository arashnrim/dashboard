import sys
from pathlib import Path
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver, common

from styles import Style

listOfURLs = ['class-95', 'gold-905', '987', 'cna938', 'symphony-924', 'yes-933', 'love-972', 'capital-958',
              'warna-942', 'ria-897', 'oli-968']

listOfNames = ['Class 95', 'Gold 905', '987', 'CNA 938', 'Symphony 92.4', 'Yes 933', 'Love 972', 'Capital 958',
               'Warna 942', 'Ria 897', 'Oli 968']

chromedriver = '/usr/local/bin/chromedriver'

if not Path(chromedriver).is_file():
    print("The Chrome driver is required for this feature. Please install it at /usr/local/bin/ and try again.")
    sys.exit()

while True:
    print("{bold}Radio{end}".format(bold=Style.BOLD, end=Style.END))
    print(
        "{blue}!{end} {bold}Warning:{end} This feature will open up several instances of Chrome.".format(
            blue=Style.BLUE, end=Style.END, bold=Style.BOLD))
    result = input("Continue? Type y for yes, n for no: ")
    if result == "y":
        break
    elif result == "n":
        sys.exit()

for i in range(len(listOfURLs)):
	driver = webdriver.Chrome(chromedriver)
	driver.implicitly_wait(90)
	driver.get('https://www.melisten.sg/radio/{}'.format(listOfURLs[i]))

	soup = BeautifulSoup(driver.page_source, 'lxml')

	ans = soup.find_all('img', class_='mr-2 lazy0 lazy-loaded')

	for x in ans:
		print("{}: ".format(listOfNames[i]), end = "")
		print(x['alt'])
		driver.close()
		break            break
