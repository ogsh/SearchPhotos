import os
import time
import flickr
import urllib
from random import shuffle


# SETTINGS
flickr.API_KEY =  "input your flickr api key"
NUM_PHOTO = 10
KEYWORD = "sky"
LICENSE = "4"

MY_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(MY_DIR, 'images')
if os.path.exists(IMAGE_DIR):
	os.rename(IMAGE_DIR, "%s.bak-%s" % (IMAGE_DIR, time.strftime('%Y%m%d%H%M%S')))
os.makedirs(IMAGE_DIR)

if __name__ == '__main__':
	photos = flickr.photos_search(text=KEYWORD, per_page='10000', license = LICENSE);
	shuffle(photos)

	retr_count = 0
	num_photos = len(photos)
	for photo in photos:
		url = "http://farm" + photo.farm + ".static.flickr.com/" + photo.server + "/" + photo.id + "_" + photo.secret + "_b.jpg"
		photoname = photo.id + "_" + photo.secret + "_b"
		filename = os.path.join(IMAGE_DIR, '%s.jpg' % (photoname))
		file(filename, "wb+").write(urllib.urlopen(url).read())
		retr_count += 1
		print("%d/%d: %s %s retrieved. " % (retr_count, num_photos, os.path.basename(filename), url))
		if retr_count >= NUM_PHOTO:
			break
