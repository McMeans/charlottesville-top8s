from PIL import Image
from io import BytesIO
import requests

characters = [
    ["Banjo & Kazooie", "banjo_and_kazooie"],
    ["Bayonetta", "bayonetta"],
    ["Bowser", "bowser"],
    ["Bowser Jr", "bowser_jr"],
    ["Byleth", "byleth"],
    ["Captain Falcon", "captain_falcon"],
    ["Chrom", "chrom"],
    ["Cloud", "cloud"],
    ["Corrin", "corrin"],
    ["Daisy", "daisy"],
    ["Dark Pit", "dark_pit"],
    ["Dark Samus", "dark_samus"],
    ["Diddy Kong", "diddy_kong"],
    ["Donkey Kong", "donkey_kong"],
    ["Dr Mario", "dr_mario"],
    ["Duck Hunt", "duck_hunt"],
    ["Falco", "falco"],
    ["Fox", "fox"],
    ["Ganondorf", "ganondorf"],
    ["Greninja", "greninja"],
    ["Hero", "dq_hero"],
    ["Ice Climbers", "ice_climbers"],
    ["Ike", "ike"],
    ["Incineroar", "incineroar"],
    ["Inkling", "inkling"],
    ["Isabelle", "isabelle"],
    ["Jigglypuff", "jigglypuff"],
    ["Joker", "joker"],
    ["Kazuya", "kazuya"],
    ["Ken", "ken"],
    ["King Dedede", "king_dedede"],
    ["King K Rool", "king_k_rool"],
    ["Kirby", "kirby"],
    ["Link", "link"],
    ["Little Mac", "little_mac"],
    ["Lucario", "lucario"],
    ["Lucas", "lucas"],
    ["Lucina", "lucina"],
    ["Luigi", "luigi"],
    ["Mario", "mario"],
    ["Marth", "marth"],
    ["Mega Man", "mega_man"],
    ["Meta Knight", "meta_knight"],
    ["Mewtwo", "mewtwo"],
    ["Min Min", "min_min"],
    ["Mr Game and Watch", "mr_game_and_watch"],
    ["Ness", "ness"],
    ["Olimar", "olimar"],
    ["Pac-Man", "pac_man"],
    ["Palutena", "palutena"],
    ["Peach", "peach"],
    ["Pichu", "pichu"],
    ["Pikachu", "pikachu"],
    ["Piranha Plant", "piranha_plant"],
    ["Pit", "pit"],
    ["Pokemon Trainer", "pokemon_trainer"],
    ["Pyra and Mythra", "pyra"],
    ["Richter", "richter"],
    ["Ridley", "ridley"],
    ["ROB", "rob"],
    ["Robin", "robin"],
    ["Rosalina and Luma", "rosalina_and_luma"],
    ["Roy", "roy"],
    ["Ryu", "ryu"],
    ["Samus", "samus"],
    ["Sephiroth", "sephiroth"],
    ["Sheik", "sheik"],
    ["Shulk", "shulk"],
    ["Simon", "simon"],
    ["Snake", "snake"],
    ["Sonic", "sonic"],
    ["Sora", "sora"],
    ["Steve", "steve"],
    ["Terry", "terry"],
    ["Toon Link", "toon_link"],
    ["Villager", "villager"],
    ["Wario", "wario"],
    ["Wii Fit Trainer", "wii_fit_trainer"],
    ["Wolf", "wolf"],
    ["Yoshi", "yoshi"],
    ["Young Link", "young_link"],
    ["Zelda", "zelda"],
    ["Zero Suit Samus", "zero_suit_samus"]
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
