import bz2
import urllib.parse
another_message = 'BZh91AY%26SY%80%F4C%E8%00%00%02%13%80%40%00%04%00%22%E3%8C%00+%00%22%004%D0%40%D04%0C%B7%3B%E6h%B1AIM%3D%5E.%E4%8Ap%A1%21%01%E8%87%D0'
print(bz2.decompress(urllib.parse.unquote_to_bytes(another_message.replace('+', '%20'))).decode('utf-8'))
