class Square():

    square_list = []

    def __init__(self, s):
        self.side = s
        self.square_list.append(self.side)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side,self.side)

square1 = Square(3)
square2 = Square(5)
square3 = Square(7)

print(square1)
print(Square.square_list)

        
