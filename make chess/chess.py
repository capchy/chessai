import pygame as p
import chesseng
width = height =512
dimension = 8
sqsize=height//dimension
maxfps=60
images={}

def loadimages():
    pieces=["wp","wB","wK","wN","wQ","bp","bB","bK","bN","bQ","wR","bR"]
    for piece in pieces:
        images[piece]=p.transform.scale(p.image.load("images/"+ piece + ".png"),(sqsize,sqsize))

def main():
    p.init()
    screen=p.display.set_mode((width,height))
    clock=p.time.Clock()
    screen.fill(p.Color("white"))
    gs=chesseng.gamestate()
    loadimages()
    running=True
    sqselected =()
    playerclicks=[]
    while running:
        for i in p.event.get():
            if i.type==p.QUIT:
                running =False
            elif i.type== p.MOUSEBUTTONDOWN:
                location=p.mouse.get_pos()
                col=location[0]//sqsize
                row=location[1]//sqsize
                if sqselected==(row,col):
                    sqselected=()
                else:
                    sqselected=(row,col)
                    playerclicks.append(sqselected)
                
                if len(playerclicks)==2:
                    move = chesseng.move(playerclicks[0],playerclicks[1],gs.board)
                    print(move.getchessnotation())
                    gs.makemove(move)
                    sqselected=()
                    playerclicks=[]

        draw_board(screen,gs)
        clock.tick(maxfps)
        p.display.flip()


def draw_board(screen,gs):
    draw_squares(screen)
    draw_pieces(screen,gs.board)


def draw_squares(screen):
    colors=[p.Color("white"),p.Color("teal")]
    for r in range(dimension):
        for c in range(dimension):
            color=colors[((r+c)%2)]
            p.draw.rect(screen,color,p.Rect(c*sqsize,r*sqsize,sqsize,sqsize))

def draw_pieces(screen,board):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece !="--":
                screen.blit(images[piece],p.Rect(c*sqsize,r*sqsize,sqsize,sqsize))
    





if __name__=="__main__":
    main()