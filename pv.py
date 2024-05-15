import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def render_text(text, position, size=1):
    glPushMatrix()
    glTranslatef(position[0], position[1], position[2])
    glScalef(size, size, size)
    for char in text:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(char))
    glPopMatrix()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)  # Camera position
    glColor3f(1.0, 1.0, 1.0)
    
    # Drawing "PRIYANSHU VERMA"
    render_text("PRIYANSHU VERMA", (-3, 0, 0), size=0.1)

    pygame.display.flip()
    pygame.time.wait(10)

def main():
    pygame.init()
    global display
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(display[0], display[1])
    glutCreateWindow("3D Text Rendering")

    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()

if __name__ == "__main__":
    main()
