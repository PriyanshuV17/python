import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

tex_coords = (
    (0, 0),
    (1, 0),
    (1, 1),
    (0, 1)
)

def generate_checkerboard_texture():
    width = 256
    height = 256
    texture = np.zeros((width, height, 3), dtype=np.uint8)
    for i in range(width):
        for j in range(height):
            color = 255 if ((i // 32) + (j // 32)) % 2 == 0 else 0
            texture[i, j] = [color, color, color]
    return texture

def load_texture(texture_data):
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, texture_data.shape[1], texture_data.shape[0], 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
    return texture

def draw_cube(texture):
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    for i, edge in enumerate(edges):
        glTexCoord2fv(tex_coords[0])
        glVertex3fv(vertices[edge[0]])
        glTexCoord2fv(tex_coords[1])
        glVertex3fv(vertices[edge[1]])
        glTexCoord2fv(tex_coords[2])
        glVertex3fv(vertices[(edge[1] + 1) % 4])
        glTexCoord2fv(tex_coords[3])
        glVertex3fv(vertices[(edge[0] + 1) % 4])
    glEnd()

def main():
    pygame.init()
    display = (1200, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    texture_data = generate_checkerboard_texture()
    texture = load_texture(texture_data)

    glEnable(GL_TEXTURE_2D)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube(texture)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
