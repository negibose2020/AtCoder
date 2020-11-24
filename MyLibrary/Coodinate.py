class Coodinate (object):
    """Coodinate object
    This class contains infomation about the coodinates.
    Each instance can have up to 3-dimensional(x,y,z) space coodinates.
    
    params
    ------------------------------
    x : int or floot ,default 0
    y : int or floot ,default 0
    z : int or floot ,default 0


    This class have following methods.
    ------------------------------
    distance : Calculate the straight-line distance between 2 points in Euclidean space.
    midpoint : Calculate the midpoint(halfway) between 2 points.
    manhattan_distance : Calculate the distance between 2 points that is sum of the absolute values their Cartesian coordinates.
    """

    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z


    def __str__(self):
        if self.z==0:
            if self.y==0:
                return "( {} )".format(self.x)
            else :
                return "( {} , {} )".format(self.x,self.y)
        else:
            return "( {} , {} , {} )".format(self.x,self.y,self.z)    


    def distance(self,other):
        """Calculate the straight-line distance between 2 points in Euclidean space.

        params
        ----------
        self : Coodinate object
        other : Coodinate object

        return
        ----------
        distance : floot

        """
        x_diff_sq=(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        z_diff_sq=(self.z-other.z)**2
        return (x_diff_sq + y_diff_sq +z_diff_sq)**0.5
    

    def midpoint(self,other):
        """Calculate the midpoint(halfway) between 2 points.

        params
        ----------
        self : Coodinate object
        other : Coodinate object

        return
        ----------
        midpoint : tupul
        
        """
        x_midpoint=(self.x+other.x)/2
        y_midpoint=(self.y+other.y)/2
        z_midpoint=(self.z+other.z)/2
        if self.z == other.z ==0 :
            if self.y == other.y==0:
                return(x_midpoint)
            else:
                return(x_midpoint,y_midpoint) 
        return(x_midpoint,y_midpoint,z_midpoint)

    def manhattan_distance(self,other):
        """Calculate the distance between 2 points that is sum of the absolute values their Cartesian coordinates.

        params
        ----------
        self : Coodinate object
        other : Coodinate object

        return
        ----------
        manhattan_distance : floot

        """

        x_diff_abs=abs(self.x - other.x)
        y_diff_abs=abs(self.y - other.y)
        z_diff_abs=abs(self.z - other.z)
        return(x_diff_abs + y_diff_abs + z_diff_abs)

    def lineSlopeGivenTwoPoints(self,other):
        if self.z!=0 or other.z!=0:
            return False
        if self==other:
            return False
        deltax=self.x - other.x
        deltay=self.y - other.y
        if deltax==0:
            return "x={}".format(self.x)
        if deltay==0:
            return "y={}".format(self.y)
        slope=deltay/deltax
        return slope

    def y_interceptGivenTwoPoints(self,other):
        if self.z!=0 or other.z!=0:
            return False
        s=Coodinate.lineSlopeGivenTwoPoints(self,other)
        if type(s)!=str:
            y_intercept=self.y-s*self.x
            return y_intercept
        elif s[0]=="y":
            return int(s[2:])
        else:
            return None

    def x_interceptGivenTwoPoints(self,other):
        if self.z!=0 or other.z!=0:
            return False
        s=Coodinate.lineSlopeGivenTwoPoints(self,other)
        if type(s)!=str:
            y_intercept=self.y-s*self.x
            x_intercept=-1*y_intercept/s
            return x_intercept
        elif s[0]=="x":
            return int(s[2:])
        else:
            return None

a=Coodinate(1,1)
b=Coodinate(1,2)
c=Coodinate(1,3)
m1=Coodinate.lineSlopeGivenTwoPoints(a,b)
m2=Coodinate.lineSlopeGivenTwoPoints(b,c)
y1=Coodinate.y_interceptGivenTwoPoints(a,b)
y2=Coodinate.y_interceptGivenTwoPoints(b,c)
x1=Coodinate.x_interceptGivenTwoPoints(a,b)
x2=Coodinate.x_interceptGivenTwoPoints(b,c)
# print(m1)
# print(m2)
# print(m1==m2)
# print(x1)
# print(x2)
# print(x1==x2)