import re
from urllib import request
from urllib import parse
import pdb
def linkedcookielist(seed='12345'):
     #pdb.set_trace()
     result = ""
     url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php' \
             '?busynothing='
     nextnothing = re.compile('the next busynothing is (\d+)')
     cookievalue = re.compile('info=([^;]+);').search
     while True:
         resp = request.urlopen(url + seed)
         next = resp.read()
         cookie = resp.getheader('Set-Cookie')
         if cookie and cookievalue(cookie):
             result += parse.unquote_plus(
                 cookievalue(cookie).group(1))
         try:
             seed = nextnothing.search(next).group(1)
         except:
             return result
print(linkedcookielist())