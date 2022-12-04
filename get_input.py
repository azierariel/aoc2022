import requests


def request_input(day: int, session_id=""):
    cookies = {"session": session_id}
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
        'Referer':'https://adventofcode.com/2022/day/2',
        'Cookie':f'session={session_id}'
    }
    url = f"https://adventofcode.com/2022/day/{day}/input"
    r = requests.get(url=url, cookies=cookies, headers=headers)
    return r.text
