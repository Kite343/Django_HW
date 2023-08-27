from django.shortcuts import render

from django.http import HttpResponse
import logging
from datetime import date, datetime

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    html_text = "<h1 align=center>This is my first website</h1>" \
                "<h2>there will be a store here.... maybe....</h2>" \
                                
    return HttpResponse(html_text)
