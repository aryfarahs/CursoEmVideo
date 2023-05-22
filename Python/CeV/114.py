import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com')
except urllib.error.URLError:
    print('Youtube não está dísponível!')
else:
    print('Youtube está funcionando!')