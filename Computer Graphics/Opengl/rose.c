#include <GL/glut.h>
#include <math.h>

// Define the number of petals in the rose
#define NUM_PETALS 50

// Define the radius of the rose
#define ROSE_RADIUS 1.0

// Define the height of the rose
#define ROSE_HEIGHT 0.5

// Define the color of the rose
#define ROSE_COLOR 1.0, 0.0, 0.0

// Define a function to draw a single petal of the rose
void drawPetal(float angle) {

  // Calculate the position of the petal
  float x = ROSE_RADIUS * cos(angle);
  float y = ROSE_HEIGHT * sin(angle);

  // Start drawing the petal
  glBegin(GL_POLYGON);

  // Set the color of the petal
  glColor3f(ROSE_COLOR);

  // Draw the vertices of the petal
  glVertex3f(x, y, 0.0);
  glVertex3f(x + ROSE_RADIUS / 2.0, y + ROSE_HEIGHT / 2.0, 0.0);
  glVertex3f(x, y + ROSE_HEIGHT, 0.0);

  // End drawing the petal
  glEnd();
}

// Define a function to draw the entire rose
void drawRose() {

  // Draw each petal of the rose
  for (int i = 0; i < NUM_PETALS; i++) {
    drawPetal(2.0 * 3.14 * i / NUM_PETALS);
  }
}

// Display callback function
void display() {

  // Clear the screen
  glClear(GL_COLOR_BUFFER_BIT);

  // Draw the rose
  drawRose();

  // Swap buffers
  glutSwapBuffers();
}

// Reshape callback function
void reshape(int width, int height) {

  // Set the viewport
  glViewport(0, 0, width, height);

  // Set the projection matrix
  glMatrixMode(GL_PROJECTION);
  glLoadIdentity();
  glOrtho(-ROSE_RADIUS * 1.5, ROSE_RADIUS * 1.5, -ROSE_HEIGHT * 1.5, ROSE_HEIGHT * 1.5, -10.0, 10.0);

  // Set the modelview matrix
  glMatrixMode(GL_MODELVIEW);
  glLoadIdentity();
}

// Main function
int main(int argc, char** argv) {

  // Initialize GLUT
  glutInit(&argc, argv);

  // Create a window
  glutCreateWindow("Rose");

  // Set the display callback function
  glutDisplayFunc(display);

  // Set the reshape callback function
  glutReshapeFunc(reshape);

  // Enter the main loop
  glutMainLoop();

  return 0;
}