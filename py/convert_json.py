import json

def zenkaku_to_hankaku(text):
    zenkaku = "０１２３４５６７８９　－ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
    hankaku = "0123456789 -ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = str.maketrans(zenkaku, hankaku)
    return text.translate(table)

def convert_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for item in data:
        for key, value in item.items():
            if isinstance(value, str):
                item[key] = zenkaku_to_hankaku(value)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    convert_json('02hakodate_restaurants.json', '02hakodate_restaurants_converted.json')