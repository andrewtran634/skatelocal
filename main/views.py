from django.shortcuts import render
from lxml import html
import requests
import json
import argparse
import json
import pprint
import sys
import urllib
import urllib2
#import re
import oauth2


GOOGKEY = '&key=AIzaSyBmu-0gJXE0CMNQRYnXeLCM_oN2_WXSR7E'
SEARCHURL = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query='
KEYWORDS = 'skate+shop+'
#MATCH = re.compile("(BOARD)|((SKATE)(.))")
# Create your views here.
def index(request):
	return render(request, 'main/index.html')
def find(request):
	zcode = request.POST['location']
	search = SEARCHURL + KEYWORDS + zcode + GOOGKEY
	page =  urllib.urlopen(search)
	jsonRaw = page.read()
	data = json.loads(jsonRaw)

	shoplist = []
	infolist = []

	biglist = data['results']
	for shops in biglist:
		infolist = []
		infolist.append(shops['name'])
		infolist.append(shops['formatted_address'])
		#shops['formatted_address']
		shoplist.append(infolist)
	return render(request, 'main/results.html', {'shoplist' : shoplist})
