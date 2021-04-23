import requests, os, bs4 

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    #TODO: Download the page
    print('Downloading image %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #TODO: find the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else: 
        comicUrl = 'https:' + comicElem[0].get('src')
        #download the image
        print('Downloading the image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    #TODO: save the image to ./xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(1000):
        imageFile.write(chunk)
    imageFile.close()
    #TODO: Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')


print('Done.')
