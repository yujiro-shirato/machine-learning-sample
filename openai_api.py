from openai import OpenAI
import configparser

# .envファイルから環境変数を読み込む

def generate_text(prompt_text):

    # 設定ファイルを読み込む
    config = configparser.ConfigParser()
    config.read('config.properties')

    #client = OpenAI()
    # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
    # if you saved the key under a different environment variable name, you can do something like:
    client = OpenAI(
        # プロパティファイルからAPIキーを取得
        api_key=config['DEFAULT']['OPENAI_API_KEY']
    )
    print('api-key取得成功')
    
    # GPT-3.5モデルを呼び出す
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            # system の content はチャット全体のコンテキストを設定します、今から質問する概要的な文を設定します
            {"role": "system", "content": "あなたは質問に回答してくれるアシスタントです。"},
            # user の content は 実際の質問を書きます
            {"role": "user", "content": prompt_text}
        ]
    )
    print('api呼び出し成功')
    # レスポンスから生成されたテキストを取得して戻り値として返す
    generated_text = completion.choices[0].message.content
    print(completion.choices[0].message.content)
    return generated_text