#include <GL/gl.h>
#include <GL/glut.h>

void display() {
  // Clear the screen to sky blue.
  glClearColor(0.53f, 0.81f, 0.98f, 1.0f);
  glClear(GL_COLOR_BUFFER_BIT);

  // Draw the hut body (rectangle) with borders.
  glBegin(GL_QUADS);
    // Red color for left border
    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex2f(-0.4f, -0.4f);
    
    // Green color for bottom border
    glColor3f(0.0f, 1.0f, 0.0f);
    glVertex2f(0.4f, -0.4f);
    
    // Blue color for right border
    glColor3f(0.0f, 0.0f, 1.0f);
    glVertex2f(0.4f, 0.4f);

    // No border for top side
    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex2f(-0.4f, 0.4f);
  glEnd();

  // Draw borders for the rectangle with increased width.
  glLineWidth(5.0f);  // Set the line width to 5.0
  glBegin(GL_LINES);
    // Left border (red)
    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex2f(-0.4f, -0.4f);
    glVertex2f(-0.4f, 0.4f);

    // Bottom border (green)
    glColor3f(0.0f, 1.0f, 0.0f);
    glVertex2f(-0.4f, -0.4f);
    glVertex2f(0.4f, -0.4f);

    // Right border (blue)
    glColor3f(0.0f, 0.0f, 1.0f);
    glVertex2f(0.4f, -0.4f);
    glVertex2f(0.4f, 0.4f);
  glEnd();
  glLineWidth(1.0f);  // Reset the line width to 1.0

  // Draw the specified roof (triangle) with borders.
  glBegin(GL_TRIANGLES);
    // Red color for left border
    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex2f(-0.6f, 0.4f);

    // Green color for bottom border
    glColor3f(0.0f, 1.0f, 0.0f);
    glVertex2f(0.6f, 0.4f);

    // Blue color for right border
    glColor3f(0.0f, 0.0f, 1.0f);
    glVertex2f(0.0f, 0.8f);
  glEnd();

  // Swap the buffers so that the drawing is displayed on the screen.
  glutSwapBuffers();
}

int main(int argc, char** argv) {
  // Initialize GLUT.
  glutInit(&argc, argv);

  // Create a window with a single color buffer and no depth buffer.
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);  // Use double buffering for smoother animation
  glutInitWindowSize(800, 600);
  glutInitWindowPosition(100, 100);
  glutCreateWindow("OpenGL Hut with Specified Roof and Increased Border Width");

  // Set the display callback function.
  glutDisplayFunc(display);

  // Enter the GLUT main loop.
  glutMainLoop();

  return 0;
}
