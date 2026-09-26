
class Rectangle:
    number_of_rectangles = 0
    
    def __init__(self, width, height):
        print("Constructor called...")
        self.width = width
        self.height = height
        self.size = None
        
        Rectangle.number_of_rectangles += 1 # var = var + 1
        
        
        
r0 = Rectangle(1, 5)        
r1 = Rectangle(2, 5)
print(f"r1 - width: {r1.width}; height: {r1.height}")
print(Rectangle.number_of_rectangles)

r2 = Rectangle(1, 3)
print(f"r2: width: {r2.width}; height: {r2.height}")
print(Rectangle.number_of_rectangles)


#%%

class Point:
    x = 3
    y = 2

p1 = Point()
p2 = Point()

print(f"p1 - x: {p1.x}; y: {p1.y}")
p1.x, p1.y = 10, 2
print(f"p1 - x: {p1.x}; y: {p1.y}\n")

print(f"p2 - x: {p2.x}; y: {p2.y}") # 3,2
p2.x, p2.y = 1, 7
print(f"p2 - x: {p2.x}; y: {p2.y}") # 1,7









