import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_imgg = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 2, 1.0), pg.transform.rotozoom(kk_img, 4, 1.0), pg.transform.rotozoom(kk_img, 6, 1.0), pg.transform.rotozoom(kk_img, 8, 1.0), pg.transform.rotozoom(kk_img, 10, 1.0)]

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x = tmr%1600
        if x == 0:
            bg_img = pg.transform.flip(bg_img, True, False)
            bg_imgg = pg.transform.flip(bg_img, True, False)
    
        screen.blit(bg_img, (-x, 0))
        screen.blit(bg_imgg, (1600-x, 0))
        screen.blit(kk_imgs[tmr%5], [300,200])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()