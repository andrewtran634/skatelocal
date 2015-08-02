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

import oauth2


GOOGKEY = '&key=AIzaSyBmu-0gJXE0CMNQRYnXeLCM_oN2_WXSR7E'
SEARCHURL = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query='
KEYWORDS = 'skate+shop+'

# Create your views here.
def index(request):
	return render(request, 'main/index.html')
def find(request):
	zcode = request.GET['zip']
	search = SEARCHURL + KEYWORDS + zcode + GOOGKEY
	page =  urllib.urlopen(search)
	jsonRaw = page.read()
	data = json.loads(jsonRaw)
	return render(request, 'main/results.html', {'data' : data, 'search' : search})
