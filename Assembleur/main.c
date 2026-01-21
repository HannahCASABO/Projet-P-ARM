#include <parm.h>

void run() {
  BEGIN();

  volatile int z = 0;

  int a = 3, b = 4, c, d, e = 10;
  int x = 0x12, y = 0x34;

  c = a + b;
  d = b - a;
  e = e + c;
  e = e - d;

  z = x << 2;
  z = z >> 1;
  z = (int)(z >> 1);

  x = x & 0x0F;
  y = y | 0x80;
  z = x ^ y;
  z = z & ~0x03;

  z = z + 1;
  z = z + 3;
  z = z + 4;
  z = z + 2;

  z = z + 0;
  z = z + 1;
  z = z + 2;
  z = z + 3;
  z = z + 4;
  z = z + 5;
  z = z + 6;
  z = z + 7;

  z = z ^ 5;
  z = z ^ 4;
  z = z ^ 3;
  z = z ^ 2;
  z = z ^ 1;

  int p = z;
  int q = p + 7;
  z = q;

  z = z << 1;
  z = z + 9;
  z = z - 9;

  END();
}
