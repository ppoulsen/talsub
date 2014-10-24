from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
import json

from data.dao import EpisodeDAO

def home(request):
    return render(request, 'index.html')


def episode_list(request):
    """
    Gets all the episodes with correct language code from GET parameter
    :param request: HttpRequest bearing language code in GET
    :return: JSON of all TAL titles, audio links, and episode number
    """
    if request.method != 'GET':
        return HttpResponseNotAllowed(request)

    langCode = request.GET['lang']

    dao = EpisodeDAO()
    dtos = dao.find('number', 'title', 'audio', languages=langCode).order_by('number')
    clean_vals = []
    for dto in dtos:
        clean_vals.append({
            'number': dto.number,
            'title': dto.title,
            'audio': dto.audio,
        })

    ret = json.dumps(clean_vals)

    return HttpResponse(ret, content_type='application/json')