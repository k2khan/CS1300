
class Point:
    """A model for a two-dimensional Cartesian point."""
    def __init__(self, x=0, y=0):
        """Construct a point with initial coordinates (x,y).

        Default (x,y) is (0,0).
        """
        self._x = x
        self._y = y
        
    def getX(self):
        """Return the x-coordinate of the point."""
        return self._x

    def setX(self, val):
        """Set the x-coordinate of the point to the given value.

        The value should be numeric.
        """
        self._x = val

    def getY(self):
        """Return the y-coordinate of the point."""
        return self._y

    def setY(self, val):
        """Set the y-coordinate of the point to the given value.

        The value should be numeric.
        """
        self._y = val

if __name__ == '__main__':
    pt1 = Point (25, 40)
    print ('pt1 = <' + str(pt1.getX()) + ',' + str(pt1.getY()) + '>')
    pt2 = Point (10, 75)
    print ('pt2 = <' + str(pt2.getX()) + ',' + str(pt2.getY()) + '>')
    pt1.setX (pt2.getY())
    pt1.setY (pt2.getX())
    print ('pt1 = <' + str(pt1.getX()) + ',' + str(pt1.getY()) + '>')
    
    
