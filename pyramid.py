import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (0, 0, 1)
)

faces = (
    (0, 1, 4),
    (1, 2, 4),
    (2, 3, 4),
    (3, 0, 4),
    (0, 1, 2, 3)
)

# Define colors for each face
face_colors = (
    (1, 0, 0),  # Red
    (0, 1, 0),  # Green
    (1, 1, 0),  # Yellow
)

def draw_pyramid():
    glBegin(GL_LINES)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    # Draw faces with different colors
    glBegin(GL_TRIANGLES)
    for i, face in enumerate(faces):
        glColor3fv(face_colors[i % len(face_colors)])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (1400, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_pyramid()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
