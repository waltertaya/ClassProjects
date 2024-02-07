#include <stdio.h>
#include <math.h>

int main() {
    int ax = -3;
    int ay = 2;
    int bx = 10;
    int by = 8;
    double m = (double)(by - ay) / (bx - ax);
    double y = ay;
    int iy;

    for (int x = ax; x <= bx; x++) {
        iy = y;
        printf("%d %d\n", x, iy);
        y += m;
    }

    return 0;
}

