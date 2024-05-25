from django.shortcuts import render
from .models import Player, Event
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import os, json

def homepage_view(request):
    context = {
        "indexes": range(1,9)
    }
    return render(request, 'mysite/homepage.html', context)

def submit(request):
    top_players = []
    elimination_style = request.POST.get('elim_type')
    for index in range(1,8):
        number = index+1
        name = request.POST.get(f"player{number}_name").strip()
        handle = request.POST.get(f"player{number}_handle").strip().replace(" ","")
        if not handle.startswith('@'):
            handle = '@' + handle
        if elimination_style is 'double_elim':
            if number == 6 or number == 8:
                placement = number-1
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
        primary = f"mysite/static/images/renders/{primChar}/{primChar}_{primAlt}.png"
        secChar = request.POST.get(f"player{number}_secondary")
        secondary = None
        terChar = request.POST.get(f"player{number}_tertiary")
        tertiary = None
        customImage = request.POST.get(f"player{number}_custom")
        if customImage is (None or ""):
            primary = customImage
            terChar = secChar
            secChar = primChar
        if secChar is not None:
            secondary = f"static/images/icons/{secChar}_icon.png"
            if terChar is not None:
                tertiary = f"static/images/icons/{terChar}_icon.png"
        top_players.append({
            'name': str(name),
            'handle': str(handle),
            'placement': str(placement),
            'primary': primary,
            'secondary': secondary,
            'tertiary': tertiary
        })
    date = datetime.strptime(request.POST.get('event_date'), '%Y-%m-%d').strftime('%m/%d/%Y').strip()
    if request.POST.get('event_type') is 'smashatuva':
        title = "Smash @ UVA " + request.POST.get('semester')[0:1] + date[-2:] + " #"
    else:
        title = "The CUT "
    title += request.POST.get('event_number')
    participants = request.POST.get('participants')
    if request.POST.get('redemption_check'):
        redempWinner = request.POST.get('redemption_name').strip()
        redempChar = request.POST.get('redemption_primary')
        redempRender = f"static/images/renders/{redempChar}_icon.png"
    else:
        redempWinner = None
        redempChar = None
        redempAlt = None
        redempRender = None
    if request.POST.get('side_check'):
        sideTitle = request.POST.get('side_event').strip() + " Winner"
        sideWinner = request.POST.get('side_name').strip()
    else:
        sideTitle = None
        sideWinner = None
    event = {
        "title": title,
        "participants": participants,
        "date": date,
        "side_title": sideTitle,
        "side_winner": sideWinner,
        "redemption_winner": redempWinner,
        "redemption_render": redempRender
    }
    if title.startswith("Smash"):
        constructSmashAtUVA(top_players, event)
    else:
        constructCUT(top_players, event)
    return None #TODO: DELETE THIS LINE WHEN FINISHED
    return render(request, 'homepage.html', {
        "graphic": "success",
        "indexes": range(1,9)
    })

def constructSmashAtUVA(top_players, event):
    graphic = Image.new("RGB", (1920,1080))
    draw = ImageDraw.Draw(graphic)
    titleText = str(event["title"])
    if titleText[12] is 'F':
        background_image = Image.open('static/images/backgrounds/uva_fall_background.png')
    else:
        background_image = Image.open('static/images/backgrounds/uva_spring_background.png')
    graphic.paste(background_image, (0,0))
    font_path = 'static/fonts/Roboto-BoldItalic.ttf'
    shadow_color = (0,0,0)
    text_color = (255, 255, 255)

    font = ImageFont.truetype(font_path, 124)
    draw.text((63,168), titleText, font=font, fill=shadow_color)
    draw.text((60,165), titleText, font=font, fill=text_color)
    
    font = ImageFont.truetype(font_path, 64)
    top8text = f"Top 8 - {event["date"]}"
    draw.text((63,168), top8text, font=font, fill=shadow_color)
    draw.text((60,165), top8text, font=font, fill=text_color)

    font = ImageFont.truetype(font_path, 40)
    participantsText = f'{event["participants"]} Participants'
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
    background_image = Image.open('static/images/backgrounds/cut_background.png')
    graphic.paste(background_image, (0,0))
    font_path = 'static/fonts/AlbertSans-Bold.ttf'
    shadow_color = (255,255,255)
    text_color = (0,0,0)

    titleText = event["title"]
    font = ImageFont.truetype(font_path, 130)
    draw.text((308,45), titleText, font=font, fill=(189, 0, 0))
    draw.text((305,40), titleText, font=font, fill=text_color)
    
    participantsText = f'{event["participants"]} Participants'
    font = ImageFont.truetype(font_path, 40)
    draw.text((63,978), participantsText, font=font, fill=shadow_color)
    draw.text((60,975), participantsText, font=font, fill=text_color)
    
    shadow_color = (0,0,0)
    text_color = (255,255,255)
    text = 'Charlottesville, VA'
    draw.text((1543,978), text, font=font, fill=shadow_color)
    draw.text((1540,975), text, font=font, fill=text_color)

    font = ImageFont.truetype(font_path, 50)
    draw.text((1323,64), 'Top 8', font=font, fill=shadow_color)
    draw.text((1320,60), 'Top 8', font=font, fill=text_color)

    dateText = event["date"]
    box = draw.textbbox((0,0), "04/12/24", font=font)
    midpoint = [1280+((box[2]-box[0])/2), 120+((box[3]-box[1])/2)]
    box2 = draw.textbbox((0,0), dateText, font=font)
    drawCoords = [midpoint[0]-((box2[2]-box2[0])/2), midpoint[1]-((box2[3]-box2[1])/2)]
    draw.text((drawCoords[0]+4, drawCoords[1]+3), dateText, font=font, fill=shadow_color)
    draw.text((drawCoords[0], drawCoords[1]), dateText, font=font, fill=text_color)

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
        json_file_path = 'static/char_coords.json'
        with open(json_file_path, 'r') as file:
            charCoords = json.load(file)

        player = top_players[index]
        primary = player["primary"]
        render = Image.open(primary)
        charName = str(os.path.basename(primary))
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

        text_color = (255, 255, 255)
        border_color = (255, 255, 255)
        shadow_color = (0, 0, 0)
        x1, y1 = coord[0], coord[1]
        x2, y2 = coord[2], coord[3]
        if event["title"].startswith("Smash"):
            start_color = (229, 114, 0)
            end_color = (217, 69, 31)
        elif index == 0 or index == 1 or index == 4:
            start_color = (255, 255, 255)
            shadow_color = (255, 255, 255)
            end_color = (217, 217, 217)
            text_color = (0, 0, 0)
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

        numCoords = [[371, 280],
                 [885, 255],
                 [1298, 255],
                 [1715, 255],
                 [845, 712],
                 [1157, 712],
                 [1459, 712],
                 [1766, 712]]
        font = ImageFont.truetype('mysite/static/fonts/Rokkitt-BoldItalic.ttf', 2000)
        x1, y1 = numCoords[index][0], numCoords[index][1]
        placement = str(index+1)
        if index == 0:
            dimensions = [281, 478]
            shadow_displace = [11, 15]
        elif index < 4:
            dimensions = [185, 299]
            shadow_displace = [20, 22]
        else:
            dimensions = [130, 143]
            shadow_displace = [25, 29]
        curDim = draw.textbbox((0, 0), placement, font=font)
        text_image = Image.new('RGBA', (curDim[2]-curDim[0]+shadow_displace[0], curDim[3]-curDim[1]+shadow_displace[1]))
        placementDraw = ImageDraw.Draw(text_image)
        placementDraw.text((-curDim[0]+shadow_displace[0],-curDim[1]+shadow_displace[1]), placement, font=font, fill=shadow_color)
        placementDraw.text((-curDim[0],-curDim[1]), placement, font=font, fill=text_color)
        text_image = text_image.resize((dimensions[0], dimensions[1]), Image.Resampling.LANCZOS)
        graphic.alpha_composite(text_image, (x1, y1))

        name = player["name"]
        areas = [[59, 791, 552, 120], 
                 [700, 575, 333, 78], 
                 [1119, 575, 333, 78], 
                 [1534, 575, 333, 78],   
                 [700, 873, 246, 54], 
                 [1011, 873, 246, 54], 
                 [1318, 873, 246, 54], 
                 [1624, 873, 246, 54]]

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

        handle = player["handle"]
        x1, y1 = coord[0], coord[1]
        if handle is not None:
            y1 -= 45
            handle_font = 'mysite/static/fonts/LibreFranklin-Bold.ttf'
            font = ImageFont.truetype(handle_font, 19)
            box = draw.textbbox((0,0), handle, font=font)
            draw.rounded_rectangle((x1, y1, x1+60+(box[2]-box[0]), y1+35), fill=(35,35,35), outline=(255,255,255), width=3, radius=20)
            draw.text((x1+40, y1-40), handle, font=font, fill=(255,255,255))
            xlogo = Image.open('mysite/static/images/misc/x.png')
            size = ((20), (20))
            xlogo = xlogo.resize(size)
            graphic.paste(xlogo, (x1+15,y1-37))
        
        if player["secondary"] is not None:
            size = ((30),(30))
            sec = Image.open(player["secondary"]).resize(size)
            graphic.alpha_composite(sec, (x1,y1-80))
            if player["tertiary"] is not None:
                ter = Image.open(player["tertiary"]).resize(size)
                graphic.alpha_composite(ter, (x1+34,y1-80))

def addSideBrackets(event, graphic, draw, font_path):
    sideTitle = event["side_title"]
    redempWinner = event["redemption_winner"]
    text_color = (255, 255, 255)
    if sideTitle is not None and redempWinner is not None:
        redempImage = Image.open(event["redemption_render"]).resize((75,75))
        graphic.alpha_composite(redempImage, (1050,967))
        font = ImageFont.truetype(font_path, 20)
        draw.text((1050+75+20,975), "Redemption Winner", font=font, fill=text_color)
        font = ImageFont.truetype(font_path, 30)
        draw.text((1050+75+20,975+25), redempWinner, font=font, fill=text_color)
        if event["title"].startswith("The"):
            text_color = (0,0,0)
        sideWinner = event["side_winner"]
        smashlogo = Image.open(f"mysite/static/images/misc/smashlogo.png").resize((75,75))
        graphic.alpha_composite(smashlogo, (990-60-75,967))
        font = ImageFont.truetype(font_path, 20)
        boxDim = draw.textbbox((0, 0), sideTitle, font=font)
        draw.text((830-(boxDim[2]),975), sideTitle, font=font, fill=text_color)
        font = ImageFont.truetype(font_path, 30)
        boxDim = draw.textbbox((0, 0), sideWinner, font=font)
        draw.text((830-(boxDim[2]),975+25), sideWinner, font=font, fill=text_color)
    elif sideTitle is not None or redempWinner is not None:
        if sideTitle is not None:
            icon = Image.open(f"mysite/static/images/misc/smashlogo.png").resize((75,75))
            title = sideTitle
            winner = event["side_winner"]
        else:
            icon = Image.open(event["redemption_render"]).resize((75,75))
            title = "Redemption Winner"
            winner = redempWinner
        graphic.alpha_composite(icon, (1030,967))
        font = ImageFont.truetype(font_path, 20)
        if event["title"].startswith("The"):
            text_color = (0,0,0)
        boxDim = draw.textbbox((0, 0), title, font=font)
        draw.text((960-(boxDim[2]),975), title, font=font, fill=(0, 0, 0))
        font = ImageFont.truetype(font_path, 30)
        boxDim = draw.textbbox((0, 0), winner, font=font)
        draw.text((960-(boxDim[2]),975+25), winner, font=font, fill=(0, 0, 0))