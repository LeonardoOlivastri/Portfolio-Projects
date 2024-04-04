import random


class Blob:

    # i blob hanno una size tra 4 e 8, e si muovono tra -1 e 1 pixel. Questo comportamento si modifica con i moltiplicatori
    def __init__(self, color, x_boundary, y_boundary, size_multiplier=1, movement_multiplier=1):
        self.size = random.randrange(4*size_multiplier, 8*size_multiplier)
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
        self.movement_range = (-1*movement_multiplier, 1*movement_multiplier+1)

    def __repr__(self):
        return 'Blob({}, {}, ({},{}))'.format(self.color, self.size, self.x, self.y)
    
    def __str__(self):
        return f'Blob of color {self.color}, size {self.size} and location {self.x, self.y}'

    #se due blob di colore diverso si scontrano, diminuiscono di dimensione
    def __add__(self, other_blob):
        if self.color != other_blob.color:
            tmp_size = self.size
            self.size -= other_blob.size
            other_blob.size -= tmp_size

    def move(self):
        self.move_x = random.randrange(self.movement_range[0],self.movement_range[1])
        self.move_y = random.randrange(self.movement_range[0],self.movement_range[1])
        self.x += self.move_x
        self.y += self.move_y

    #funzione per evitare che i blob escano dallo schermo
    def check_bounds(self):
        if self.x < 0: self.x = 0
        elif self.x > self.x_boundary: self.x = self.x_boundary
        
        if self.y < 0: self.y = 0
        elif self.y > self.y_boundary: self.y = self.y_boundary
