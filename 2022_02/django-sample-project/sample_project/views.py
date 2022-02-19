from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage
import json
import random


def read_json(file_):
    with open(file_, "r") as f:
        datastore = json.load(f)
    return datastore


quotes_file = staticfiles_storage.url("data/alan_watts_quotes.json")
quotes_json = read_json(quotes_file)


def get_quote_details(quoteid):
    return quotes_json["quotes"][quoteid]


def index(request):
    if request.method != "POST":
        return render(request, "index.html", {"quotes_": quotes_json})


def quotes(request):
    if request.method != "POST":
        no_of_quotes = len(quotes_json["quotes"])
        quote_num = random.randint(0, no_of_quotes - 1)
        quote = get_quote_details(quote_num)
        return render(request, "quotes.html", {"quotes_": quote})
