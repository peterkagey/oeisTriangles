from triangle_drawer import TriangleDrawer

class SequenceDrawer:
  def __init__(self, integer_sequence, name):
    self.tabl = self.to_tabl(integer_sequence)
    self.name = name

  def to_tabl(self, integer_sequence):
    cursor = 0
    row_length = 1
    table = []
    while len(integer_sequence) >= cursor + row_length:
      table.append(integer_sequence[cursor:cursor+row_length])
      cursor += row_length
      row_length += 1
    return table

  def draw(self):
    TriangleDrawer(self.tabl, self.name).draw_triangular_image()
