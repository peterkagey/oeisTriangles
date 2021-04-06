from PIL import Image, ImageDraw
import math
import random

class TriangleDrawer:
  # tabl is e.g. [[1],[2,3],[4,5,6]]
  # sequence name is e.g. A999999
  def __init__(self, tabl, sequence_name):
    self.rows = len(tabl)    # rows of triangle
    self.s = math.ceil(8192/3/self.rows) # Distance between hexagon centers
    self.r = self.s/2/0.866 # "radius" of hexagon
    self.tabl = tabl
    self.name = sequence_name

  def draw_hexagon(self, triangle_coordinate, color=100):
    (x,y) = triangle_coordinate
    coordinates = [(x + self.r*math.cos(math.radians(theta)), y + self.r*math.sin(math.radians(theta))) for theta in range(30,390,60)]
    self.dctx.polygon(coordinates, fill=color)

  def draw_triangular_image(self):
    height = math.ceil(2*self.r + 0.866 * self.s * (self.rows-1))
    width = 2*height
    top_point = (width/2, self.r)
    img = Image.new("RGBA", (width, height), (255,255,255,0))  # create new Image
    self.dctx = ImageDraw.Draw(img)  # create drawing context
    self.fill_hexagons(top_point, self.get_colors())
    del self.dctx  # destroy drawing context
    file_name = "/tmp/" + self.name + ".png"
    img.save(file_name)

  def get_colors(self):
    color1 = (random.randint(50,100),random.randint(50,100),random.randint(50,100))
    color2 = (random.randint(150,200),random.randint(150,200),random.randint(150,200))
    return (color1, color2)

  def fill_hexagons(self, top_point, colors):
    (color1, color2) = colors
    (x_t, y_t) = top_point
    for a in range(self.rows):
      for b in range(self.rows-a):
        color = colors[self.tabl[a+b][b] % 2]
        x = x_t - self.s*(a-b)/2
        y = y_t + 0.866*self.s*(a+b)
        self.draw_hexagon((x, y), color)
