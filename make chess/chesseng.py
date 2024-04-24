class gamestate():
    def __init__(self):
        self.board=[
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--",],
            ["--","--","--","--","--","--","--","--",],
            ["--","--","--","--","--","--","--","--",],
            ["--","--","--","--","--","--","--","--",],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
             
        ]
        self.whitetomove=True
        self.movelog=[]
    def makemove(self,move):
        self.board[move.startrow][move.startcol]="--"
        self.board[move.endrow][move.endcol]=move.piecemoved
        self.whitetomove=not self.whitetomove
class move():
    rankstorows={"1":7,"2":6,"3":5,"4":4,"5":3,"6":2,"7":1,"8":0}
    rowstoranks={v: k for k, v in rankstorows.items()}
    filestocols={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
    colstofiles={v: k for k, v in filestocols.items()}

    def __init__(self,startsq,endsq,board):
        self.startrow=startsq[0]
        self.startcol=startsq[1]
        self.endrow=endsq[0]
        self.endcol=endsq[1]
        self.piecemoved= board[self.startrow][self.startcol]
        self.piececaptured= board[self.endrow][self.endcol]
    def getchessnotation(self):
        return self.getrankfile(self.startrow,self.startcol)+self.getrankfile(self.endrow,self.endcol)
    def getrankfile(self,r,c):
        return self.colstofiles[c]+self.rowstoranks[r]
   

