import pyxel
import math
import random

pyxel.init(200,200)
pyxel.load("my_resource.pyxres")


ballx = [random.randint(0, 199)]
bally = [random.randint(-80,-30)]
vx = [math.cos(math.radians(random.randint(30, 150)))]
vy = [math.sin(math.radians(random.randint(30, 150)))]
n = [0] #左右どちらに動くか判定する変数
m = 0 #受け取った変数
l = 0 #受け損ねた変数
p = 0 #クリア数判定の変数
c = [random.randint(1, 8192)]#隠し要素
prysho = 0#ポリゴンショック変数
mas = [0] #ボールの性質を保存する変数（マスボ判定(とはいうものの、ボール判定なのでマスボだけじゃない)）
#０がモンボ(と愉快な仲間達),1がマスボ,2がマルマイン,3がクイックボール,
#4がポリゴンショック,5がネットボール(予定),6がウルトラボール(予定)
#追加される＋初回は必ずモンボ
speed = 3 #速度
padx = 100
qui = 0 #クイックボールの判定
get = 0 #getモードのスイッチ
#bgm
pyxel.playm(2, loop=True)

def update():
    global ballx, bally, angle, vx, vy, n, speed, padx, m, d,l,p,mas,qui,c,prysho,get
    if l >=20: #失敗後のやり直し判定
        if pyxel.btnp(pyxel.KEY_SPACE):
            ballx = [random.randint(0, 199)]
            bally = [random.randint(-80,-30)]
            vx = [math.cos(math.radians(random.randint(30, 150)))]
            vy = [math.sin(math.radians(random.randint(30, 150)))]
            n = [0] #左右どちらに動くか判定する変数
            m = 0 #受け取った変数
            l = 0 #受け損ねた変数
            p = 0 #クリア数判定の変数
            prysho = 0#ポリゴンショック変数
            c = [random.randint(1,8192)]#隠し要素
            get = 0 #getモードのスイッチ
            mas = [0] #ボールの性質を保存する変数（マスボ判定）#追加されるのは必ずモンボ
            speed = 3
            padx = 100
            pyxel.playm(2, loop=True)
        pass
    elif p >= 10: #クリア後のやり直し判定
        if pyxel.btnp(pyxel.KEY_SPACE):
            ballx = [random.randint(0, 199)]
            bally = [random.randint(-80,-30)]
            vx = [math.cos(math.radians(random.randint(30, 150)))]
            vy = [math.sin(math.radians(random.randint(30, 150)))]
            n = [0] #左右どちらに動くか判定する変数
            m = 0 #受け取った変数
            l = 0 #受け損ねた変数
            p = 0 #クリア数判定の変数
            prysho = 0#ポリゴンショック変数
            c = [random.randint(1,8192)]#隠し要素
            get = 0 #getモードのスイッチ
            mas = [0] #ボールの性質を保存する変数（マスボ判定）#追加されるのは必ずモンボ
            speed = 3
            padx = 100
        pass
    elif prysho ==1: #ポリゴンショック時のやり直し判定
        if pyxel.btnp(pyxel.KEY_SPACE):
            ballx = [random.randint(0, 199)]
            bally = [random.randint(-80,-30)]
            vx = [math.cos(math.radians(random.randint(30, 150)))]
            vy = [math.sin(math.radians(random.randint(30, 150)))]
            n = [0] #左右どちらに動くか判定する変数
            m = 0 #受け取った変数
            l = 0 #受け損ねた変数
            p = 0 #クリア数判定の変数
            prysho = 0#ポリゴンショック変数
            c = [random.randint(1,8192)]#隠し要素
            get = 0 #getモードのスイッチ
            mas = [0] #ボールの性質を保存する変数（マスボ判定）#追加されるのは必ずモンボ
            speed = 3
            padx = 100
            pyxel.stop()
            pyxel.playm(2, loop=True)
        pass
    elif pyxel.btnp(pyxel.KEY_SPACE):#通常時のやり直し判定
        ballx = [random.randint(0, 199)]
        bally = [random.randint(-80,-30)]
        vx = [math.cos(math.radians(random.randint(30, 150)))]
        vy = [math.sin(math.radians(random.randint(30, 150)))]
        n = [0] #左右どちらに動くか判定する変数
        m = 0 #受け取った変数
        l = 0 #受け損ねた変数
        p = 0 #クリア数判定の変数
        prysho = 0#ポリゴンショック変数
        c = [random.randint(1,8192)]#隠し要素
        get = 0 #getモードのスイッチ
        mas = [0] #ボールの性質を保存する変数（マスボ判定）#追加されるのは必ずモンボ
        speed = 3
        padx = 100
        pyxel.playm(2, loop=True)
        pass

    else:

#処理開始

        for i in range(0,len(ballx)):

#ボールが右端と左端に行ってしまったときの処理について、反転の処理
#cosがマイナス値を引いた時に反転しないバグを修正するために煩雑になってしまった。
            if ballx[i] > 200:
                if vx[i] >= 0:
                    n[i] = 1
                else:
                    n[i] = 0
            elif ballx[i] < 0:
                if vx[i] >= 0:
                    n[i] = 0
                else:
                    n[i] = 1

#ボールの挙動について
            if n[i] == 0:
                ballx[i] = ballx[i]+(vx[i]*speed)
                bally[i] = bally[i]+(vy[i]*speed)
            elif n[i] == 1:
                ballx[i] = ballx[i]+(-vx[i]*speed)
                bally[i] = bally[i]+(vy[i]*speed)


#当たり判定
            if (padx-22 < ballx[i] < padx+22) and (bally[i] > 195):
                #当たり判定を左右合わせて4だけ強化
                    if l < 20:
                        if mas[i]==2:
                            pyxel.playm(0)
                        elif mas[i] ==4:
                            pass
                        else:
                            pyxel.playm(1)

                    if m < 9:
                        if mas[i]==1:#マスボの処理
                            m=0
                            ballx.append(random.randint(0, 199))
                            bally.append(random.randint(-80,-30))
                            mas.append(0)
                            vx.append(math.cos(math.radians(random.randint(30, 150))))
                            vy.append(math.sin(math.radians(random.randint(30, 150))))
                            n.append(0)
                            c.append(random.randint(1,8192))
                            p+=1
                            speed = 3
                            #速度を戻す
                            mas[i]=0
                            #マスボだけ特別扱い、スコアを1あげる
                            #マスボは特別なのでモンボに戻します。

                        elif mas[i] ==2:#マルマインの処理
                            if get > 0:
                                get -= 1
                                pyxel.playm(3)
                                m += 2
                                speed *= 1.15
                            else:
                                #マルマインを拾った場合は、
                                #これまでに集めたポイントを消失させ、スコアを１減らす.
                                pyxel.playm(0)
                                m=0
                                p-=1
                                mas[i]=0
                                #踏んじゃった時はかわいそうなので強制的にモンボに戻します
                                #スピードも増やしません
                                #マルマインは合法的にスピードを落とすことのできる手段です。

                        elif mas[i]==3:#クイックボールの処理
                            l -= 4 #ライフを4回復
                            m += 1 #普通に１点分加算
                            speed =15 #一瞬めっちゃ早くなる
                            qui = 10
                            speed *= 1.15 #スピード加算
                            #少しの間(ボール10個分)マスボの出やすさ3倍、マルマインが出ない

                        elif mas[i]==4:#ポリゴンショックの処理
                            prysho = 1
                            pyxel.stop()
                            #ポリゴンショック状態に移行

                        elif mas[i]==5:#ネットボールの処理
                            get += 3 #3回までマルマインをゲットできる
                            m += 1
                            speed *= 1.15
                            #GETモードに移行

                        else:#通常ボールの処理
                            m += 1
                            speed *= 1.15
                            #速度を1.15倍する
                    elif m >= 9:
                        m = 0
                        #ボール追加
                        ballx.append(random.randint(0, 199))
                        bally.append(random.randint(-80,-30))
                        mas.append(0)
                        vx.append(math.cos(math.radians(random.randint(30, 150))))
                        vy.append(math.sin(math.radians(random.randint(30, 150))))
                        n.append(0)
                        c.append(random.randint(1,8192))
                        p += 1
                        speed = 3
                        #速度を戻す
                    #ひとまず拾えた場合、上にボールを戻す処理
                    ballx[i] = random.randint(0, 199)
                    bally[i] = random.randint(-30, -80)

#当たった時　次回のボール判定
                    if mas[i] == 0:
                        if p <=5:
                            if random.randint(1,100) >= 96:#5%でマスボ
                                mas[i] = 1
                            elif (random.randint(1,100)<= 30)and(p>=1):
                                #30%の確率でマルマイン
                                #クイックボールだけ特殊な判定
                                if qui > 0 :
                                    qui -= 1
                                    if random.randint(1,100) >= 86:#15%でマスボ
                                        mas[i] = 1
                                    elif 71 <= random.randint(1,100) <=75:
                                        mas[i] = 3 #クイックボールは5％
                                    elif 76 <= random.randint(1,100) <=78:
                                        mas[i] = 5 #ネットボールは3％
                                else:
                                    mas[i] = 2
                            #p>=1の条件は、マイナスになった時の処理が面倒なので。
                            elif 71 <= random.randint(1,100) <=75:
                                mas[i] = 3 #クイックボールは5％
                            elif 76 <= random.randint(1,100) <=78:
                                mas[i] = 5 #ネットボールは3％
                            else:
                                mas[i] = 0

                        elif 5< p<= 7:#クリア度合いに応じてマルマイン度合いをあげていく
                            if random.randint(1,100) >= 96:#5%
                                mas[i] = 1
                            elif (random.randint(1,100) <= 50)and(p>=1):#50%の確率でマルマイン
                                #クイックボールだけ特殊な判定
                                if qui > 0 :
                                    qui -= 1
                                    if random.randint(1,100) >= 86:#15%でマスボ
                                        mas[i] = 1
                                    elif 71 <= random.randint(1,100) <=75:
                                        mas[i] = 3 #クイックボールは5％
                                    elif 76 <= random.randint(1,100) <=78:
                                        mas[i] = 5 #ネットボールは3％
                                else:
                                    mas[i] = 2

                            elif 71 <= random.randint(1,100) <=75:
                                mas[i] = 3 #クイックボールは5％
                            elif 76 <= random.randint(1,100) <=78:
                                mas[i] = 5 #ネットボールは3％
                            else:
                                mas[i] = 0

                        else:#クリア度合いに応じてマルマイン度合いをあげていく
                            if random.randint(1,100) >= 96:#5%
                                mas[i] = 1
                            elif (random.randint(1,100)<= 70)and(p>=1):#70%の確率でマルマイン
                                #クイックボールだけ特殊な判定
                                if qui > 0 :
                                    qui -= 1
                                    if random.randint(1,100) >= 86:#15%でマスボ
                                        mas[i] = 1
                                    elif 71 <= random.randint(1,100) <=75:
                                        mas[i] = 3 #クイックボールは5％
                                    elif 76 <= random.randint(1,100) <=78:
                                        mas[i] = 5 #ネットボールは3％
                                else:
                                    mas[i] = 2
                            elif 71 <= random.randint(1,100) <=75:
                                mas[i] = 3 #クイックボールは5％
                            elif 76 <= random.randint(1,100) <=78:
                                mas[i] = 5 #ネットボールは3％
                            else:
                                mas[i] = 0
                    else:#モンボじゃない場合はモンボに戻します
                        mas[i] = 0

                    #ポリゴン判定
                    if c[i] == 137:
                        mas[i] = 4

                    #1/11でプレミアボールスキン(10個買った時のおまけなので)
                    #プレミアボール,スーパーボールの時は得点2
                    if 1 <= c[i] <= 1488 :
                        m += 1
                    # ハイパーボールは得点3
                    elif 1489 <= c[i] <= 1860 :
                        m += 2


                    vx[i] = math.cos(math.radians(random.randint(30, 150)))
                    vy[i] = math.sin(math.radians(random.randint(30, 150)))
                    c[i] = random.randint(1,8192)


#当たり判定をすり抜けたボールのリセット
#ハズレ音
            if bally[i] > 200:

                if l < 20:
                    if mas[i]==2:
                        pass
                    elif mas[i]== 4:
                        pass
                    else:
                    #マルマインとポリゴンはすり抜けて正解なので音を入れません
                        pyxel.playm(0)
                        l += 1
#ボール生成
                ballx[i] = random.randint(0, 199)
                bally[i] = random.randint(-80,-30)
                vx[i] = math.cos(math.radians(random.randint(30, 150)))
                vy[i] = math.sin(math.radians(random.randint(30, 150)))
                c[i] = random.randint(1,8192)

#外れた時のボールの種類判定
                #マルマインは場合分けが必要
                if mas[i]==2:
                    if p <=5:
                        if random.randint(1,100) >= 91:#10%でマスボ
                            mas[i] = 1
                        elif (random.randint(1,100) <= 30)and(p>=1):#30%の確率でマルマイン
                            #クイックボールだけ特殊な判定
                            if qui > 0 :
                                qui -= 1
                                if random.randint(1,100) >= 86:#15%でマスボ
                                    mas[i] = 1
                                elif 71 <= random.randint(1,100) <=75:
                                    mas[i] = 3 #クイックボールは5％
                                elif 76 <= random.randint(1,100) <=78:
                                    mas[i] = 5 #ネットボールは3％
                            else:
                                mas[i] = 2
                        #p>=1の条件は、マイナスになった時の処理が面倒なので。
                        elif 71 <= random.randint(1,100) <=75:
                            mas[i] = 3 #クイックボールは5％
                        elif 76 <= random.randint(1,100) <=78:
                            mas[i] = 5 #ネットボールは3％
                        else:
                            mas[i] = 0

                    elif 5< p<= 7:#クリア度合いに応じてマルマイン度合いをあげていく
                        if random.randint(1,100) >= 91:#すり抜けた場合は次回の判定を10%に
                            mas[i] = 1
                        elif (random.randint(1,100) <= 50)and(p>=1):#50%の確率でマルマイン
                            #クイックボールだけ特殊な判定
                            if qui > 0 :
                                qui -= 1
                                if random.randint(1,100) >= 86:#15%でマスボ
                                    mas[i] = 1
                                elif 71 <= random.randint(1,100) <=75:
                                    mas[i] = 3 #クイックボールは5％
                                elif 76 <= random.randint(1,100) <=78:
                                    mas[i] = 5 #ネットボールは3％
                            else:
                                mas[i] = 2

                        elif 71 <= random.randint(1,100) <=75:
                            mas[i] = 3 #クイックボールは5％
                        elif 76 <= random.randint(1,100) <=78:
                            mas[i] = 5 #ネットボールは3％
                        else:
                            mas[i] = 0

                    else:#クリア度合いに応じてマルマイン度合いをあげていく
                        if random.randint(1,100) >= 91:#すり抜けた場合は次回の判定を10%に
                            mas[i] = 1
                        elif (random.randint(1,100)<= 70)and(p>=1):#70%の確率でマルマイン
                            #クイックボールだけ特殊な判定
                            if qui > 0 :
                                qui -= 1
                                if random.randint(1,100) >= 86:#15%でマスボ
                                    mas[i] = 1
                                elif 71 <= random.randint(1,100) <=75:
                                    mas[i] = 3 #クイックボールは5％
                                elif 76 <= random.randint(1,100) <=78:
                                    mas[i] = 5 #ネットボールは3％
                            else:
                                mas[i] = 2
                        elif 71 <= random.randint(1,100) <=75:
                            mas[i] = 3 #クイックボールは5％
                        elif 76 <= random.randint(1,100) <=78:
                            mas[i] = 5 #ネットボールは3％
                        else:
                            mas[i] = 0

                elif mas[i] == 0:#モンボの処理
                    if random.randint(1,100) >= 96:#5％でマスボ
                        mas[i] = 1
                    elif (random.randint(1,100)<= 50)and(p>=1):#50%の確率でマルマイン(一律)
                        #クイックボールだけ特殊な判定
                        if qui > 0 :
                            qui -= 1
                            if random.randint(1,100) >= 86:#15%でマスボ
                                mas[i] = 1
                            elif 71 <= random.randint(1,100) <=75:
                                mas[i] = 3 #クイックボールは5％
                            elif 76 <= random.randint(1,100) <=78:
                                mas[i] = 5 #ネットボールは3％
                        else:
                            mas[i] = 2
                    elif 71 <= random.randint(1,100) <=75:
                        mas[i] = 3 #クイックボールは5％
                    elif 76 <= random.randint(1,100) <=78:
                        mas[i] = 5 #ネットボールは3％
                    else:
                        mas[i] = 0
                    #モンボを落とした場合は通常通り
                else:
                    mas[i]=0
                    #特殊ボールは全てモンボに戻す

                #ポリゴン判定
                if c[i] == 137:
                    mas[i] = 4



#スピードが早くなりすぎるとゲームが成り立たないので上限値を設定
    #下に落ちた時は失敗しているので、速度を変化させない
    #ライフ１と引き換えに速度を落とすのは面白そうなので採用↓
                speed =3
                #マルマインでも発動するのでいい難易度調整になってそう
#スピード
            if mas[i]==3:
                speed = 15
            else:
                if speed > 7:#スピードが早くなりすぎるとゲームが成り立たないので上限値を設定
                    speed = 7


#マウス
        padx = pyxel.mouse_x
#操作感を上げるためにウィンドウの端まで行ったら、判定板が端に止まるようにした。
        if padx <= 20:
            padx =20
        elif padx >= 180:
            padx =180





def draw():
    global ballx, bally, angle, vx, vy, n, speed, padx, m, d,l,p,mas,qui,c,prysho
#背景をモンスターボール色にする
    pyxel.cls(7)
    pyxel.rect(0, 0, 200, 100, 8)
    pyxel.rect(0,97,200,5,0)
    pyxel.circ(100,100 , 15, 0)
    pyxel.circ(100,100 , 10, 7)
    pyxel.circb(100, 100, 8, 0)

    if l >= 20:
        pyxel.text(85, 150, "YOU LOSE", 0)
        pyxel.text(85, 160, "SCORE: " + str(p), 0)
        pyxel.text(55, 140, "Press space to NEW GAME",0)
        pyxel.stop()
    elif prysho == 1:
        if pyxel.frame_count %2 ==0:
            pyxel.cls(12)
        else:
            pyxel.cls(14)
        pyxel.text(85, 150, "YOU LOSE", 0)
        pyxel.text(85, 160, "SCORE: " + str(p), 0)
        pyxel.text(55, 140, "Press space to NEW GAME",0)
        pyxel.playm(0)
    else:
        for i in range(0,len(ballx)):
            if mas[i]==0:
                if c[i] == 4096:#ダイパ色違いの確率でピカチュウスキン
                    pyxel.blt(ballx[i]-8, bally[i]-8, 0, 16, 32, 16, 16, 1)
                elif 382 <= c[i] <= 393 :#国際孵化の確率でポッチャマスキン
                    pyxel.blt(ballx[i]-8, bally[i]-8, 0, 32, 32, 16, 16, 1)
                elif 1 <= c[i] <= 744 :#1/11でプレミアボールスキン(10個買った時のおまけなので)
                #ポッチャマと範囲重複してるけどなんとかなるっしょ
                    pyxel.blt(ballx[i]-8, bally[i]-8, 0, 32, 16, 16, 16, 1)
                elif 745 <= c[i] <= 1488 :#プレミアボールくらいっしょ
                    pyxel.blt(ballx[i]-8, bally[i]-8, 0, 32, 0, 16, 16, 1)
                elif 1489 <= c[i] <= 1860 :#ハイパーボールはスーパーボールの半分くらいのレア度
                    pyxel.blt(ballx[i]-8, bally[i]-8, 0, 48, 0, 16, 16, 1)
                else:
                    pyxel.blt(ballx[i]-8, bally[i]-8, 0, 0,0, 16, 16, 1)
            elif mas[i]==2:
                pyxel.blt(ballx[i]-8, bally[i]-8, 0, 16, 16, 16, 16, 1)
            elif mas[i]==3:
                pyxel.blt(ballx[i]-8, bally[i]-8, 0, 48, 16, 16, 16, 1)
            elif mas[i]==1:
                pyxel.blt(ballx[i]-8, bally[i]-8, 0, 16, 0, 16, 16, 1)
            elif mas[i]==4:
                pyxel.blt(ballx[i]-8, bally[i]-8, 0, 0, 48, 16, 16, 1)
            elif mas[i]==5:
                pyxel.blt(ballx[i]-8, bally[i]-8, 0, 48, 32, 16, 16, 1)
        pyxel.rect(padx-20, 195, 40, 5, 0)
#モンスターボール色を読み込む
        pyxel.text(10, 10, "POINT: " + str(m), 0)
        pyxel.text(10, 20, "SCORE: " + str(p), 0)
        pyxel.text(10, 30, "LIFE: " + str(20-l), 0)
        if get >= 1:
            pyxel.text(10, 40, "GET MODE: "+ str(get), 0)
        if p >= 10:
            #背景をモンスターボール色にする
            pyxel.cls(7)
            pyxel.rect(0, 0, 200, 100, 8)
            pyxel.rect(0,97,200,5,0)
            pyxel.circ(100,100 , 15, 0)
            pyxel.circ(100,100 , 10, 7)
            pyxel.circb(100, 100, 8, 0)
            pyxel.text(85, 130, "YOU WIN!", 0)
            pyxel.text(80, 140, "SCORE: " + str(p), 0)
            pyxel.text(55, 150, "Press space to NEW GAME",0)
pyxel.run(update, draw)
