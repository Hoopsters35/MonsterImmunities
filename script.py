import requests, bs4
base_url = 'http://runescape.wikia.com/wiki/Special:Search?query='

def get_immunity(soup, attr_name):
    attr = soup.select(f'span[title$="{attr_name}."] > img')
    if attr:
        return attr[0].get('alt')
    return 'Unknown'

while True:
    query = input('Enter boss name: ')
    query_link = "+".join(query.split())
    url = base_url + query_link
    rq = requests.get(url)
    search_soup = bs4.BeautifulSoup(rq.text, 'html5lib')
    boss_page_url = search_soup.select('ul.Results li.result a.result-link')[0].get('href')

    boss_page = requests.get(boss_page_url)
    boss_soup = bs4.BeautifulSoup(boss_page.text, 'html5lib')

    poison = get_immunity(boss_soup, 'poison')
    deflect = get_immunity(boss_soup, 'deflect')
    stun = get_immunity(boss_soup, 'stun')
    drain = get_immunity(boss_soup, 'drain')

    print(f'Poison immune: {poison}\nDeflect immunte: {deflect}\nStun immune: {stun}\nDrain immune: {drain}')