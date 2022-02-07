from flask import Flask, render_template
import json
import random


app = Flask(__name__)

@app.route('/')
def hello_geek():
    f = open('hsk-level-5.json')
    data = json.load(f)
    id = random.randrange(1201,2500,1)

   
    for i in data:
      if i['id'] == id:
        f.close()
        #print(i)
        pinyin = i['pinyin']
        return render_template('index.html', pinyin=i['pinyin'], hanzi=i['hanzi'], translations=i['translations'])

    
if __name__ == "__main__":
    app.run(debug=True)

