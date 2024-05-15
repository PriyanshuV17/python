import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def draw_luffy():
    # Body
    glColor3f(1.0, 1.0, 0.0)  # Yellow
    glBegin(GL_QUADS)
    glVertex3f(-0.5, -1.0, 0.0)
    glVertex3f(0.5, -1.0, 0.0)
    glVertex3f(0.5, 1.0, 0.0)
    glVertex3f(-0.5, 1.0, 0.0)
    glEnd()

    # Head
    glColor3f(1.0, 0.0, 0.0)  # Red
    glBegin(GL_QUADS)
    glVertex3f(-0.2, 1.0, 0.0)
    glVertex3f(0.2, 1.0, 0.0)
    glVertex3f(0.2, 1.2, 0.0)
    glVertex3f(-0.2, 1.2, 0.0)
    glEnd()

    # Eyes
    glColor3f(0.0, 0.0, 0.0)  # Black
    glBegin(GL_QUADS)
    glVertex3f(-0.1, 1.1, 0.0)
    glVertex3f(-0.05, 1.1, 0.0)
    glVertex3f(-0.05, 1.15, 0.0)
    glVertex3f(-0.1, 1.15, 0.0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(0.05, 1.1, 0.0)
    glVertex3f(0.1, 1.1, 0.0)
    glVertex3f(0.1, 1.15, 0.0)
    glVertex3f(0.05, 1.15, 0.0)
    glEnd()

    # Mouth
    glColor3f(0.0, 0.0, 0.0)  # Black
    glBegin(GL_QUADS)
    glVertex3f(-0.15, 1.05, 0.0)
    glVertex3f(0.15, 1.05, 0.0)
    glVertex3f(0.15, 1.1, 0.0)
    glVertex3f(-0.15, 1.1, 0.0)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_luffy()
        pygame.display.flip()
        pygame.time.wait(10)

main()