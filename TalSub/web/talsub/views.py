from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
import json

from data.dao import EpisodeDAO
from model.episode import Episode
from shared.converters import DTOConverter


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


def transcript(request):
    """
    Returns full transcript for given episode number and lang
    :param request: HttpRequest bearing language code and episode number
    :return: JSON of episode transcript
    """
    if request.method != 'GET':
        return HttpResponseNotAllowed(request)

    langCode = request.GET['lang']
    number = int(request.GET['episode'])

    # Get episode that matches language and number requirement
    dao = EpisodeDAO()
    dto = dao.find(languages=langCode, number=number).first()

    # Convert to model and strip other languages
    model = DTOConverter().from_dto(Episode, dto)
    model.transcripts = [t for t in model.transcripts if t.language == langCode]

    # Convert model to json
    ret = model.to_json()

    return HttpResponse(ret, content_type='application/json')
