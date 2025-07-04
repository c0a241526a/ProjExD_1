import os
import sys
import pygame as pg #pygameパッケージ(モジュール)をimport

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))#スクリーンsurfaceを作成 set_mode(,)
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#pg_bg.jpgを読み込む 背景画像のsurface
    bg_img2 = pg.transform.flip(bg_img,True,False)#画像を反転させて画像を繋げるための画像
    koukaton_img = pg.image.load("fig/3.png")#こうかとんの画像
    koukaton_img = pg.transform.flip(koukaton_img,True,False)#こうかとんの画像を左右反転 transform.flip(画像,左右反転T/F,上下反転T/F)
    koukaton_rct = koukaton_img.get_rect()#koukaton_imgから対応するrectを変数に代入　こうかとんの画像のrect
    koukaton_rct.center=300,200#rectに位置を設定

    tmr = 0

    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x=tmr%3200#+=だと左へ移動するのためbiltの方は-にする    tmr%3200でtmr=3200の余りを出すので0~3199の間になる

        key_lst=pg.key.get_pressed()#すべてのキーの押下状態(押されているか)を取得(T/Fで出力)
        if key_lst:#キーボードが押されていないとき
            move_RL=-1
            move_OD=0#背景画像と同じ速度で流れる
        if key_lst[pg.K_RIGHT]:#K_UPはキーボードの→が押されているときにTrue
            move_RL+=2
            move_OD=0
        if key_lst[pg.K_UP]:#K_UPはキーボードの↑が押されているときにTrue
            move_RL-=1
            move_OD-=1
        if key_lst[pg.K_DOWN]:#K_UPはキーボードの↓が押されているときにTrue
            move_RL-=1
            move_OD+=1
        if key_lst[pg.K_LEFT]:#K_UPはキーボードの←が押されているときにTrue
            move_RL-=1
            move_OD=0


        koukaton_rct.move_ip((move_RL,move_OD))#(左右の移動,上下の移動)

        
        screen.blit(bg_img, [-x, 0])#スクリーンsurfaceの(横,縦)にbg_img を貼り付ける　blit(画像,位置)でsurfaceに他のsurfaceを貼り付け
        screen.blit(bg_img2, [-x+1600, 0])#スクリーンが連続しているようにみせる 画像を反転させて画像を繋げる
        screen.blit(bg_img, [-x+3200, 0])#元の画像をつなげて背景をループさせる 画像の横幅は1600
        #screen.blit(koukaton_img, [300, 200]) rectの方を使用
        screen.blit(koukaton_img,koukaton_rct)#koukaton_rctに位置の設定がされている
        pg.display.update()
        tmr += 1  #while1回ごとに増加 
        clock.tick(200)#clock.tick(n)で1秒にn回while文を実行する


if __name__ == "__main__":#このプログラムから実行されたときのみ実行される
    pg.init()#pygameモジュールを初期化
    main()#main関数の内容は上にある
    pg.quit()#pygameモジュールの初期化を解除
    sys.exit()#システムの終了