class Coodinate (object):
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    
    def distance(self,other):
        x_diff_sq=(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        z_diff_sq=(self.z-other.z)**2
        return (x_diff_sq + y_diff_sq +z_diff_sq)**0.5
    
    def midpoint(self,other):
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
        x_diff_abs=abs(self.x - other.x)
        y_diff_abs=abs(self.y - other.y)
        z_diff_abs=abs(self.z - other.z)
        return(x_diff_abs + y_diff_abs + z_diff_abs)
