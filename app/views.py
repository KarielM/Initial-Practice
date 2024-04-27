from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
import random

# Create your views here.

def hey_you(request:HttpRequest, str0:str) -> HttpResponse:
   return HttpResponse(f'Hey {str0}')

def how_old(request:HttpRequest, end:int, birthyear:int) -> HttpResponse:
   return HttpResponse(end - birthyear)

def can_i_take_your_order(request:HttpRequest, burgers:str, fries:str, drinks:str) -> HttpResponse:
   return HttpResponse((burgers * 4.5)+(fries * 1.5)+(drinks*1.0))


















def hello_world_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World!")

def hello_nate(request: HttpRequest, name:str) -> HttpResponse:
    return HttpResponse(f"Hello {name}!")

def roll_die_view(request: HttpRequest, sides:int) -> HttpResponse:
    roll = random.randint(1,sides)
    return HttpResponse(roll)

def random_between_view(request: HttpRequest, lo:int, hi:int) -> HttpResponse:
    return HttpResponse(random.randint(lo,hi))

def add_view(request:HttpRequest, x:int, y:int):
    return HttpResponse(x + y)

def test_pop(request:HttpRequest) -> HttpResponse:
    list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    list.pop(list.index('c'))
    return HttpResponse(list)

def hey_you(request:HttpRequest, name:str) -> HttpResponse:
  return HttpResponse(f"Hello, {name}!")

def how_old(request:HttpRequest,end:int,birthyear:int) -> HttpResponse:
  return HttpResponse(end - birthyear)

def can_i_take_your_order(request:HttpRequest, burgers:int, fries:int, drinks:int) -> HttpResponse:
  return HttpResponse((burgers*4.5)+(fries*1.5)+(drinks*1.0))

def near_hundred(request:HttpRequest, n:int) -> HttpResponse:
  return HttpResponse(bool(abs(100-n)<=10) or bool(abs(200-n)<=10))

def string_splosion(request:HttpRequest, str0:str) -> HttpResponse:
  result = ''
  for i in range (len(str0)):
     result += str0[:i+1]
  return HttpResponse(result)

def cat_dog(request:HttpRequest, str0:str) -> HttpResponse:
  count_cat = 0
  count_dog = 0
  for i in range(len(str0)-2):
    if str0[i:i+3] == 'dog':
      count_dog += 1
    if str0[i:i+3] == 'cat':
      count_cat += 1
   
  return HttpResponse(bool(count_cat == count_dog))

def lone_sum(request:HttpRequest, a:str, b:str, c:str):
  if a != b and b != c and a != c:
    return HttpResponse(a+b+c)
  else:
    if a == b == c:
      return HttpResponse(0)
    elif a == b:
      return HttpResponse(c)
    elif a == c:
      return HttpResponse(b)
    else: 
      if c == b:
        return HttpResponse(a)
