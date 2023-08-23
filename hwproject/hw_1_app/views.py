from django.shortcuts import render
from django.http import HttpResponse
import logging
from datetime import date, datetime

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    html_text = "<h1 align=center>This is my first website</h1>" \
                "<h2>A link to the about me page will appear here soon</h2>" \
                "<h2>Here will be a link to examples of my work</h2>"                
    return HttpResponse(html_text)

def about(request):
    logger.info('about page accessed')
    md = datetime(1986, 3, 18)
    today = date.today()

    html_text = "<p><h1 align=center>Hi, I'm Kite</h1></p>" \
                f"<p><h2>I'm {today.year - md.year - ((today.month, today.day) < (md.month, md.day))} years old</h2>" \
                "<h2>Someday I will become a good programmer</h2></p>"                 
    return HttpResponse(html_text)