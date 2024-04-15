from PIL import Image, ImageDraw, ImageFont

graphic = Image.new("RGBA", (1920,1080))

background_image = Image.open('mysite/static/images/backgrounds/uva_fall_background.png')
graphic.paste(background_image, (0,0))

draw = ImageDraw.Draw(graphic)
border_color = (255, 255, 255)

coords = [[35, 770, 632, 937],
          [683, 564, 1050, 666],
          [1100, 564, 1467, 666],
          [1517, 564, 1884, 666],
          [683, 862, 959, 937],
          [997, 862, 1272, 937],
          [1302, 862, 1578, 937],
          [1609, 862, 1884, 937]]
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
font_size = 96
text_color = (255, 255, 255)
shadow_color = (0, 0, 0, 255)
font = ImageFont.truetype(font_path, font_size)
draw.text((48,23), text, font=font, fill=shadow_color)
draw.text((45,20), text, font=font, fill=text_color)

font = ImageFont.truetype(font_path, 48)
text = 'Top 8 - 04/12/24'
draw.text((48,138), text, font=font, fill=shadow_color)
draw.text((45,135), text, font=font, fill=text_color)
# Display the image
graphic.show()