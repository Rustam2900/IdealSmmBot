import requests
import json

# API URL
api_url = 'https://smmstone.com/api/v2'

# API Key
api_key = '2ba7b0c55a957dc7dbf2caa5e1604031'
# So'rov ma'lumotlari
query_params = {
    'key': api_key,
    'action': 'services'
}

# So'rovni jo'natish
response = requests.get(api_url, params=query_params)
print(response.text)
# Javobni tekshirish
# try:
#     response.raise_for_status()  # HTTP xatoliklarini qaytaradi
#     data = response.json()  # JSON formatdagi javobni o'qish
#     print(json.dumps(data, indent=4))  # JSON ma'lumotlarini ekranga chiqarish
# except requests.exceptions.HTTPError as errh:
#     print("HTTP xatolik:", errh)
# except requests.exceptions.JSONDecodeError as errj:
#     print("JSON tahlil xatoligi:", errj)
# except Exception as err:
#     print("Xatolik:", err)
