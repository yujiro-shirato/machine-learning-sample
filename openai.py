import openai
import configparser

def generate_text(prompt_text):
    
    # ConfigParserオブジェクトを作成してプロパティファイルを読み込む
    config = configparser.ConfigParser()
    config.read('config.properties')

    # プロパティファイルからAPIキーを取得
    api_key = config['DEFAULT']['openai_api_key']

    # OpenAI APIキーを設定
    openai.api_key = api_key

    # GPT-3.5モデルを呼び出す
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_text,
        max_tokens=100
    )

    # レスポンスから生成されたテキストを取得して戻り値として返す
    generated_text = response.choices[0].text.strip()
    return generated_text