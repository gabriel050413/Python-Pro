meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "VDD": "abreviação da palavra verdade",
            "BISCOITAR": "postar algo apenas para chamar a atenção",
            "HATER":"pessoa que está constantemente criticando os outros",
            "VLW": "abreviação da palavra valeu"
            }
word = input("fale uma palavra que você não entende")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("não sei essa palavra tambem")
