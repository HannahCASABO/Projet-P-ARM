#include <parm.h>

void run() {
  BEGIN();

  volatile int a = 3;
  volatile int b = 4;
  volatile int c = 0;
  volatile int d = 0;
  volatile int e = 10;

  volatile int x = 0x12;
  volatile int y = 0x34;
  volatile int z = 0;

  // ---- Arithmétique simple (ADD/SUB)
  c = a + b;
  d = b - a;
  e = e + c;
  e = e - d;

  // ---- Décalages (LSL/LSR/ASR)
  z = x << 2;
  z = z >> 1;
  z = (int)(z >> 1);   // force un LSR (shift logique) côté compilateur

  // ---- Logique (AND/ORR/EOR/BIC)
  x = x & 0x0F;
  y = y | 0x80;
  z = x ^ y;
  z = z & ~0x03;

  // ---- Comparaisons (CMP) + branches conditionnelles
  if (a == 3) {
    z = z + 1;
  } else {
    z = z + 2;
  }

  if (b != 0) {
    z = z + 3;
  }

  if (c >= d) {
    z = z + 4;
  } else {
    z = z + 5;
  }

  // ---- Boucle (B, CMP, branches) + incréments
  volatile int i = 0;
  while (i < 8) {
    z = z + i;
    i = i + 1;
  }

  // ---- Une autre boucle (SUBS, BNE)
  volatile int n = 5;
  while (n != 0) {
    z = z ^ n;
    n = n - 1;
  }

  // ---- Accès pile (LDR/STR) : force des loads/stores
  volatile int p = z;
  volatile int q = p + 7;
  z = q;

  if ((z & 1) == 0) {
    z = z + 9;
  } else {
    z = z - 9;
  }

  END();
}
