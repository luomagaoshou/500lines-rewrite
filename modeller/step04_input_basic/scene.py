from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from shapes import *
from common.trackball import Trackball


class Scene:
    def __init__(self):
        define_shapes()
        self.shapes = [Plane()]
        self.trackball = Trackball(theta=-25, distance=15)
        self.translation = [0, 0, 0, 0]

    def add_samle_shapes(self):
        cube = Cube(color_index=1)
        cube.translate(2, 0, 2)
        self.shapes.append(cube)

        sphere = Sphere(color_index=3)
        sphere.translate(-2, 0, 2)
        self.shapes.append(sphere)

        snowball = Snowball()
        snowball.translate(-2, 0, -2)
        self.shapes.append(snowball)

    def get_shapes(self, active):
        return [x for x in self.shapes if x.is_active() == active]

    def translate(self, x, y, z):
        self.translation[0] += x
        self.translation[1] += y
        self.translation[2] += z

    def render(self):
        # << init_view
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        xSize, ySize = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        aspect_ratio = float(xSize) / float(ySize)
        glViewport(0, 0, xSize, ySize)
        gluPerspective(70, aspect_ratio, 0.1, 1000.0)
        glTranslated(0, 0, -15)
        # >> init_view

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glTranslate(self.translation[0], self.translation[1], self.translation[2])
        tb_mat = self.trackball.matrix
        glMultMatrixf(tb_mat)

        glDisable(GL_LIGHTING)
        for shape in self.get_shapes(False):
            shape.render()

        glEnable(GL_LIGHTING)
        for shape in self.get_shapes(True):
            shape.render()

        glPopMatrix()
        glFlush()

    def drag(self, pos, delta):
        self.trackball.drag_to(pos[0], pos[1], delta[0], delta[1])
