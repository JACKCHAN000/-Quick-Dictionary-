# %%
import urllib.request as req
from urllib.parse import quote
from bs4 import BeautifulSoup

# %%


def check(word):
    url = 'https://www.hkcards.com/cj/cj-char-'+quote(word)+'.html'
    request = req.Request(url, headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    })
    with req.urlopen(request) as response:
        html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.findAll('meta')
    code = (data[-2]['content'].split("。 "))[0].split("【倉頡碼】")[-1]
    """img_url = "https://www.hkcards.com/img/cj/"+quote(word)+'.html'
    img = Image.open(BytesIO((requests.get(img_url)).content))"""

    return code


# %%
words = "天地玄黃，宇宙洪荒。"
for i in words:
    print(i+": "+check(i))

# %%
