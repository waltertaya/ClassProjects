#include <stdio.h>
#include <GL/glut.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    glBegin(GL_LINES);

    glVertex2i(180, 15);
    glVertex2i(10, 145);

    glEnd();

    glFlush();
}

void init () {
    glClearColor(0.0, 0.0, 0.0, 0.0);
    glMatrixMode(GL_PROJECTION);

    gluOrtho2D(0.0, 200.0, 0.0, 150.0);
}

int main(int argc, char** argv) {
    // glutInit(&argc, argv);
    glutCreateWindow("OpenGL Line Example");
    glutDisplayFunc(display);
    glutMainLoop();

    return 0;
}
