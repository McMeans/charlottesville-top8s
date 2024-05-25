from PIL import Image, ImageDraw, ImageFont
import random, string

def addName(graphic, draw, index, color, text, font_path, boxCoords):
    if index == 0 or index == 1 or index == 4:
        text_color = (0,0,0)
        shadow_color = (255, 255, 255)
    else:
        text_color = (255, 255, 255)
        shadow_color = (0, 0, 0)
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
    if index == 5 or index == 7:
        placement = str(index)
    else:
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
    
    areas = [[59, 791, 552, 120], 
             [700, 575, 333, 78], 
             [1119, 575, 333, 78], 
             [1534, 575, 333, 78],   
             [700, 873, 246, 54], 
             [1011, 873, 246, 54], 
             [1318, 873, 246, 54], 
             [1624, 873, 246, 54]]
    handle = "@JuiceGoose_ssbu"
    font = ImageFont.truetype('mysite/static/fonts/LibreFranklin-Bold.ttf', 19)
    box = draw.textbbox((0,0), handle, font=font)
    x1, y1 = boxCoords[0], boxCoords[1]
    draw.rounded_rectangle((x1, y1-45, x1+60+(box[2]-box[0]), y1-10), fill=(35,35,35), outline=(255,255,255), width=3, radius=20)
    draw.text((x1+40, y1-40), handle, font=font, fill=(255,255,255))
    xlogo = Image.open('mysite/static/images/misc/x.png')
    size = ((20), (20))
    xlogo = xlogo.resize(size)
    graphic.paste(xlogo, (x1+15,y1-37))
    x, y, width, height = areas[index]
    font_size = 150
    font = ImageFont.truetype(font_path, font_size)

    size = ((30),(30))
    icon = Image.open(f'mysite/static/images/icons/Wario_icon.png').resize(size)
    icon2 = Image.open(f'mysite/static/images/icons/Sora_icon.png').resize(size)
    graphic.alpha_composite(icon, (x1,y1-80))
    graphic.alpha_composite(icon2, (x1+34,y1-80))

    box = draw.textbbox((0,0), text, font=font)
    text_width = box[2] - box[0]
    text_height = box[3] - box[1]
    while text_width > width or text_height > (height * 0.75):
        font_size -= 1
        font = ImageFont.truetype(font_path, font_size)
        box = draw.textbbox((0,0), text, font=font)
        text_width = box[2] - box[0]
        text_height = box[3] - box[1]

    xCoord = x + (width - text_width) / 2
    yCoord = y + (height - text_height) / 2
    if index == 0:
        yCoord -= (27*(4/len(name)))
    elif index < 4:
        yCoord -= (20*(4/len(name)))
    else:
        yCoord -= (14*(4/len(name)))
    draw.text((xCoord+3, yCoord+3), text, font=font, fill=shadow_color)
    draw.text((xCoord, yCoord), text, font=font, fill=text_color)
    #draw.rectangle([(x,y), (x+width, y+height)], outline=(128,128,128), width=3)

graphic = Image.new("RGBA", (1920,1080))

background_image = Image.open('mysite/static/images/backgrounds/cut_background.png')
graphic.paste(background_image, (0,0))

draw = ImageDraw.Draw(graphic)

char = 'Ken'
mario0 = Image.open(f'mysite/static/images/renders/{char}/{char}_0.png')
size = ((599),(599))
mario0 = mario0.resize(size)
graphic.alpha_composite(mario0, (0-35,271-0))

twoFourCoords = [648-20, 246-0]
mario1 = Image.open(f'mysite/static/images/renders/{char}/{char}_1.png')
size = ((369),(369))
mario1 = mario1.resize(size)
graphic.alpha_composite(mario1, (twoFourCoords[0],twoFourCoords[1]))

refChar = "Luigi"
mario2 = Image.open(f'mysite/static/images/renders/{char}/{char}_2.png')
mario2 = mario2.resize(size)
graphic.alpha_composite(mario2, (twoFourCoords[0]+(1*(1065-648)),twoFourCoords[1]))

mario3 = Image.open(f'mysite/static/images/renders/{char}/{char}_3.png')
mario3 = mario3.resize(size)
graphic.alpha_composite(mario3, (twoFourCoords[0]+(2*(1065-648)),twoFourCoords[1]))

fiveEightCoords = [654-0, 667-0]
mario4 = Image.open(f'mysite/static/images/renders/{char}/{char}_4.png')
size = ((276),(276))
mario4 = mario4.resize(size)
graphic.alpha_composite(mario4, (fiveEightCoords[0],fiveEightCoords[1]))

mario5 = Image.open(f'mysite/static/images/renders/{char}/{char}_5.png')
mario5 = mario5.resize(size)
graphic.alpha_composite(mario5, (fiveEightCoords[0]+(1*(1578-1271)),fiveEightCoords[1]))

mario6 = Image.open(f'mysite/static/images/renders/{char}/{char}_6.png')
mario6 = mario6.resize(size)
graphic.alpha_composite(mario6, (fiveEightCoords[0]+(2*(1578-1271)),fiveEightCoords[1]))

mario7 = Image.open(f'mysite/static/images/renders/{char}/{char}_7.png')
mario7 = mario7.resize(size)
graphic.alpha_composite(mario7, (fiveEightCoords[0]+(3*(1578-1271)),fiveEightCoords[1]))


coords = [[34, 769, 633, 938],
          [682, 563, 1051, 667],
          [1099, 563, 1468, 667],
          [1516, 563, 1885, 667],
          [684, 860, 960, 938],
          [996, 860, 1273, 938],
          [1301, 860, 1579, 938],
          [1608, 860, 1885, 938]]
font_path = 'mysite/static/fonts/AlbertSans-Bold.ttf'
text_color = (255, 255, 255)
shadow_color = (25, 25, 25, 155)
for index, coord in enumerate(coords):
    x1, y1 = coord[0], coord[1]
    x2, y2 = coord[2], coord[3]
    start_color = (229, 114, 0)
    end_color = (217, 69, 31)
    border_color = (255, 255, 255)
    if index == 0 or index == 1 or index == 4:
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

    # Draw the filled rectangle with gradient fill
    for y in range(y1, y2):
        draw.line([(x1, y), (x2, y)], fill=gradient[y - y1], width=1)
    draw.rectangle((x1, y1, x2, y2), outline=border_color, width=4)

    text = f'{index+1}'



text = "The CUT 144"
font_size = 130
font = ImageFont.truetype(font_path, font_size)
draw.text((308,45), text, font=font, fill=(189, 0, 0))
draw.text((305,40), text, font=font, fill=text_color)

shadow_color=(0,0,0)
text_color=(255,255,255)
font = ImageFont.truetype(font_path, 50)
text = 'Top 8'
draw.text((1323,64), text, font=font, fill=shadow_color)
draw.text((1320,60), text, font=font, fill=text_color)

text = '04/12/24'
box = draw.textbbox((0,0), "04/12/24", font=font)
midpoint = [1280+((box[2]-box[0])/2), 120+((box[3]-box[1])/2)]
box2 = draw.textbbox((0,0), text, font=font)
drawCoords = [midpoint[0]-((box2[2]-box2[0])/2), midpoint[1]-((box2[3]-box2[1])/2)]
draw.text((drawCoords[0]+4, drawCoords[1]+3), text, font=font, fill=shadow_color)
draw.text((drawCoords[0], drawCoords[1]), text, font=font, fill=text_color)

font = ImageFont.truetype(font_path, 40)
text = 'Charlottesville, VA'
draw.text((1543,978), text, font=font, fill=shadow_color)
draw.text((1540,975), text, font=font, fill=text_color)

text_color=(0,0,0)
shadow_color=(255,255,255)
text = '12 Participants'
draw.text((63,978), text, font=font, fill=shadow_color)
draw.text((60,975), text, font=font, fill=text_color)


names = ['JOHN LION|JuiceGoose', 'JOHN LION|apT', 'JL|LukeM', 'MEOW|Giselle', 'JL|Mr. C', 'BN|StormSilver', 'TestName09872345','JL|Zach L.']
#names = ['', '', '', '', '', '', '', '']

for index, name in enumerate(names):
    if name == "":
        characters = string.ascii_letters + string.digits
        length = random.randint(4, 10)
        name = name.join(random.choices(characters, k=length))
    addName(graphic, draw, index, (255,255,255), name, font_path, coords[index])


char = "Wario"
redempImage = Image.open(f"mysite/static/images/icons/{char}_icon.png").resize((75,75))
winner = "JL|JB"
graphic.alpha_composite(redempImage, (1050,967))
font = ImageFont.truetype(font_path, 20)
draw.text((1050+75+20,975), "Redemption Winner", font=font, fill=(255, 255, 255))
font = ImageFont.truetype(font_path, 30)
draw.text((1050+75+20,975+25), winner, font=font, fill=(255, 255, 255))

smashlogo = Image.open(f"mysite/static/images/misc/smashlogo.png").resize((75,75))
graphic.alpha_composite(smashlogo, (990-60-75,967))
title = "Squad Strike Winner"
winner = "JB & jclyde"
font = ImageFont.truetype(font_path, 20)
boxDim = draw.textbbox((0, 0), title, font=font)
draw.text((830-(boxDim[2]),975), title, font=font, fill=(0, 0, 0))
font = ImageFont.truetype(font_path, 30)
boxDim = draw.textbbox((0, 0), winner, font=font)
draw.text((830-(boxDim[2]),975+25), winner, font=font, fill=(0, 0, 0))

# Display the image
graphic.show()
