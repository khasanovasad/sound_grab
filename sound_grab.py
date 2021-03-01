from __future__ import unicode_literals
import youtube_dl

def download(url, filename, destination):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'
        }],
        'outtmpl': destination + filename + '.mp3',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

destination = "~/Music/"
grab_em = {
        "https://www.youtube.com/watch?v=WSuVCyT63II": "The Beatles -- Yesterday",
        "https://www.youtube.com/watch?v=7qMls5yxP1w": "The Beatles -- Hey Jude!",
        "https://www.youtube.com/watch?v=6d5ST3tbPIU": "The Beatles -- Let It Be",
        "https://www.youtube.com/watch?v=S302kF8MJ-I": "The Beatles -- She Loves You",
        "https://www.youtube.com/watch?v=HuS5NuXRb5Y": "The Beatles -- Eleonor Rigby",
        "https://www.youtube.com/watch?v=KQetemT1sWc": "The Beatles -- Here Comes The Sun",
        "https://www.youtube.com/watch?v=9_c2XZd9mMo": "The Beatles -- And I Love Her",
        "https://www.youtube.com/watch?v=lqAS8sCffZg": "The Beatles -- In My Life",
        "https://www.youtube.com/watch?v=iELGhAGwBdc": "The Beatles -- Here, There And Everywhere",

        "https://www.youtube.com/watch?v=AjIL2BemqBY": "Deep Purple -- Soldier Of Fortune",
        "https://www.youtube.com/watch?v=9_Iq9CWuqMM": "Deep Purple -- When A Blind Man Cries",

        "https://www.youtube.com/watch?v=LYU-8IFcDPw": "Linkin Park -- Faint",
        "https://www.youtube.com/watch?v=eVTXPUF4Oz4": "Linkin Park -- In The End",
        "https://www.youtube.com/watch?v=kXYiU_JCYtU": "Linkin Park -- Numb",
        "https://www.youtube.com/watch?v=8sgycukafqQ": "Linkin Park -- What I've Done",

        "https://www.youtube.com/watch?v=6Ejga4kJUts": "The Cranberries -- Zombie",
        "https://www.youtube.com/watch?v=Zz-DJr1Qs54": "The Cranberries -- Ode To My Family",
        "https://www.youtube.com/watch?v=RUmdWdEgHgk": "The Cranberries -- When You Are Gone",
        "https://www.youtube.com/watch?v=G6Kspj3OO0s": "The Cranberries -- Linger",
        "https://www.youtube.com/watch?v=ky4CdN0x58A": "The Cranberries -- Animal Instinct",
        "https://www.youtube.com/watch?v=SHoHIL2ABVQ": "The Cranberries -- Just My Imagination",
        "https://www.youtube.com/watch?v=7LM4Cb6wZUA": "The Cranberries -- Ridiculous Thoughts",
        "https://www.youtube.com/watch?v=h1lMxX8doSU": "The Cranberries -- All Over Now",
        "https://www.youtube.com/watch?v=ZKwJrfF-0uY": "The Cranberries -- Wake Me When It's Over",
        "https://www.youtube.com/watch?v=hUFPooqKllA": "The Cranberries -- Promises",
        "https://www.youtube.com/watch?v=Yam5uK6e-bQ": "The Cranberries -- Dreams",

        "https://www.youtube.com/watch?v=fJ9rUzIMcZQ": "Queen -- Bohemain Rhapsody",
        "https://www.youtube.com/watch?v=rY0WxgSXdEE": "Queen -- Another One Bites The Dust",
        "https://www.youtube.com/watch?v=-tJYN-eG1zk": "Queen -- We Will Rock You",
        "https://www.youtube.com/watch?v=04854XqcfCY": "Queen -- We Are The Champions",
        "https://www.youtube.com/watch?v=Z3w5gVM_4y8": "Queen -- I Want To Break Free",
        "https://www.youtube.com/watch?v=azdwsXLmrHE": "Queen -- Radio Ga Ga",
        "https://www.youtube.com/watch?v=t99KH0TR-J4": "Queen -- The Show Must Go On",
        "https://www.youtube.com/watch?v=sUJkCXE4sAA": "Queen -- Love Of My Life",
        "https://www.youtube.com/watch?v=kijpcUv-b8M": "Queen -- Somebody To Love",
        "https://www.youtube.com/watch?v=a01QQZyl-_I": "Queen -- Pressure",
        "https://www.youtube.com/watch?v=2ZBtPf7FOoM": "Queen -- Killer Queen",
        "https://www.youtube.com/watch?v=HgzGwKwLmgM": "Queen -- Don't Stop Me Now",

        "https://www.youtube.com/watch?v=zRIbf6JqkNc": "Guns N' Roses -- Don't Cry",
        "https://www.youtube.com/watch?v=8SbUC-UaAxE": "Guns N' Roses -- November Rain",

        "https://www.youtube.com/watch?v=n4RjJKxsamQ": "Scorpions -- Wind Of Change",
        "https://www.youtube.com/watch?v=1UUYjd2rjsE": "Scorpions -- Send Me An Angel",
        "https://www.youtube.com/watch?v=CjRas1yOWvo": "Scorpions -- Still Loving You",

        "https://www.youtube.com/watch?v=QkF3oxziUI4": "Led Zappelin -- Stairway To Heaven",
        "https://www.youtube.com/watch?v=s85y2M615PA": "Led Zappelin -- Immigrant Song",

        "https://www.youtube.com/watch?v=pAgnJDJN4VA": "AC~DC -- Back In Black",
        "https://www.youtube.com/watch?v=l482T0yNkeo": "AC~DC -- Highway To Hell",

        "https://www.youtube.com/watch?v=fregObNcHC8": "Nirvana (MTV Unplugged) -- The Man Who Sold The World",
        "https://www.youtube.com/watch?v=z9LiPuVRyU8": "Nirvana (MTV Unplugged) -- Come As You Are",
        "https://www.youtube.com/watch?v=1YhR5UfaAzM": "Nirvana (MTV Unplugged) -- Something In The Way",
        "https://www.youtube.com/watch?v=pkcJEvMcnEg": "Nirvana -- Lithium",
        "https://www.youtube.com/watch?v=hTWKbfoikeg": "Nirvana -- Smells Like Teen Spirit",
        "https://www.youtube.com/watch?v=_24pJQUj7zg": "Nirvana (MTV Unplugged) -- About A Girl",
        "https://www.youtube.com/watch?v=GtBhclCigH0": "Nirvana (MTV Unplugged) -- Dumb",
        "https://www.youtube.com/watch?v=aWmkuH1k7uA": "Nirvana (MTV Unplugged) -- All Apologies",

        "https://www.youtube.com/watch?v=JoolQUDWq-k": "Metallica -- Die My Darling",
        "https://www.youtube.com/watch?v=tAGnKpE4NCI": "Metallica -- Nothing Else Matters",
        "https://www.youtube.com/watch?v=eRV9uPr4Dz4": "Metallica -- Until It Sleeps",
        "https://www.youtube.com/watch?v=xnKhsTXoKCI": "Metallica -- Master Of Puppets",
        "https://www.youtube.com/watch?v=CD-E-LDc384": "Metallica -- Enter Sandman",
        "https://www.youtube.com/watch?v=WEQnzs8wl6E": "Metallica -- Fade To Black",
        "https://www.youtube.com/watch?v=Ckom3gf57Yw": "Metallica -- The Unforgiven",
        "https://www.youtube.com/watch?v=5bt7kAVxKfs": "Metallica -- The Unforgiven 2",
        "https://www.youtube.com/watch?v=aSNJ00iAZ7I": "Metallica -- One",
        "https://www.youtube.com/watch?v=k7_hwgD1ugg": "Metallica -- To Live Is To Die",

        "https://www.youtube.com/watch?v=Ij99dud8-0A": "Iron Maiden -- Wasted Years",
        "https://www.youtube.com/watch?v=J51LPlP-s9o": "Iron Maiden -- Hallowed Be Thy Name",
        "https://www.youtube.com/watch?v=2G5rfPISIwo": "Iron Maiden -- Trooper",
        "https://www.youtube.com/watch?v=J0N1yY937qg": "Iron Maiden -- Fear Of The Dark",

        "https://www.youtube.com/watch?v=DW3pZjmS3rg": "Black Sabbath -- Planet Caravan",
        "https://www.youtube.com/watch?v=vmV8niW5GXs": "Black Sabbath -- Solitude",
        "https://www.youtube.com/watch?v=0qanF-91aJo": "Black Sabbath -- Paranoid",
        "https://www.youtube.com/watch?v=LQUXuQ6Zd9w": "Black Sabbath -- War Pigs",

        "https://www.youtube.com/watch?v=34ZmKbe5oG4": "Pink Floyd -- Another Brick In The Wall 2",
        "https://www.youtube.com/watch?v=_FrOQC-zEog": "Pink Floyd -- Comfortably Numb",
        "https://www.youtube.com/watch?v=hjpF8ukSrvk": "Pink Floyd -- Wish You Were Here",
        "https://www.youtube.com/watch?v=7jMlFXouPk8": "Pink Floyd -- High Hopes",
        "https://www.youtube.com/watch?v=cWGE9Gi0bB0": "Pink Floyd -- Shine On Your Crazy Diamond",

        "https://www.youtube.com/watch?v=lS-af9Q-zvQ": "The Doors -- Riders On The Storm",
        "https://www.youtube.com/watch?v=Mgw5j9h8528": "The Doors -- Been Down So Long",
        "https://www.youtube.com/watch?v=j0Mz_IqpZX8": "The Doors -- People Are Strange",
        "https://www.youtube.com/watch?v=imcHmSUVEvk": "The Doors -- Crystal Ship",
        "https://www.youtube.com/watch?v=WwnLt6b7YHk": "The Doors -- L.A Woman",
}

for key, value in grab_em.items():
    download(key, value, destination)
    print()

