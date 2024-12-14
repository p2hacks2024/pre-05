import json
import os

def zenkaku_to_hankaku(text):
    zenkaku = "０１２３４５６７８９　－ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
    hankaku = "0123456789 -ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = str.maketrans(zenkaku, hankaku)
    return text.translate(table)

def convert_json(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist.")
        return
    
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for item in data:
        for key, value in item.items():
            if isinstance(value, str):
                item[key] = zenkaku_to_hankaku(value)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    try:
        print(f"現在のディレクトリ: {os.getcwd()}")
        
        # 入出力ファイルの設定
        input_file = 'place_details.json'  # 相対パスで指定
        output_file = 'place_details_converted.json'
        
        print(f"探索するファイル: {input_file}")
        print(f"絶対パス: {os.path.abspath(input_file)}")
        
        # ファイルの存在確認と変換実行
        if os.path.exists(input_file):
            print(f"ファイルが見つかりました: {input_file}")
            print("変換開始")
            convert_json(input_file, output_file)
            print("変換完了")
        else:
            print(f"エラー: {input_file} が見つかりません")
            print("以下を確認してください:")
            print("1. ファイルが正しい場所にあるか")
            print("2. ファイル名が正しいか")
            print("3. 現在のディレクトリが正しいか")
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")