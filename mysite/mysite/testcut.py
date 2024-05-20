from PIL import Image, ImageDraw, ImageFont
import random, string

def addName(graphic, draw, index, color, text, font_path, boxCoords):
    areas = [[159, 791, 446, 120], 
             [770, 575, 263, 78], 
             [1189, 575, 263, 78], 
             [1604, 575, 263, 78],   
             [746, 873, 200, 54], 
             [1057, 873, 200, 54], 
             [1368, 873, 200, 54], 
             [1670, 873, 200, 54]]
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
        yCoord -= (25*(4/len(name)))
    elif index < 4:
        yCoord -= (20*(4/len(name)))
    else:
        yCoord -= (17*(4/len(name)))
    draw.text((xCoord+3, yCoord+3), text, font=font, fill=(0,0,0))
    draw.text((xCoord, yCoord), text, font=font, fill=color)
    #draw.rectangle([(x,y), (x+width, y+height)], outline=(0,0,0), width=3)

graphic = Image.new("RGBA", (1920,1080))

background_image = Image.open('mysite/static/images/backgrounds/cut_background.png')
graphic.paste(background_image, (0,0))

draw = ImageDraw.Draw(graphic)

char = 'Luigi'
mario0 = Image.open(f'mysite/static/images/renders/{char}/{char}_0.png')
size = ((599),(599))
mario0 = mario0.resize(size)
graphic.alpha_composite(mario0, (34-0,271-0))

char = 'Pikachu'
mario1 = Image.open(f'mysite/static/images/renders/{char}/{char}_1.png')
size = ((369),(369))
mario1 = mario1.resize(size)
graphic.alpha_composite(mario1, (682-0,246-0))

char = 'Chrom'
mario2 = Image.open(f'mysite/static/images/renders/{char}/{char}_2.png')
size = ((369),(369))
mario2 = mario2.resize(size)
graphic.alpha_composite(mario2, (1099,246))

char = 'Mewtwo'
mario3 = Image.open(f'mysite/static/images/renders/{char}/{char}_3.png')
size = ((369),(369))
mario3 = mario3.resize(size)
graphic.alpha_composite(mario3, (1516,246))

char = 'Inkling'
mario4 = Image.open(f'mysite/static/images/renders/{char}/{char}_4.png')
size = ((276),(276))
mario4 = mario4.resize(size)
graphic.alpha_composite(mario4, (684-0,667-0))

char = 'Ness'
mario5 = Image.open(f'mysite/static/images/renders/{char}/{char}_5.png')
size = ((276),(276))
mario5 = mario5.resize(size)
graphic.alpha_composite(mario5, (996,667))

char = 'Mario'
mario6 = Image.open(f'mysite/static/images/renders/{char}/{char}_6.png')
size = ((276),(276))
mario6 = mario6.resize(size)
graphic.alpha_composite(mario6, (1301,667))

char = 'Bowser'
mario7 = Image.open(f'mysite/static/images/renders/{char}/{char}_7.png')
size = ((276),(276))
mario7 = mario7.resize(size)
graphic.alpha_composite(mario7, (1608,667))


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


numCoords = [[34, 769-35],
          [682+5, 563-20],
          [1099+5, 563-20],
          [1516+5, 563-20],
          [684+3, 860-10],
          [996+3, 860-10],
          [1301+3, 860-10],
          [1608+3, 860-10]]
for index, coord in enumerate(numCoords):
    x1, y1 = coord[0], coord[1]
    text = str(index+1)
    if index == 0:
        font_size = 205
    elif index < 4:
        font_size = 125
    else:
        font_size = 85
    font = ImageFont.truetype(font_path, font_size)
    draw.text((x1+3,y1+3), text, font=font, fill=shadow_color)
    draw.text((x1,y1), text, font=font, fill=text_color)


names = ['JOHN LION|JuiceGoose', 'JOHN LION|apT', 'JL|LukeM', 'MEOW|Giselle', 'JL|Mr. C', 'BN|StormSilver', 'TestName09872345','JL|Zach L.']
#names = ['', '', '', '', '', '', '', '']

for index, name in enumerate(names):
    '''
    characters = string.ascii_letters + string.digits
    length = random.randint(4, 10)
    name = name.join(random.choices(characters, k=length))
    '''
    addName(graphic, draw, index, (255,255,255), name, font_path, coords[index])


# Display the image
graphic.show()
