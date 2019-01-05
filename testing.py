import urllib
from urllib.request import urlopen
from link_finder import LinkFinder
html_string = ''
try:
    req = urllib.request.Request('https://www.giki.edu.pk/AboutGIKI/VisionandMission', headers={'User-Agent': "Magic Browser"})
    response = urlopen(req)
    if 'text/html' in response.getheader('Content-Type'):
        html_bytes = response.read()
        html_string = html_bytes.decode("utf-8")
    finder = LinkFinder('https://www.giki.edu.pk/','https://www.giki.edu.pk/AboutGIKI/VisionandMission')
    finder.feed(html_string)

except Exception as e:
        print(str(e))
