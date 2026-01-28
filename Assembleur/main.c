#include <parm.h>

volatile int RESULT = 0;

void run(void) {
  BEGIN();

  /* On force de la mémoire (LDR/STR) avec volatile */
  volatile int z = 0;

  int a = 3, b = 4;
  int c = 0, d = 0, e = 10;
  int x = 0x12;   /* 18 */
  int y = 0x34;   /* 52 */

  /* ---- Arithmétique simple (ADD/SUB) */
  c = a + b;      /* 7 */
  d = b - a;      /* 1 */
  e = e + c;      /* 17 */
  e = e - d;      /* 16 */

  /* ---- Décalages (LSL/LSR/ASR) */
  z = x << 2;         /* 72 */
  z = z >> 1;         /* 36 */
  z = (int)(z >> 1);  /* 18 */

  /* ---- Logique (AND/ORR/EOR/BIC) */
  x = x & 0x0F;     /* 2 */
  y = y | 0x80;     /* 180 */
  z = x ^ y;        /* 182 */
  z = z & ~0x03;    /* 180 */

  /* ---- CMP + branches conditionnelles */
  if (a == 3) {
    z = z + 1;      /* +1 */
  } else {
    z = z + 2;
  }

  if (b != 0) {
    z = z + 3;      /* +3 */
  }

  if (c >= d) {
    z = z + 4;      /* +4 */
  } else {
    z = z + 5;
  }
  /* Après ce bloc, z = 188 */

  /* ---- Arithmétique étendue sans conditions */
  z = z + 1;
  z = z + 3;
  z = z + 4;
  z = z + 2;
  /* z = 198 */

  /* ---- Simulation de boucle (déroulée manuellement) */
  z = z + 0;
  z = z + 1;
  z = z + 2;
  z = z + 3;
  z = z + 4;
  z = z + 5;
  z = z + 6;
  z = z + 7;
  /* +28 => z = 226 */

  /* ---- XOR “décrémentation” (suite fixe) */
  z = z ^ 5;
  z = z ^ 4;
  z = z ^ 3;
  z = z ^ 2;
  z = z ^ 1;
  /* z = 227 */

  /* ---- Boucle (CMP + branches) */
  volatile int i = 0;
  while (i < 8) {
    z = z + i;      /* ajoute 0..7 => +28 */
    i = i + 1;
  }
  /* z = 255 */

  /* ---- Boucle (SUBS / BNE typiquement) */
  volatile int n = 5;
  while (n != 0) {
    z = z ^ n;
    n = n - 1;
  }
  /* z = 254 */

  /* ---- Accès mémoire (LDR / STR) */
  volatile int p = z;     /* force store */
  volatile int q = p + 7; /* force load + add + store */
  z = q;                  /* force load */

  /* ---- Décalage + arithmétique finale */
  z = z << 1;   /* *2 */
  z = z + 9;
  z = z - 9;

  /* Stocke le résultat final en global volatile */
  RESULT = z;
  END();
  /* z = 522 */
}
