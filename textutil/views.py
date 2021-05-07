from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter

#def index(request):
#   #return HttpResponse('''<h1>FB</h1> <a href="https://www.facebook.com/login.php"> Facebook</a>''')
#  return HttpResponse('''<h1>WP</h1> <a href="https://www.whatsapp.com/"> whatsapp</a>''')

#def about(request):
#    return HttpResponse("Welcome to my website") 

#def openfile(request):
#    file=open("textutil/1.txt.txt",'r')
#    return HttpResponse(file.read())'''

def index(request):
    return render(request,'index.html')
    #return HttpResponse("Home")

    

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('xyz','off')
    fullcaps=request.POST.get('fullcaps','off')
    newline=request.POST.get('newline','off')
    space=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')

    tpo=djtext
    abc=""
    if removepunc == "on":
        punct= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        new=""
        for char in tpo:
            if char not in punct:
                new=new+char        
        params={'abc':"Removing punctuations",'mno':new}
        tpo=new
        abc=abc+"Remove punc"
        #return render(request,'analyze.html',params)
    if(fullcaps=="on"):
        new=""
        new=tpo.upper()
        params={'abc':"Capital Function",'mno':new}
        tpo=new
        abc=abc+"Capital"
        #return render(request,'analyze.html',params)
    # Previous code      
    if(newline=="on"):
        new=""
        for char in tpo:
            if char != '\n' and char!='\r':
                new=new + char
        params={'abc':"Remove new line",'mno':new}
        tpo=new
        abc=abc+"Remove new line"
        #return render(request,'analyze.html',params) 
    if(space=="on"):
        new=""
        for i in range(0,len(tpo)):
            if tpo[i] !=" ":
                new=new+tpo[i]
        params={'abc':"Remove spaces",'mno':new}
        tpo=new
        abc=abc+"Remove spaces"
       # return render(request,'analyze.html',params) 
    '''elif(charcount=="on"):
        d=dict()
        for line in tpo:
            line=line.strip()
            line=line.lower()
            words=line.split(" ")
        for word in words:
            if word in d:
                d[word]=d[word]+1
            else:
                d[word]=1    
        params={'abc':"Character Counter",'mno':d}
        return render(request,'analyze.html',params)                
    else:
        return HttpResponse('error')'''
    if removepunc == "on"  or fullcaps == "on" or newline== "on" or space=="on":
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("there is some error")     

def about(request):
    return render(request,'about.html')   

def contact(request):
    return render(request,'contact.html')       

