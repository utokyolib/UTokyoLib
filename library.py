import requests
from bs4 import BeautifulSoup

class LibraryError(Exception):
    pass

def fetch_opening_info(libraryType, year=None, month=None, day=None):
    if year and month:
        url = f"https://opac.dl.itc.u-tokyo.ac.jp/opac/calendar/?lang=0&countercd={libraryType}&date={year}-{month:02}"
    else:
        url = f"https://opac.dl.itc.u-tokyo.ac.jp/opac/calendar/?lang=0&countercd={libraryType}"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')


    style = None

    calendar_table = soup.find('table', {'class': 'lib_calendar'})
    for elem in calendar_table.find_all('td'):
        if elem.get_text().strip() == str(day):
            style = elem.get('style')
            break

    if not style:
        raise LibraryError("開館時間の style が見つかりません")

    
    opening_type = None
    opening_info = None

    remark_table = soup.find('table', {'class': 'remarks'})
    for elem in remark_table.find_all('tr'):
        td_list = elem.find_all('td')

        if td_list[0].get('style') == style:
            opening_type = td_list[0].get_text().strip()
            opening_info = td_list[1].get_text().strip()
            break


    if opening_type and opening_info:
        return (opening_type, opening_info)
    else:
        raise LibraryError("開館時間の style に対応する情報が見つかりません")