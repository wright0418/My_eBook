def save_game(character, filename):
    file = open(filename, "w")
    for key, value in character.items():
        file.write(f"{key}:{value}\n")
    file.close()
    print("遊戲進度已儲存")

def load_game(filename):
    try:
        file = open(filename, "r")
        character = {}
        for line in file.readlines():
            key, value = line.strip().split(":")
            character[key] = value
        file.close()
        print("遊戲進度已讀取")
        return character
    except:
        print("無法讀取存檔")
        return None
