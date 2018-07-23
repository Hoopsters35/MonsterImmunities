import requests, bs4
base_url = 'http://runescape.wikia.com/wiki/Special:Search?query='
while True:
    query = input('Enter boss name: ')
    query_link = "+".join(query.split())
    url = base_url + query_link
    rq = requests.get(url)
    search_soup = bs4.BeautifulSoup(rq.text, 'html5lib')
    boss_page_url = search_soup.select('ul.Results li.result a.result-link')[0].get('href')

    boss_page = requests.get(boss_page_url)
    boss_soup = bs4.BeautifulSoup(boss_page.text, 'html5lib')

    poison = boss_soup.select('span[title$="poison."] > img')[0].get('alt')
    deflect = boss_soup.select('span[title$="deflect."] > img')[0].get('alt')
    stun = boss_soup.select('span[title$="stun."] > img')[0].get('alt')
    drain = boss_soup.select('span[title$="drain."] > img')[0].get('alt')

    print(f'Poison immune: {poison}\nDeflect immunte: {deflect}\nStun immune: {stun}\nDrain immune: {drain}')