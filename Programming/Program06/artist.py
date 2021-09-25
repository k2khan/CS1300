from cs1graphics import *
from time import sleep

class Frog(Layer):
    """A class for making a 2d Frog."""
    def __init__(self, xPos=550, yPos=350, bodyColor='green2', featureColor='green3', eyeColor='black'):
        """Creates a new instance of a Frog.
        The reference point is intialized to be the same point as the xPos and yPos

        xPos is initially 550
        yPos is initially 350
        bodyColor is initially 'green2'
        featureColor is initially 'green3'
        eyeColor is initially 'black'

        xPos, yPos should be numeric
        bodyColor, featureColor, eyeColor should be strings
        """
        super().__init__()
        self._xPos = xPos 
        self._yPos = yPos
        self._bodyColor = bodyColor
        self._featureColor = featureColor
        self._eyeColor = eyeColor

        self._frog = Ellipse(60, 45)
        self._frog.setFillColor(self._bodyColor)
        self._frog.setBorderWidth(1)
        self._frog.moveTo(xPos, yPos)

        self._outsideEye1 = Circle(7)
        self._outsideEye1.setFillColor(self._bodyColor)
        self._outsideEye1.setBorderWidth(1)
        self._outsideEye1.moveTo(xPos-10, yPos-20)
        self._outsideEye2 = Circle(7)
        self._outsideEye2.setFillColor(self._bodyColor)
        self._outsideEye2.moveTo(xPos+10, yPos-20)
        self._outsideEye2.setBorderWidth(1)

        self._insideEye1 = Circle(3)
        self._insideEye1.setFillColor('white')
        self._insideEye1.setBorderWidth(0)
        self._insideEye1.moveTo(xPos-10, yPos-20)
        self._insideEye2 = self._insideEye1.clone()
        self._insideEye2.moveTo(xPos+10, yPos-20)


        self._eye1 = Circle(2)
        self._eye1.setFillColor(self._eyeColor)
        self._eye1.setBorderWidth(0)
        self._eye1.moveTo(xPos-10, yPos-20)
        self._eye2 = Circle(2)
        self._eye2.moveTo(xPos+10, yPos-20)
        self._eye2.setFillColor(self._eyeColor)
        self._eye2.setBorderWidth(0)

        self._nose1 = Circle(2)
        self._nose1.setFillColor(self._featureColor)
        self._nose1.setBorderWidth(0)
        self._nose1.setDepth(5)
        self._nose1.moveTo(xPos-3, yPos+3)
        self._nose2 = Circle(2)
        self._nose2.setFillColor(self._featureColor)
        self._nose2.setBorderWidth(0)
        self._nose2.setDepth(5)
        self._nose2.moveTo(xPos+3, yPos+3)

        self._mouth = Ellipse(30, 22.5)
        self._mouth.setFillColor(self._featureColor)
        self._mouth.setBorderWidth(0)
        self._mouth.setDepth(25)
        self._mouth.moveTo(xPos, yPos+5)

        self._mouthCoverUp = self._mouth.clone()
        self._mouthCoverUp.setFillColor(self._bodyColor)
        self._mouthCoverUp.setDepth(20)
        self._mouthCoverUp.move(0, -3)
        
        # add frog to layer
        self.add(self._frog)
        self.add(self._outsideEye1)
        self.add(self._outsideEye2)
        self.add(self._insideEye1)
        self.add(self._insideEye2)
        self.add(self._eye1)
        self.add(self._eye2)
        self.add(self._nose1)
        self.add(self._nose2)
        self.add(self._mouth)
        self.add(self._mouthCoverUp)
        self.setDepth(20)
        self.adjustReference(self._xPos, self._yPos) #Sets the reference point to each initialized frog to the center of the position of the frog

    def adjustBodyColor(self, color):
        """Adjusts the color of the Frog's body.

        The value should be a string.
        """
        if not isinstance(color, str): #Checks for correct input
            raise TypeError('Please enter a string')
        self._frog.setFillColor(color)
        self._outsideEye1.setFillColor(color)
        self._outsideEye2.setFillColor(color)
        self._mouthCoverUp.setFillColor(color)

    def adjustEyeColor(self, color):
        """Adjusts the color of the Frog's eyes.

        The value should be a string.
        """
        if not isinstance(color, str):
            raise TypeError('Please enter a string')
        self._eye1.setFillColor(color)
        self._eye2.setFillColor(color)


    def adjustFeatureColor(self, color):
        """Adjusts the color of the Frog's nose and mouth.

        The value should be a string.
        """
        if not isinstance(color, str): #Checks for correct input
            raise TypeError('Please enter a string')
        self._nose1.setFillColor(color)
        self._nose2.setFillColor(color)
        self._mouth.setFillColor(color)
    
    def dance(self):
        """Makes the Frog 'dance' by making it go side to side."""
        self.rotate(-10)
        sleep(0.333)
        for i in range(3):
            self.rotate(20)
            sleep(0.333)
            self.rotate(-20)
            sleep(0.333)
        self.rotate(10) #This last rotate is done so that the frog is standing straight

    def swerve(self):
        """Rotates/spins the frog around a reference point."""
        self.adjustReference(-20, -20)
        for i in range(72):
            self.rotate(5)
            sleep(0.003)


if __name__ == '__main__':
    # create canvas
    p = Canvas(1000, 600)
    p.setTitle('Frogs')

    # create background
    grass = Rectangle(1000, 300)
    grass.setFillColor('lawn green')
    grass.moveTo(500, 450)
    grass.setBorderWidth(0)
    p.add(grass)

    sky = Rectangle(1000, 300)
    sky.setFillColor('sky blue')
    sky.moveTo(500, 150)
    sky.setBorderWidth(0)
    p.add(sky)


    # create tree
    treeLayer = Layer()

    tree = Polygon(Point(200, 225), Point(250, 300), Point(150, 300))
    tree.setFillColor('darkgreen')
    tree.setDepth(10)
    treeLayer.add(tree)

    tree1 = tree.clone()
    tree1.moveTo(200, 225)
    treeLayer.add(tree1)

    tree2 = tree.clone()
    tree2.moveTo(200, 250)
    treeLayer.add(tree2)

    wood = Rectangle(35, 75)
    wood.setFillColor('brown')
    wood.setBorderWidth(0)
    wood.moveTo(200, 350)
    wood.setDepth(75)
    treeLayer.add(wood)

    # tree detail
    marking1 = Path(Point(205, 327.5), Point(212.5, 342.5), Point(205, 360), Point(212.5, 377.5))
    marking2 = Path(Point(190, 327.5), Point(197.5, 342.5), Point(190, 360), Point(197.5, 377.5))

    treeLayer.add(marking2)
    treeLayer.add(marking1)

    p.add(treeLayer)

    # make multiple trees
    tree1 = treeLayer.clone()
    tree1.moveTo(400, -50)
    tree1.setDepth(10)
    p.add(tree1)

    tree2 = treeLayer.clone()
    tree2.moveTo(250, -25)
    tree2.setDepth(10)
    p.add(tree2)

    tree3 = treeLayer.clone()
    tree3.moveTo(500, 50)
    tree3.setDepth(10)
    p.add(tree3)

    tree4 = treeLayer.clone()
    tree4.moveTo(200, 100)
    tree4.setDepth(30)
    p.add(tree4)

    tree5 = treeLayer.clone()
    tree5.moveTo(-50, 150)
    tree5.setDepth(10)
    p.add(tree5)

    f1 = Frog()
    p.add(f1)
    f1.dance()
    
    f2 = Frog(300, 300, 'red', 'yellow', 'black')
    p.add(f2)
    f2.swerve()

    f3 = Frog(800, 400, 'pink', 'purple', 'red') 
    p.add(f3)
    f3.dance()

    f4 = Frog(500, 500, 'blue', 'green2', 'black')
    p.add(f4)
    f4.swerve()
