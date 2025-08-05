from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

# 表示したい国とタイムゾーン名のリスト
COUNTRIES = {
    '日本': 'Asia/Tokyo',
    'アメリカ（ニューヨーク）': 'America/New_York',
    'イギリス（ロンドン）': 'Europe/London',
    'オーストラリア（シドニー）': 'Australia/Sydney',
    'ブラジル（サンパウロ）': 'America/Sao_Paulo',
}

@app.route('/')
def index():
    times = {}
    now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
    for country, tzname in COUNTRIES.items():
        tz = pytz.timezone(tzname)
        times[country] = now_utc.astimezone(tz).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', times=times)

if __name__ == '__main__':
    # 開発用サーバをポート5000で起動
    app.run(host='127.0.0.1', port=5000, debug=True)
