if i.type==p.MOUSEBUTTONUP:
                    move = chesseng.move(playerclicks[0],playerclicks[1],gs.board)
                    print(move.getchessnotation())
                    gs.makemove(move)
                    sqselected=()
                    playerclicks=[]