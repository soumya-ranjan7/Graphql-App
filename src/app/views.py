from django.shortcuts import render
import requests
import json 


def index(request):
    context = {"response":"false"}
    url = 'https://api.github.com/graphql'
    headers = {"Authorization" :"token <Github Token>"}
    query = {}

    if(request.method=="POST"):
      
        query["query"]="""{
  user(login: "%s"){
    name
    bio
    email
    followers(){
      totalCount
    }
    repositories(first: 10, isFork: false){
    
      nodes{
          name
          url
          description
          primaryLanguage{
            name
          }
      }
    }
    
    }
 }""" % request.POST["username"]

        data = requests.post(url=url, json=query, headers=headers)
        data = json.loads(data.text)
        context['details'] = data['data']['user']
        context['response'] = "true"
    return render(request,'app/index.html',context)