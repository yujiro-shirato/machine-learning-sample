# インストール
pip install Flask

pip install requests

pip install pandas

pip install scikit-learn

pip install openai


# 仮想環境の作成（例）
python -m venv myenv

## 仮想環境を有効化
### Windowsの場合
myenv\Scripts\activate
### macOS / Linuxの場合
source myenv/bin/activate

# 実行方法
export FLASK_APP=chat

flask run
