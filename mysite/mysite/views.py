from django.shortcuts import render
from django.template.loader import get_template
from .models import Player, Event
from datetime import datetime

def homepage_view(request):
    return render(request, 'mysite/homepage.html')

def submit(request):
    top_players = [None] * 8
    elimination_style = request.POST.get('elim_type')
    for index, player in enumerate(top_players):
        number = index+1
        name = request.POST.get(f"player{number}_name").strip()
        handle = request.POST.get(f"player{number}_handle").strip()
        if not handle.startswith('@'):
            handle = '@' + handle
        if elimination_style == 'double_elim':
            if number == 6:
                placement = 5
            elif number == 8:
                placement = 7
            else: 
                placement = number
        else:
            if number == 1 or number == 2 or number == 3:
                placement = number
            elif number == 4:
                placement = 3
            else: 
                placement = 5
        primChar = request.POST.get(f"player{number}_primary")
        primAlt = (request.POST.get(f"player{number}_alt"))[0:1]
        primary = f"static/images/renders/{primChar}/{primChar}_{primAlt}.png"
        secChar = request.POST.get(f"player{number}_secondary")
        secondary = None
        terChar = request.POST.get(f"player{number}_tertiary")
        tertiary = None
        customImage = request.POST.get(f"player{number}_custom")
        if not customImage == None:
            primary = customImage
            terChar = secChar
            secChar = primChar
        if not secChar == 'None':
            secondary = f"static/images/icons/{secChar}_icon.png"
            if not terChar == 'None':
                tertiary = f"static/images/icons/{terChar}_icon.png"
        player = Player.objects.create(player_name=name, player_handle=handle, player_placement=placement, primary_character=primary, secondary_character=secondary, tertiary_character=tertiary)
    date = datetime.strptime(request.POST.get('event_date'), '%Y-%m-%d').strftime('%m/%d/%Y').strip()
    if request.POST.get('event_type') == 'smashatuva':
        title = "Smash @ UVA " + request.POST.get('semester')[0:1] + date[-2:] + " #"
    else:
        title = "The CUT "
    title += request.POST.get('event_number')
    participants = request.POST.get('participants')
    if request.POST.get('redemption_check'):
        redempWinner = request.POST.get('redemption_name').strip()
        redempChar = request.POST.get('redemption_primary')
        redempAlt = request.POST.get('redemption_alt')[0:1]
        redempRender = f"static/images/renders/{redempChar}_{redempAlt}_redemption.png"
    if request.POST.get('side_check'):
        sideTitle = request.POST.get('side_event').strip()
        sideWinner = request.POST.get('side_name').strip()
    event = Event.objects.create(event_title=title, event_participants=participants, event_date=date, side_title=sideTitle, side_winner=sideWinner, redemption_winner=redempWinner, redemption_redner=redempRender)
    return constructGraphic(top_players, event)

def constructGraphic(top_players, event):
    #TODO: Actually implement this
    return None