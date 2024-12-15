import requests

# Define the URL
url = 'https://www.tanitjobs.com/'

# Define the headers (removing pseudo-headers)
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': '_ga=GA1.1.1758304557.1731253357; fpestid=4DnpEWxQyOUaWw-52ZJMiYHeRDkQPmbDfpxb5xLF9XC4H9YSWllV5x3d4Wg-EIK3mGHi9w; _cc_id=cfd82f5a98f2ec2573f4fcfd41859095; panoramaId_expiry=1733133042342; panoramaId=0a7814d66a3d777e4675c18f4d7016d53938c6c8d09edcf8a18691596a374f9f; panoramaIdType=panoIndiv; cf_clearance=MEP.xvMSkf8MUgBC_gdDezoDh1qk8dJE5pX5gf91DME-1732662705-1.2.1.1-IITVr1p33FbfpmOkJ6VfseBtUpfvkWZtzfr_KRpTd.yFvX_s_syuE6XYZ4qtqcGoeWRxay2Senx0i3UOQsC_YEft9._SopGbQIHuWUj_6hIjuuvksb31mdCytx_3UBFWmASFGpSG_E5dE8BFftVtYFKtkEImxWzHKykosPHZrxtO7q4mpQ2olR8oDGPRARfLanWURyJ82LvfU73RL9KXCZOI0REU1M_5JTsTjPtBLDmNg51_oZMCGQqSdalOJCxSMyOLl7K1Rl4FmoY8hHrCqKW5dYm_10YuRO39YsFSWwqw.ZeD7dD92wNmePpIImhLOEjli7wHMmAzVI3GDmb.RyThV.52YHVQV2bJSkAShxzDxhfxh25wukISX00OeNLue4AIdCHeM9U6TtEjbXHOXxGp1hTkKdEbNAKdBqdSwTUJj66.VuWR2BMq3adN6e3O; PHPSESSID=m1oh1596hr1gj08colf39bq5qp; _ga_ZL9LBW1J59=GS1.1.1732667821.6.0.1732667821.0.0.0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-arch': 'x86',
    'sec-ch-ua-bitness': '64',
    'sec-ch-ua-full-version': '131.0.6778.86',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.86", "Chromium";v="131.0.6778.86", "Not_A Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': 'Windows',
    'sec-ch-ua-platform-version': '15.0.0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

# Make the HTTP request
response = requests.get(url, headers=headers)

# Print the response text (HTML content)
print(response.text)
