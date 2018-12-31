from django.shortcuts import render
from django.http import HttpResponse
import requests, urllib
import json
# Create your views here.
def index(request):
    url = ("https://facebook.github.io/react-native/movies.json")
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    print (data)
    data_title = [];
    data_id = [];
    main_data = zip(data_title, data_id)
    for i in data['movies']:
        data_id.append(i['id'])
        data_title.append(i['title'] + " " + i['releaseYear'])
        print (i['title'])
    return render(request, 'index.html', {'allData': main_data})