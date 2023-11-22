#include <GL/gl.h>
#include <GL/glut.h>

void display() {
  // Clear the screen to black.
  glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
  glClear(GL_COLOR_BUFFER_BIT);

  // Draw the roof of the hut
  glBegin(GL_TRIANGLES);

    // Set the color of the first vertex to red.
    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex2f(-0.8f, 0.0f);

    // Set the color of the second vertex to green.
    glColor3f(0.0f, 1.0f, 0.0f);
    glVertex2f(0.8f, 0.0f);

    // Set the color of the third vertex to blue.
    glColor3f(0.0f, 0.0f, 1.0f);
    glVertex2f(0.0f, 0.8f);
  glEnd();

  // Draw the body of the hut
  glBegin(GL_QUADS);

    // Set the color of the body to match the roof.
    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex2f(-0.65f, 0.0f);
    glColor3f(0.0f, 0.0f, 1.0f);
    glVertex2f(-0.65f, -0.85f);
    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex2f(0.65f, -0.85f);
    glColor3f(0.0f, 1.0f, 0.0f);
    glVertex2f(0.65f, 0.0f);

  glEnd();

  // Draw the outline of the body
  glLineWidth(2.0f);
  glBegin(GL_LINES);

    // Left line (red)
    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex2f(-0.7f, 0.0f);
    glVertex2f(-0.7f, -0.9f);

    // Bottom line (green)
    glColor3f(0.0f, 1.0f, 0.0f);
    glVertex2f(-0.7f, -0.9f);
    glVertex2f(0.7f, -0.9f);

    // Right line (blue)
    glColor3f(0.0f, 0.0f, 1.0f);
    glVertex2f(0.7f, 0.0f);
    glVertex2f(0.7f, -0.9f);
  glEnd();

  // Swap the buffers so that the drawing is displayed on the screen.
  glutSwapBuffers();
}

int main(int argc, char** argv) {
  // Initialize GLUT.
  glutInit(&argc, argv);

  // Create a window with a single color buffer and no depth buffer.
  glutInitDisplayMode(GLUT_SINGLE);
  glutInitWindowSize(800, 800);
  glutInitWindowPosition(1000, 100);
  glutCreateWindow("MY HUT");

  // Set the display callback function.
  glutDisplayFunc(display);

  // Enter the GLUT main loop.
  glutMainLoop();

  return 0;
}