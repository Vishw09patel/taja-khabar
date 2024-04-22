from django.shortcuts import render
import requests
# Create your views here.
def indexpage(request):
    # search_results = []
    #
    # # Handle search query
    # query = request.GET.get('query')
    # if query:
    #     # Perform search across all categories
    #     categories = ['sports', 'business', 'politics', 'science', 'entertainment', 'automobile']
    #     for category in categories:
    #         url = f"https://inshortsapi.vercel.app/news?category={category}"
    #         response = requests.get(url)
    #         data = response.json()["data"]
    #         # Filter data for articles containing the search query in title or content
    #         filtered_data = [article for article in data if
    #                          query.lower() in article['title'].lower() or query.lower() in article['content'].lower()]
    #         search_results.extend(filtered_data)
    #
    # context = {
    #     'news_articles': search_results
    # }
    return render(request,'index.html')

def sports(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=sports")
    dataurl = url.json()
    mydata = dataurl["data"]
    context = {
        "sportsdata": mydata
    }
    return render(request,'sports.html',context)

def business(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=business")
    dataurl = url.json()
    mydata = dataurl["data"]
    context = {
        "businessdata": mydata
    }
    return render(request,'business.html',context)

def politics(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=politics")
    dataurl = url.json()
    mydata = dataurl["data"]
    context = {
        "politicsdata": mydata
    }
    return render(request,'politics.html',context)

def science(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=science")
    dataurl = url.json()
    mydata = dataurl["data"]
    context = {
        "sciencedata": mydata
    }
    return render(request,'science.html',context)

def entertainment(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=entertainment")
    dataurl = url.json()
    mydata = dataurl["data"]
    context = {
        "entertainmentdata": mydata
    }
    return render(request,'entertainment.html',context)

def Automobile(request):
    url = requests.get("https://inshortsapi.vercel.app/news?category=automobile")
    dataurl = url.json()
    mydata = dataurl["data"]
    context = {
        "Automobiledata": mydata
    }
    return render(request,'Automobile.html',context)


# views.py

from django.shortcuts import render
from .models import *  # Import your NewsArticle model


# def index(request):
#     # Get all news articles
#     news_articles = .objects.all()
#
#     # Handle search query
#     query = request.GET.get('query')
#     if query:
#         # Filter news articles based on the search query
#         news_articles = news_articles.filter(title__icontains=query)
#
#     context = {
#         'news_articles': news_articles
#     }
#     return render(request, 'index.html', context)
