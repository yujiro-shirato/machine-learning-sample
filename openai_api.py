from openai import OpenAI
import configparser

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
    # レスポンスから生成されたテキストを取得して戻り値として返す
    generated_text = completion.choices[0].message.content
    return generated_text

def generate_babbage(prompt_text):

    # 設定ファイルを読み込む
    config = configparser.ConfigParser()
    config.read('config.properties')

    client = OpenAI(
        # プロパティファイルからAPIキーを取得
        api_key=config['DEFAULT']['OPENAI_API_KEY']
    )
    
    # babbage-002モデルを呼び出す
    completion = client.completions.create(
        model=config['DEFAULT']['BABBAGE_MODEL'],
        prompt=prompt_text,
        max_tokens=300,
        n=1,
        stop=["\n", "<|endoftext|>"],
        temperature=0.2,
        top_p=1,
        echo=False,
        presence_penalty=1,
        frequency_penalty=1
    )
    # レスポンスから生成されたテキストを取得して戻り値として返す
    combined_text = ""
    for i, choice in enumerate(completion.choices):
        combined_text += f"\n{choice.text.strip()}\n"

    return combined_text
    # generated_text = completion.choices[0].text.strip()
    # return generated_text

def generate_gpt35(prompt_text):

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
    
    # GPT-3.5モデルを呼び出す
    completion = client.chat.completions.create(
        model=config['DEFAULT']['GPT35_MODEL'],
        messages=[
            # system の content はチャット全体のコンテキストを設定します、今から質問する概要的な文を設定します
            {"role": "system", "content": "あなたは健康マイレージのFAQ回答者です\
             ユーザーは健康マイレージ関連した質問をしてきます\
             質問内容に対してfine-tuningで学習したデータを最優先で回答してください"},
            # user の content は 実際の質問を書きます
            {"role": "user", "content": prompt_text}
        ]
    )
    # レスポンスから生成されたテキストを取得して戻り値として返す
    generated_text = completion.choices[0].message.content
    return generated_text