from django.shortcuts import render
from .models import Player, Event
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import os

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
    if title.startswith("Smash"):
        constructSmashAtUVA(top_players, event)
    else:
        constructCUT(top_players, event)
    return None #TODO: DELETE THIS LINE WHEN FINISHED
    return render(request, 'homepage.html', {
        "graphic": "success"
    })

def constructSmashAtUVA(top_players, event):
    graphic = Image.new("RGB", (1920,1080))
    start_color = (35, 45, 75)
    end_color = (18, 24, 40) 
    for y in range(1080):
        color = (
            int(start_color[0] + (end_color[0] - start_color[0]) * y / 1080),
            int(start_color[1] + (end_color[1] - start_color[1]) * y / 1080),
            int(start_color[2] + (end_color[2] - start_color[2]) * y / 1080)
        )
        for x in range(1920):
            graphic.putpixel((x, y), color)
    draw = ImageDraw.Draw(graphic)
    font = None #TODO: ADD THIS
    
    #TODO: ADD BACKGROUND IMAGE

    #TODO: ADD TITLE

    graphic = addPlayers(top_players, event, graphic, draw, font)
    addSideBrackets(event, graphic, draw, font)
    return None #TODO: DELETE THIS LINE WHEN DONE
    graphic.save("graphic.png")

def constructCUT(top_players, event):
    graphic = Image.new("RGB", (1920,1080))
    draw = ImageDraw.Draw(graphic)
    font = None #TODO: ADD THIS

    #TODO: ADD BACKGROUND IMAGE

    #TODO: ADD TITLE
    
    addPlayers(top_players, event, graphic, draw, font)
    addSideBrackets(event, graphic, draw, font)
    return None #TODO: DELETE THIS LINE WHEN DONE
    graphic.save("graphic.png")


def addPlayers(top_players, event, graphic, draw, font):
    for index, player in enumerate(top_players):
        #TODO: Add Player Images
        return None

    rectCoords = [[35, 770, 632, 937],
          [683, 564, 1050, 666],
          [1100, 564, 1467, 666],
          [1517, 564, 1884, 666],
          [683, 862, 959, 937],
          [997, 862, 1272, 937],
          [1302, 862, 1578, 937],
          [1609, 862, 1884, 937]]
    for index, coord in enumerate(rectCoords):
        border_color = (255, 255, 255)
        x1, y1 = rectCoords[0], rectCoords[1]
        x2, y2 = rectCoords[2], rectCoords[3]
        if event.event_title.startswith("Smash"):
            start_color = (229, 114, 0)
            end_color = (217, 69, 31)
        elif index == 0 or index == 1 or index == 4:
            start_color = (255, 255, 255)
            end_color = (217, 217, 217)
            border_color = (0, 0, 0)
        else:
            start_color = (24, 24, 24)
            end_color = (0, 0, 0)
        gradient = [
            (
                int(start_color[0] + (end_color[0] - start_color[0]) * (i - y1) / (y2 - y1)),
                int(start_color[1] + (end_color[1] - start_color[1]) * (i - y1) / (y2 - y1)),
                int(start_color[2] + (end_color[2] - start_color[2]) * (i - y1) / (y2 - y1))
            ) for i in range(y1, y2)
        ]
        for y in range(y1, y2):
            draw.line([(x1, y), (x2, y)], fill=gradient[y - y1], width=1)
        draw.rectangle((x1, y1, x2, y2), outline=border_color, width=4)

    #TODO: Add Player names and Handles
    
    return None #TODO: DELETE WHEN DONE

def addSideBrackets(event, graphic, draw, font):
    if not event.side_title == None and not event.redemption_winner == None:
        #TODO: Implement
        return None
    elif not event.side_title == None:
        #TODO: Implement
        return None
    elif not event.redemption_winner == None:
        #TODO: Implement
        return None