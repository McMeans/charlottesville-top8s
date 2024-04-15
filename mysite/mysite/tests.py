from PIL import Image, ImageDraw, ImageFont

graphic = Image.new("RGBA", (1920,1080))

background_image = Image.open('mysite/static/images/backgrounds/uva_fall_background.png')
graphic.paste(background_image, (0,0))

draw = ImageDraw.Draw(graphic)
border_color = (255, 255, 255)

coords = [[34, 769, 633, 938],
          [682, 563, 1051, 667],
          [1099, 563, 1468, 667],
          [1516, 563, 1885, 667],
          [684, 860, 960, 938],
          [996, 860, 1273, 938],
          [1301, 860, 1579, 938],
          [1608, 860, 1885, 938]]
for index, coord in enumerate(coords):
    x1, y1 = coord[0], coord[1]
    x2, y2 = coord[2], coord[3]
    start_color = (229, 114, 0)
    end_color = (217, 69, 31)
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

text = "Smash @ UVA S24 #12"
font_path = 'mysite/static/fonts/Roboto-BoldItalic.ttf'
font_size = 124
text_color = (255, 255, 255)
shadow_color = (0, 0, 0, 255)
font = ImageFont.truetype(font_path, font_size)
draw.text((63,30), text, font=font, fill=shadow_color)
draw.text((60,25), text, font=font, fill=text_color)

font = ImageFont.truetype(font_path, 64)
text = 'Top 8 - 04/12/24'
draw.text((63,168), text, font=font, fill=shadow_color)
draw.text((60,165), text, font=font, fill=text_color)

font = ImageFont.truetype(font_path, 40)
text = '12 Participants'
draw.text((63,978), text, font=font, fill=shadow_color)
draw.text((60,975), text, font=font, fill=text_color)

text = 'Charlottesville, VA'
draw.text((1543,978), text, font=font, fill=shadow_color)
draw.text((1540,975), text, font=font, fill=text_color)


# Display the image
graphic.show()