from cs1graphics import *
from time import sleep

# create canvas
p = Canvas(1000, 600)
p.setTitle('FROG VS OWL')

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

# create frog
f = Layer() # frog layer
frog = Ellipse(60, 45)
frog.setFillColor('green2')
frog.setBorderWidth(1)
frog.moveTo(500, 500)

outsideEye1 = Circle(7)
outsideEye1.setFillColor('green2')
outsideEye1.setBorderWidth(1)
outsideEye1.moveTo(490, 480)
outsideEye2 = outsideEye1.clone()
outsideEye2.moveTo(510, 480)

insideEye1 = Circle(3)
insideEye1.setFillColor('white')
insideEye1.setBorderWidth(0)
insideEye1.moveTo(490, 480)
insideEye2 = insideEye1.clone()
insideEye2.moveTo(510, 480)


eye1 = Circle(2)
eye1.setFillColor('black')
eye1.setBorderWidth(0)
eye1.moveTo(490, 480)
eye2 = eye1.clone()
eye2.moveTo(510, 480)

nose1 = Circle(2)
nose1.setFillColor('green3')
nose1.setBorderWidth(0)
nose1.setDepth(5)
nose1.moveTo(497, 503)
nose2 = nose1.clone()
nose2.moveTo(503, 503)

mouth = Ellipse(30, 22.5)
mouth.setFillColor('green3')
mouth.setBorderWidth(0)
mouth.setDepth(25)
mouth.moveTo(500, 505)

mouthCoverUp = mouth.clone()
mouthCoverUp.setFillColor('green2')
mouthCoverUp.setDepth(20)
mouthCoverUp.move(0, -3)

# create owl
o = Layer() # layer for owl
owl = Ellipse(60, 45)
owl.setFillColor('brown4')
owl.setBorderWidth(1)
owl.moveTo(600, 500)

outerEye1 = Circle(15)
outerEye1.setFillColor('skyblue')
outerEye1.setBorderWidth(0)
outerEye1.moveTo(590, 500)
outerEye2 = outerEye1.clone()
outerEye2.move(20, 0)

innerEye1 = Circle(10)
innerEye1.setFillColor('white')
innerEye1.setBorderWidth(0)
innerEye1.moveTo(589, 500)
innerEye2 = innerEye1.clone()
innerEye2.move(22, 0)

owlEye1 = Circle(7)
owlEye1.setFillColor('black')
owlEye1.moveTo(589, 500)
owlEye2 = owlEye1.clone()
owlEye2.move(21, 0)

smallEye1 = Circle(2)
smallEye1.setFillColor('white')
smallEye1.setBorderWidth(0)
smallEye1.moveTo(589, 500)
smallEye2 = smallEye1.clone()
smallEye2.move(21, 0)

owlNose = Polygon(Point(600, 518), Point(595, 509), Point(605, 509))
owlNose.setFillColor('yellow')
owlNose.setBorderWidth(0)
owlNose1 = Circle(5)
owlNose1.setFillColor('yellow') # add some more detail for the nose
owlNose1.setBorderWidth(0)
owlNose1.moveTo(600, 510)

# set starting positions
f.move(-600, -100)
o.move(100, -150)

# add frog
f.add(frog)
f.add(outsideEye1)
f.add(outsideEye2)
f.add(insideEye1)
f.add(insideEye2)
f.add(eye1)
f.add(eye2)
f.add(nose1)
f.add(nose2)
f.add(mouth)
f.add(mouthCoverUp)
f.setDepth(20)
p.add(f)

# add owl to layer
o.add(owl)
o.add(outerEye1)
o.add(outerEye2)
o.add(innerEye1)
o.add(innerEye2)
o.add(owlEye1)
o.add(owlEye2)
o.add(smallEye1)
o.add(smallEye2)
o.add(owlNose)
o.add(owlNose1)
o.setDepth(20)
p.add(o)

# start animation

for i in range(0, 75):
    f.move(5, 0)
    sleep(0.033)

frogTalk = Text('Where is Ralph?', 12, Point(300, 360))
p.add(frogTalk)

for i in range(0, 30):
    sleep(0.033)

frogTalk.setMessage('')

for i in range(0, 35):
    o.move(-5, 1)
    sleep(0.033)

owlTalk = Text('Hey Rocky!', 12, Point(550, 350))
p.add(owlTalk)

for i in range(0, 30):
    sleep(0.033)

owlTalk.setMessage('')

for i in range(0, 30):
    sleep(0.033)

frogTalk.setMessage('You look small')

for i in range(0, 30):
    sleep(0.033)

frogTalk.setMessage('')

for i in range(0, 30):
    sleep(0.033)

owlTalk.setMessage("I'm the same size as you...")

for i in range(0, 30):
    sleep(0.033)

owlTalk.setMessage('')

for i in range(0, 30):
    sleep(0.033)

frogTalk.setMessage("No you're not")

for i in range(0, 30):
    sleep(0.033)

frogTalk.setMessage('')

for i in range(0, 30):
    sleep(0.033)

owlTalk.setMessage('ME ANGRY')

# set owl reference point before scaling
o.adjustReference(600, 500)

for i in range(0, 20):
    sleep(0.033)

owlTalk.setMessage('')

for i in range(0, 15):
    o.scale(1.05)
    sleep(0.033)

for i in range(0, 30):
    sleep(0.033)

frogTalk.setMessage('ok bye')

for i in range(0, 30):
    sleep(0.033)

frogTalk.setMessage('')

for i in range(0, 100):
    f.move(-5, 0)

frogTalk.move(310, 0)
frogTalk.setMessage('Hehe')

for i in range(0, 20):
    sleep(0.033)

frogTalk.setMessage('')

for i in range(0, 150):
    o.move(5, 0)
    sleep(0.033)
