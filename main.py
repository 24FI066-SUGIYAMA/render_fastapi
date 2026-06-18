from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉 - \"大吉！素晴らしい幸運が舞い込むでしょう。\"",
        "中吉 - \"中吉！努力が実を結び、良い結果が待っています。\"",
        "小吉 - \"小吉！ちょっとした幸運があなたの元にやってきます。\"",
        "吉 - \"吉！安定した幸せな日々が続くでしょう。\"",
        "末吉 - \"末吉！努力が実り始め、良い方向に進む時期です。\"",
        "凶 - \"凶。悪いことが起こるかもしれませんが、気を引き締めてください。\"",
        "小凶 - \"小凶。注意が必要な日です。慎重に行動しましょう。\"",
        "大凶 - \"大凶。厳しい状況が訪れるかもしれませんが、乗り越えましょう。\""
    ]

    return omikuji_list[random.randrange(8)]


### コードいろいろ... ###

@app.get("/index")
def index():
    html_content = """
    <html>
    <head>
        <title>Some HTML in here</title>
        <style>
            body { 
                text-align: center; 
                padding-top: 60px; 
                background-color: #f8f9fa; 
                color: #333333; 
                line-height: 1.6;
            }
            .container {
                background-color: #ffffff;
                padding: 40px;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
                display: inline-block;
                max-width: 500px;
                width: 90%;
            }
            h1 { 
                color: #0056b3; 
                font-size: 2rem; 
                margin-bottom: 20px;
            }
            p { 
                color: #666666; 
                font-size: 1.1rem; 
                margin: 10px 0;
            }
            .info {
                margin-top: 20px;
                padding-top: 20px;
                border-top: 1px solid #e9ecef;
                text-align: left;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Look ma! HTML!</h1>
            <p>ホームページ・メイカーの課題ページです。</p>
            
            <div class="info">
                <p><strong>現在のステータス:</strong> FastAPIを使ってAPIサーバーを構築し、HTMLの返却テストを行っています。</p>
                <p><strong>動作状況:</strong> Renderにデプロイし、正常にWebページが公開されました。</p>
            </div>
        </div>
    </body>
</html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(present):
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しはキャンディーです。"}  # f文字列というPythonの機能を使っている

