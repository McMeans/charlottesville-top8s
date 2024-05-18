from django.shortcuts import render
from .models import Player, Event
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import os, json

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
    draw = ImageDraw.Draw(graphic)
    if event.event_title[12] == 'F':
        background_image = Image.open('mysite/static/images/backgrounds/uva_fall_background.png')
    else:
        background_image = Image.open('mysite/static/images/backgrounds/uva_spring_background.png')
    graphic.paste(background_image, (0,0))
    font_path = 'mysite/static/fonts/Roboto-BoldItalic.ttf'
    shadow_color = (0,0,0)
    text_color = (255, 255, 255)

    font = ImageFont.truetype(font_path, 124)
    draw.text((63,168), event.event_title, font=font, fill=shadow_color)
    draw.text((60,165), event.event_title, font=font, fill=text_color)
    
    font = ImageFont.truetype(font_path, 64)
    top8text = f"Top 8 - {event.event_date}"
    draw.text((63,168), top8text, font=font, fill=shadow_color)
    draw.text((60,165), top8text, font=font, fill=text_color)

    font = ImageFont.truetype(font_path, 40)
    participantsText = f'{event.event_participants} Participants'
    draw.text((63,978), participantsText, font=font, fill=shadow_color)
    draw.text((60,975), participantsText, font=font, fill=text_color)
    locationText = 'Charlottesville, VA'
    draw.text((1543,978), locationText, font=font, fill=shadow_color)
    draw.text((1540,975), locationText, font=font, fill=text_color)

    addPlayers(top_players, event, graphic, draw, font_path)
    addSideBrackets(event, graphic, draw, font_path)
    return None #TODO: DELETE THIS LINE WHEN DONE
    graphic.save("graphic.png")

def constructCUT(top_players, event):
    graphic = Image.new("RGB", (1920,1080))
    draw = ImageDraw.Draw(graphic)
    background_image = Image.open('mysite/static/images/backgrounds/cut_background.png')
    graphic.paste(background_image, (0,0))
    font_path = 'mysite/static/fonts/AlbertSans-Bold.ttf'
    shadow_color = (0,0,0)
    text_color = (255, 255, 255)

    #TODO: ADD TEXT
    
    addPlayers(top_players, event, graphic, draw, font_path)
    addSideBrackets(event, graphic, draw, font_path)
    return None #TODO: DELETE THIS LINE WHEN DONE
    graphic.save("graphic.png")


def addPlayers(top_players, event, graphic, draw, font_path):
    rectCoords = [[35, 770, 632, 937],
          [683, 564, 1050, 666],
          [1100, 564, 1467, 666],
          [1517, 564, 1884, 666],
          [683, 862, 959, 937],
          [997, 862, 1272, 937],
          [1302, 862, 1578, 937],
          [1609, 862, 1884, 937]]
    for index, coord in enumerate(rectCoords):
        json_file_path = 'char_coords.json'
        with open(json_file_path, 'r') as file:
            charCoords = json.load(file)

        player = top_players[index]
        render = Image.open(player.primary_character)
        charName = str(player.primary_character.name)
        if charName.__contains__('_'):
            stop_index = charName.find('_')
            charName = charName[:stop_index]
        
        if charName in charCoords:
            displace = True
        else:
            displace = False
        displacement = [0, 0]

        #TODO: ACCOUNT FOR RESIZING
        positions = [[34, 271],[682, 246],[1099, 246],[1516, 246],[684, 667],[996, 667],[1301, 667],[1608, 667]][index]
        if index == 0:
            size = ((599),(599))
            if displace:
                displacement = [charCoords[charName][0], charCoords[charName][1]]
        elif index < 4:
            size = ((369),(369))
            if displace:
                displacement = [charCoords[charName][2], charCoords[charName][3]]
        else:
            size = ((276),(276))
            if displace:
                displacement = [charCoords[charName][4], charCoords[charName][5]]
        render = render.resize(size)
        graphic.alpha_composite(render, (positions[0]-displacement[0], positions[1]-displacement[1]))

        text_color, border_color = (255, 255, 255)
        shadow_color = (0, 0, 0)
        x1, y1 = coord[0], coord[1]
        x2, y2 = coord[2], coord[3]
        if event.event_title.startswith("Smash"):
            start_color = (229, 114, 0)
            end_color = (217, 69, 31)
        elif index == 0 or index == 1 or index == 4:
            start_color, shadow_color = (255, 255, 255)
            end_color = (217, 217, 217)
            text_color, border_color = (0, 0, 0)
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

        numCoord = [[34, 769-35],
                    [682+5, 563-20],
                    [1099+5, 563-20],
                    [1516+5, 563-20],
                    [684+3, 860-10],
                    [996+3, 860-10],
                    [1301+3, 860-10],
                    [1608+3, 860-10]][index]
        x1, y1 = numCoord[0], numCoord[1]
        if index == 0:
            font_size = 205
        elif index < 4:
            font_size = 125
        else:
            font_size = 85
        font = ImageFont.truetype(font_path, font_size)
        num = player.player_placement
        draw.text((x1+3,y1+3), num, font=font, fill=shadow_color)
        draw.text((x1,y1), num, font=font, fill=text_color)

        name = player.player_name
        areas = [[159, 791, 446, 120], 
                [770, 575, 263, 78], 
                [1189, 575, 263, 78], 
                [1604, 575, 263, 78],   
                [746, 873, 200, 54], 
                [1057, 873, 200, 54], 
                [1368, 873, 200, 54], 
                [1670, 873, 200, 54]]

        x, y, width, height = areas[index]
        font_size = 150
        font = ImageFont.truetype(font_path, font_size)
        box = draw.textbbox((0,0), name, font=font)
        text_width = box[2] - box[0]
        text_height = box[3] - box[1]
        while text_width > width or text_height > (height * 0.75):
            font_size -= 1
            font = ImageFont.truetype(font_path, font_size)
            box = draw.textbbox((0,0), name, font=font)
            text_width = box[2] - box[0]
            text_height = box[3] - box[1]

        xCoord = x + (width - text_width) / 2
        yCoord = y + (height - text_height) / 2
        if index == 0:
            yCoord -= (25*(4/len(name)))
        elif index < 4:
            yCoord -= (20*(4/len(name)))
        else:
            yCoord -= (17*(4/len(name)))
        draw.text((xCoord+3, yCoord+3), name, font=font, fill=shadow_color)
        draw.text((xCoord, yCoord), name, font=font, fill=text_color)

        #TODO: Add handles and non-primary characters
    
    return None #TODO: DELETE WHEN DONE

def addSideBrackets(event, graphic, draw, font_path):
    if not event.side_title == None and not event.redemption_winner == None:
        #TODO: Implement
        return None
    elif not event.side_title == None:
        #TODO: Implement
        return None
    elif not event.redemption_winner == None:
        #TODO: Implement
        return None