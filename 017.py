# -*- coding:utf-8 -*-
import re
from urllib import request
from urllib import parse
import pdb
import bz2
def linkedcookielist(seed='12345'):
     #pdb.set_trace()
    result =''
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php' \
            '?busynothing='
    nextnothing = re.compile('the next busynothing is (\d+)')
    cookievalue = re.compile('info=([^;]+);').search
    while True:
        resp = request.urlopen(url + seed)
        next = resp.read()
        #print(next)
        cookie = resp.getheader('Set-Cookie')
        if cookie and cookievalue(cookie):
            #print(cookie)
            result +=cookievalue(cookie).group(1)
        try:
            seed = nextnothing.search(next.decode('utf-8')).group(1)
        except:
            #pdb.set_trace()
            #result.replace('+','20%')
            #result=parse.unquote_bytes(result)
            #f=open('017-pass.bz','wb')
            #f.write(result.encode('utf-8').decode('unicode_escape').encode('latin1'))
            #f.close
            return result

another_message=linkedcookielist()
pdb.set_trace()
print(bz2.decompress(parse.unquote_to_bytes(another_message.replace('+', '%20'))).decode('utf-8'))