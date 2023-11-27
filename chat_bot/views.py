from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import auth
import os
# from openai import OpenAI
import requests

# client = OpenAI(
#     api_key = "nulll"
# )

# create a function to ask openAI
# def askOpenAI(message):
#     response = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": message,
#         }
#     ],
#     model="gpt-3.5-turbo",
# )   
#     print(response)
#     answer = response.choices[0].message.content
#     return answer


# openai API key exhausted, use rapidAPI

def askRapidChatGPT(message):
    url = os.environ.get('RAPID_API_HOST')
    payload = {
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ],
        "temperature": 1
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": os.environ.get('RAPID_API_KEY'),
        "X-RapidAPI-Host": "chatgpt53.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    answer = response.json()['choices'][0]['message']['content']
    print(answer)
    return answer




# Create your views here.
def test(request):
    data = {'name':'Ryo','age':'21'}
    return JsonResponse(data)

def home(request):
    return render(request, 'index.html')
def chatbot(request):
    if request.method == "POST":
        message = request.POST.get('message')
        response = askRapidChatGPT(message)
        
        return JsonResponse({'response': response, 'message':message})
    return render(request, 'chatbot.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)

def signup(request):
    return render(request, 'signup.html')
