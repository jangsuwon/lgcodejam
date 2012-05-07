class BoxMap:
    def __init__(self):
        self.boxes = []
    def addBox(self,fromPoint,toPoint):
        self.boxes.append((fromPoint,toPoint))
    def isWay(self, fromPoint, toPoint):
        from_x,from_y = fromPoint
        to_x, to_y = toPoint
        result = False
        for (boxFromPoint,boxToPoint) in self.boxes:
            boxFrom_x, boxFrom_y = boxFromPoint
            boxTo_x, boxTo_y = boxToPoint
            if (from_x >= boxFrom_x) and (from_y >= boxFrom_y) and (to_x <= boxTo_x) and (to_y <= boxTo_y):
                result = True
                break
        return result
    def numOfWays(self, fromPoint, toPoint):
        from_x,from_y = fromPoint
        to_x,to_y = toPoint
        if from_x > to_x or from_y > to_y:
            return 0
        numOfWay = 0
        if (self.isWay(fromPoint, (from_x+1, from_y))):
            if (from_x+1, from_y) == toPoint:
                return 1
            else:
                numOfWay += self.numOfWays((from_x+1, from_y),(to_x,to_y))
        if (self.isWay(fromPoint, (from_x, from_y+1))):
            if (from_x, from_y+1) == toPoint:
                return 1
            else:
                numOfWay += self.numOfWays((from_x, from_y+1),(to_x,to_y))
        return numOfWay

if __name__ == '__main__':
    import sys
    f = sys.stdin
    numOfInput = int(f.readline().strip()) 
    for i in range(numOfInput):
        spec = f.readline().strip().split(" ")
        spec = [int(x) for x in spec]
        sfrom_x,sfrom_y,sto_x,sto_y = spec
        m = BoxMap() 
        numOfBoxes = int(f.readline().strip())
        for j in range(numOfBoxes):
            box = f.readline().strip().split(" ")
            box = [int(x) for x in box]
            from_x,from_y,to_x,to_y = box
            m.addBox((from_x,from_y),(to_x,to_y))
        print m.numOfWays((sfrom_x,sfrom_y),(sto_x,sto_y))
        
