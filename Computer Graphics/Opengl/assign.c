#include <GL/gl.h>
#include <GL/glut.h>

void display() {

  glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
  glClear(GL_COLOR_BUFFER_BIT);

  glBegin(GL_TRIANGLES);

    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex2f(-0.8f, 0.0f);

    glColor3f(0.0f, 1.0f, 0.0f);
    glVertex2f(0.8f, 0.0f);

    glColor3f(0.0f, 0.0f, 1.0f);
    glVertex2f(0.0f, 0.8f);
  glEnd();

  glBegin(GL_QUADS);

    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex2f(-0.65f, 0.0f);
    glColor3f(0.0f, 0.0f, 1.0f);
    glVertex2f(-0.65f, -0.85f);
    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex2f(0.65f, -0.85f);
    glColor3f(0.0f, 1.0f, 0.0f);
    glVertex2f(0.65f, 0.0f);

  glEnd();

  glLineWidth(2.0f);
  glBegin(GL_LINES);

    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex2f(-0.7f, 0.0f);
    glVertex2f(-0.7f, -0.9f);

    glColor3f(0.0f, 1.0f, 0.0f);
    glVertex2f(-0.7f, -0.9f);
    glVertex2f(0.7f, -0.9f);

    glColor3f(0.0f, 0.0f, 1.0f);
    glVertex2f(0.7f, 0.0f);
    glVertex2f(0.7f, -0.9f);
  glEnd();

  glutSwapBuffers();
}

int main(int argc, char** argv) {
  glutInit(&argc, argv);

  glutInitDisplayMode(GLUT_SINGLE);
  glutInitWindowSize(800, 800);
  glutInitWindowPosition(1000, 100);
  glutCreateWindow("MY HUT MULTICOLORED");
  glutDisplayFunc(display);

  glutMainLoop();

  return 0;
}