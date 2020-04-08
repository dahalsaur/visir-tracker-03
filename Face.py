import cv2

class Face():
    def __init__(self, area):
        self.id = -1
        self.area = area
        self.text = "unknown"

    def getId(self):
        return self.id
        
    def setId(self, newId):
        self.id = newId

    def getText(self):
        return self.text
        
    def setText(self, newText):
        self.text = newText

    def getArea(self):
        return self.area

    def setArea(self, newArea):
        self.area = newArea
