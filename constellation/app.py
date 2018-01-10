from flask import Flask, render_template, request
import random
import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

app = Flask(__name__)

def get_constellation(month, day):
    dates = (21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22)
    constellations = ("摩羯座", "水瓶座", "雙魚座", "牡羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蠍座", "射手座")

    if day < dates[month-1]:
        return constellations[month-1]
    else:
        return constellations[month]

def findkind(name):

    if name == "牡羊座":
        return "fire"
    elif name == "獅子座":
        return "fire"
    elif name == "雙子座":
        return  "wind"
    elif name == "射手座":
        return  "fire"
    elif name == "天蠍座":
        return  "water"
    elif name == "雙魚座":
        return  "water"
    elif name == "水瓶座":
        return  "wind"
    elif name == "處女座":
        return  "land"
    elif name == "巨蟹座":
        return  "water"
    elif name == "天秤座":
        return  "wind"
    elif name == "魔羯座":
        return  "land"
    elif name == "金牛座":
        return  "land"
    else:
        return "ERROR"
def findtype(name):

    if name == "牡羊座":
        return "冒險型投資人" + "--" + "風險承受度高"
    elif name == "獅子座":
        return "積極型投資人" + "--" + "風險承受度中高"
    elif name == "雙子座":
        return  "積極型投資人"+ "--" + "風險承受度中高"
    elif name == "射手座":
        return  "冒險型投資人" + "--" + "風險承受度高"
    elif name == "天蠍座":
        return  "穩健型投資人" + "--" + "風險承受度中"
    elif name == "雙魚座":
        return  "保守型投資人" + "--" + "風險承受度低"
    elif name == "水瓶座":
        return  "保守型投資人" + "--" + "風險承受度低"
    elif name == "處女座":
        return  "保守型投資人" + "--" + "風險承受度低"
    elif name == "巨蟹座":
        return  "消極型投資人" + "--" + "風險承受度極低"
    elif name == "天秤座":
        return  "穩健型投資人" + "--" + "風險承受度中"
    elif name == "魔羯座":
        return  "消極型投資人" + "--" + "風險承受度極低"
    elif name == "金牛座":
        return  "穩健型投資人" + "--" + "風險承受度中"
    else:
        return "ERROR"

def findstock(kind):
    import pandas as pd
    import numpy as np
    import csv
    from pandas import DataFrame
    dfa = pd.read_csv('stock.csv',index_col=['Stock'])
    dfb = pd.read_csv('table.csv',index_col=['Kind'])
    dfc=dfa*dfb.loc[kind,:]
    dfc['total']=dfc['Price']+dfc['Dividend']+dfc['Profit']+dfc['Liability']
    dfd=dfc.sort_values(by=['total'],ascending=False).head(1)
    pic=dfd.index
    pica=pic.values
    picb=pica[0]
    picc=str(picb)
    return picc


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    month = request.form['month']
    day = request.form['day']

    try:
        name = get_constellation(int(month), int(day))
        kind = findkind(name)
        category = findtype(name)
        pic1 = findstock(kind)
    except Exception as e:
        return "<h1>發生錯誤！！！</h1>" + "錯誤訊息如下：" + "<br>" + str(e.args)

    description1 = "您的星座是" + name + "   " + "投資類型為:" + category
    description2 = "理財特質為" + random.choice(personalities[name])
    description3 = investment[pic1]
    description5 = "基於上述投資策略，我們為您推薦的股票是 -- " + pic1

    return render_template('results.html', name=name, description1=description1,description2=description2,description3 = description3,description5 = description5,pic1=pic1)



investment = {}
investment['2408'] = ["股價波動度高,股利殖利率低,創造現金流入能力中,償債能力低"]
investment['2474'] = ["股價波動度高,股利殖利率中高,創造現金流入能力高,償債能力高"]
investment['2454'] = ["股價波動度中高,股利殖利率中高,創造現金流入能力低,償債能力中高"]
investment['2330'] = ["股價波動度低,股利殖利率中,創造現金流入能力高,償債能力高"]
investment['2633'] = ["股價波動度中,股利殖利率低,創造現金流入能力低,償債能力中"]
investment['2303'] = ["股價波動度中高,股利殖利率中,創造現金流入能力中,償債能力中"]
investment['1216'] = ["股價波動度低,股利殖利率中,創造現金流入能力中,償債能力低"]
investment['2912'] = ["股價波動度中,股利殖利率低,創造現金流入能力中高,償債能力低"]
investment['2311'] = ["股價波動度中,股利殖利率中,創造現金流入能力中高,償債能力中"]
investment['2324'] = ["股價波動度低,股利殖利率高,創造現金流入能力低,償債能力中"]
investment['2317'] = ["股價波動度中,股利殖利率高,創造現金流入能力中,償債能力中高"]
investment['1402'] = ["股價波動度低,股利殖利率低,創造現金流入能力低,償債能力低"]

personalities = {}
personalities['牡羊座'] = ["注重如何快速讓資產增值，像賭徒般的追求高報酬，可接受高風險。","積極樂觀，喜歡冒險，善於把握時機出手迅速，敢於投資，能承受不可承受之敗仗，但也能擔起別人不可及之成功",
                        "小宇宙永遠都在燃燒，尤其擅長打破故舊成規，喜歡在沒變化的重複行為中找出樂趣，最容易一時興起買進用不到的東西，得先理債優於理財。"]


personalities["金牛座"] = ["穩定地累積財富，承擔適度風險，追求穩定報酬。","總有那股樸實勁，但又缺失安全感，對於理財也是慎重選擇，精打細算。",
                        "刻苦耐勞、堅忍不拔、凡事不躁進，用錢更是謹慎，但也因此在理財上容易犯下被自己的小心謹慎特性困住的窘境。",
                        "喜歡錢但不在乎。討厭幹沒有意義的事。"]

personalities["雙子座"] = ["積極累積財富，願意承擔較高風險，接受新推出的金融商品。","有著天使降臨人間的治癒和驚人的投資策略，也有惡魔主宰負面情緒的消極思想，對於付出行動的投資，可能更適合做一個投資理財的分析師。",
                        "擁有一顆「新鮮事」探索雷達，生活多采多姿，卻也容易踩上理財地雷，就是任何理財計畫永遠跟不上你多變的步伐。"]


personalities["巨蟹座"] = ["以安定為先，講求保護本金不受虧損及保持資產的流動性",
                        "家庭觀念意識強烈，保護家庭是原始責任感，所以對於家庭收入支出會有個平衡杆，而達到家庭和諧，定期理財會是他的首選。","浪漫體貼。細心關愛自己愛的人。","外表孩子氣，內心卻很成熟。",
                        "平常花錢相當節制，家人開銷往往是巨蟹最大的花費來源，想要讓理財計畫平順執行，愛家的巨蟹最好量力而為。"]

personalities["獅子座"] = ["積極累積財富，願意承擔較高風險，接受新推出的金融商品。","獅子是個王者，有高高在上的享受必有人後的埋汰，獅子是慷慨的，但也伴隨著利益的流失，仍需追逐開拓新的投資領域。",
                        "講義氣喜歡被人群圍繞、擁戴，對朋友跟另一半更是大方，理財誤區就在使用信用卡與追求名牌不曾設限，易把消費當作犒賞自己的主要方式。"]

personalities["處女座"] = ["以穩定為首要的考慮因素，追求低風險，可容忍低報酬。","凡是追求完美的個性，對於投資，只要是處女座出手一般都會有不錯的收益，所以哪類型的投資對它來說都是一樣的。",
                        "喜歡給自己訂出高標準，常低估自我能耐，因此，理財地雷在過度思考，反而無法看到更大的商機。","死要面子愛逞強。即使傷心也表現得十分強勢。"]

personalities["天秤座"] = ["穩定地累積財富，承擔適度風險，追求穩定報酬。","天秤心思淡定講究條理，對它來說投資越是簡單純粹就好，收益可以不用太高。",
                        "喜歡力求公平，卻常因為要考慮的事情太多了，最後打翻自己完美推演，導致理財計畫往往做的跟說的不一樣。"]

personalities["天蠍座"] = ["穩定地累積財富，承擔適度風險，追求穩定報酬。","天性善理，投資有一手，也能抓準時機，完善的風控措施是最理性的選擇。",
                        "「愛恨分明」是典型特質，延伸到金錢觀，該花時一擲千金、不該花時一毛不拔。","神秘。總希望別人瞭解自己內心。"]


personalities["射手座"] = ["注重如何快速讓資產增值，像賭徒般的追求高報酬，可接受高風險。","隨便了，記憶大概在7秒，愛投資甚麼就甚麼，它自己有想法，它不聽，你也攔不住。",
                        "不喜歡拘束，追求自由是個享樂主義派，做理財計畫時往往很認真，執行起來卻很隨便，尤其要避免低潮時做出重大投資決定，以免讓自己的財庫在不知不覺中洩洪。"]

personalities["魔羯座"] = ["以安定為先，講求保護本金不受虧損及保持資產的流動性。",
                        "專注單一，喜歡鑽研，投資會比較喜歡一步一步，徐徐漸進。",
                        "做事喜歡腳踏實地，對金錢卻特別容易感到不安，「太過保守」、「錯失投資良機」是最常在摩羯身上看到的理財誤區。"]

personalities["水瓶座"] = ["以穩定為首要的考慮因素，追求低風險，可容忍低報酬。","十二個星座里思想最天馬行空的，他們追求的是思想精神最高境界，「視金錢如糞土」錢夠花就行啦!",
                        "同時具備內斂與自由奔放2種靈魂，平常為了追求安定生活，可以量入為出，但性子一來，也能將全部的計畫拋在腦後，就把一整筆儲蓄毫不猶豫花光，擺盪的性格阻礙累積財富的步伐。"]

personalities["雙魚座"] = ["以穩定為首要的考慮因素，追求低風險，可容忍低報酬。",
                        "浪漫當然也需要物質去支撐，投資實物也是不錯的選擇，既有物質享受，也有將來升值可能。",
                        "天生浪漫，無時不在幻想，理財時容易將這種情結搬到現實中，不愛花時間過度理性分析，讓投資跟著感覺走。"]

if __name__=="__main__":
    app.run(debug=True)
