from django.shortcuts import render, HttpResponse

topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'model', 'body':'Model is ..'}
]

def HTMLTemplate(article):
    
    global topics

    ol = ''

    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'

    return f'''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
        {article}
    </body>
    </html>
    '''

def index(request):

    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''

    return HttpResponse(HTMLTemplate(article))

def create(request):
    return HttpResponse('Creat')

def read(requestm,id):

    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'

    return HttpResponse(HttpResponse(article))

