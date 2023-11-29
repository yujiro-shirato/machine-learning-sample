import requests

# ポケモンAPI
def get_pokemon_info(pokemon_id_or_name):
    base_url = "https://pokeapi.co/api/v2/pokemon/"

    # ポケモンの詳細情報を取得するためのURLを作成
    url = f"{base_url}{pokemon_id_or_name}/"

    # HTTP GETリクエストを送信
    response = requests.get(url)

    if response.status_code == 200:
        # レスポンスが成功した場合はJSONデータを取得
        pokemon_data = response.json()

        # ポケモンの名前や能力、タイプなどを表示
        print("Name:", pokemon_data['name'])
        print("Abilities:", [ability['ability']['name'] for ability in pokemon_data['abilities']])
        print("Types:", [type['type']['name'] for type in pokemon_data['types']])
        # 他にも必要な情報を取得して表示することができます
        
        # 名前だけ返す
        return f"{pokemon_data['name']}"
    else:
        # レスポンスが失敗した場合はエラーメッセージを表示
        return f"見つかりません。"