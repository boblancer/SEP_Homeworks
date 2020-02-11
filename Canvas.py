from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import math
import random
from PySide2.QtMultimedia import QSound

class Particle():
    def __init__(self, x, y, r, c):
        self.originX = x
        self.originY = y
        self.x = x
        self.y = y
        self.r = r
        self.direction = 1 # postive or negative direction
        self.distance = [random.uniform(50, 120), random.uniform(50, 100)]
        self.radians = random.uniform(0, math.pi * 2)
        self.color = c
        self.total_rewind = 1
        self.rewind = 1
        self.rewinding = False
    def set_rewind(self, n):
        self.total_rewind = n
        self.rewinding = True

    def update(self):
        if self.rewinding:
            self.rewind += 3
            rewind_val = self.rewind/self.total_rewind
            if self.rewind >= self.total_rewind:
                self.rewinding = False
        else:
            self.rewind = 1
            rewind_val = 1

        self.radians += 0.06 * self.direction * rewind_val
        self.x = self.originX + (math.cos(self.radians) * self.distance[1] )
        self.y = self.originY + (math.sin(self.radians) * 100 )

class Canvas(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Draw circles')
        timer = QTimer(self)
        timer.setInterval(15) # interval in ms
        self.connect(timer, SIGNAL("timeout()"), self.animate)
        timer.start()
        self.direction = 1
        self.particles = []
        self.colors = [QColor(0,189,255), QColor(77,57,206), QColor(8,142,255)]

        for i in range(60):
            self.particles.append(Particle(150,150, 3, self.colors[random.randint(0,2)]))
        self.rewinding = False

    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        # optional
        paint.setRenderHint(QPainter.Antialiasing)
        # make a white drawing background
        paint.setBrush(QColor(0, 0, 0, 127))
        # paint.drawRect(event.rect())
        # for circle make the ellipse radii match
        # draw red circles

        for particle in self.particles:
            if self.rewinding:
                particle.set_rewind(400)
            particle.direction = self.direction
            particle.update()
            paint.setPen(particle.color)
            paint.setBrush(particle.color)
            particle.color
            paint.drawEllipse(QPoint(particle.x, particle.y), particle.r, particle.r)
        paint.end()
        self.rewinding = False
    def reverse_direction(self):
        self.direction = self.direction * -1
        self.rewinding = True
        QSound.play("rewind.wav")


    def animate(self):
        self.repaint()

