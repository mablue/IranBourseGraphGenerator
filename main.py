import requests

date = '13990507'
url = 'http://members.tsetmc.com/tsev2/excel/MarketWatchPlus.aspx?d=' + date
r = requests.get(url, allow_redirects=True)

open(date+'.xlsx', 'wb').write(r.content)




