from PIL import Image
from io import BytesIO
import requests

characters = [
    ["Kirby", "kirby"],
    ["Mr Game & Watch", "mr_game_and_watch"],
    ["Sora", "sora"]
]

for i, character in enumerate(characters):
    for index in range(0, 8):
        image = Image.new("RGBA", (1000,1000), (0,0,0,0))
        urlNum = index+1
        if urlNum != 1:
            url = f'https://www.smashbros.com/assets_v2/img/fighter/{character[1]}/main{urlNum}.png'
        else:
            url = f'https://www.smashbros.com/assets_v2/img/fighter/{character[1]}/main.png'
        
        response = requests.get(url)
        if response.status_code == 200:
            render = Image.open(BytesIO(response.content))
            
            if render.width > render.height:
                scale = 1000 / render.width
            else:
                scale = 1000 / render.height
            new_size = (int(render.width * scale), int(render.height * scale))
            render = render.resize(new_size, resample=Image.BILINEAR)

            x = (image.width - render.width) // 2
            y = (image.height - render.height) // 2
            image.alpha_composite(render, (x, y))

            file_path = f'mysite/static/images/renders/{character[0]}/{character[0]}_{index}.png'
            image.save(file_path)
