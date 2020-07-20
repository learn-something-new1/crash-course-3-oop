import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success Response= {response.status_code}')
        #print(f'Content {response.text}')
        # instant = nama lain dari object dari class
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'hasil Pemanggilan {url}')
        print(f'Title: {soup.title.string}')
    else:
        print(f'Woops ada kesalahan {response.status_code}')
#    print(f'Success', response)
except Exception as e:
    print(f'There is a error{e}')
 #   print('There is a error', e)
print('Program ended')