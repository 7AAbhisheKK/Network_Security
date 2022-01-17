from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'POST':
        temp = ""
        text1 = request.POST['text']
        text1 = text1.lower()
        encryption = True
        if 'cypher' in request.POST:
            for x in text1:
                temp = temp + chr(25-ord(x)+2*ord('a'))
            print(temp)
        if 'decypher' in request.POST:
            for x in text1:
                temp = temp + chr(25-ord(x)+2*ord('a'))
            print(temp)
            encryption = False
       
        return render(request, 'result.html',{"result":temp,"encryption":encryption})
    else:
        return render(request, 'home.html',{"message":"hello"})