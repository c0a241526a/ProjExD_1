import os
import sys
import pygame as pg #pygameパッケージ(モジュール)をimport

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))#スクリーンsurfaceを作成 set_mode(,)
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#pg_bg.jpgを読み込む 背景画像のsurface
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])#スクリーンsurfaceの(0,0)にbg_img を貼り付ける　blit(画像,位置)でsurfaceに他のsurfaceを貼り付け
        pg.display.update()
        tmr += 1        
        clock.tick(10)#clock.tick(n)で1秒にn回while文を実行する


if __name__ == "__main__":#このプログラムから実行されたときのみ実行される
    pg.init()#pygameモジュールを初期化
    main()#main関数の内容は上にある
    pg.quit()#pygameモジュールの初期化を解除
    sys.exit()#システムの終了