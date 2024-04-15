from PIL import Image, ImageDraw, ImageFont

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

background_image = Image.open('mysite/mysite/uva_sunrise_aerial.jpg')
background_opacity = background_image.convert("RGBA")
opacity_layer = Image.new("RGBA", background_opacity.size, (255, 255, 255, int(255 * 0.9)))
background_opacity = Image.alpha_composite(background_opacity, opacity_layer)
graphic.paste(background_opacity, (0,0), background_opacity)

draw = ImageDraw.Draw(graphic)
border_color = (256, 256, 256)

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
font_name = "Arial Bold Italic"
font_size = 96
text_color = (255, 255, 255)
shadow_color = (0, 0, 0, 20)
font = ImageFont.truetype(font_name + ".ttf", font_size)
draw.text((40,25), text, font=font, fill=shadow_color)
draw.text((35,20), text, font=font, fill=text_color)
# Display the image
graphic.show()