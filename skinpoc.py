import requests
ssid = input('ssid: ')
newskin = input('url to new skin: ')
url1 = ("https://api.minecraftservices.com/minecraft/profile/skins")
headers = {
    'Authorization': f"Bearer {ssid}",
    'Content-Type': 'application/json',
}
json_headers = {
    'variant': 'classic',
    'url': f"{newskin}",
}
resp = requests.post(url1, headers=headers, json=json_headers)
print(resp.status_code)
print(resp.text)
print(resp.json)