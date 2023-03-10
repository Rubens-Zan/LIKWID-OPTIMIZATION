#include <stdio.h>
#include <stdlib.h>    /* exit, malloc, calloc, etc. */
#include <string.h>
#include <getopt.h>    /* getopt */
#include <time.h>
#include <likwid.h>
#include "matriz.h"

/**
 * Exibe mensagem de erro indicando forma de uso do programa e termina
 * o programa.
 */

static void usage(char *progname)
{
  fprintf(stderr, "Forma de uso: %s [ -n <ordem> ] \n", progname);
  exit(1);
}



/**
 * Programa principal
 * Forma de uso: matmult [ -n <ordem> ]
 * -n <ordem>: ordem da matriz quadrada e dos vetores
 *
 */

int main (int argc, char *argv[]) 
{
  LIKWID_MARKER_INIT;

  int c, n=DEF_SIZE;
  
  MatRow mRow_1, mRow_2, resMat;
  Vetor vet, res;
  
  /* =============== TRATAMENTO DE LINHA DE COMANDO =============== */

  char *opts = "n:";
  c = getopt (argc, argv, opts);
  
  while ( c != -1 ) {
    switch (c) {
    case 'n':  n = atoi(optarg);              break;
    default:   usage(argv[0]);
    }
      
    c = getopt (argc, argv, opts);
  }
  
  /* ================ FIM DO TRATAMENTO DE LINHA DE COMANDO ========= */
 
  // srand(time(NULL));
  srandom(20212);
      
  res = (real_t *) calloc (n, sizeof(real_t));
  resMat = geraMatRow(n, n, 1);
    
  mRow_1 = geraMatRow (n, n, 0);
  mRow_2 = geraMatRow (n, n, 0);

  vet = geraVetor (n, 0);

#ifdef DEBUG
    prnMat (mRow_1, n, n);
    prnMat (mRow_2, n, n);
    prnVetor (vet, n);
    printf ("=================================\n\n");
#endif /* DEBUG */
  LIKWID_MARKER_START ("multMatVet_NAO_OTIM");
  multMatVet (mRow_1, vet, n, n, res);
  LIKWID_MARKER_STOP ("multMatVet_NAO_OTIM");

  LIKWID_MARKER_START ("multMatVet_COM_OTIM");
  multMatVetOtim(mRow_1, vet, n, n, res);
  LIKWID_MARKER_STOP ("multMatVet_COM_OTIM");

  LIKWID_MARKER_START ("multMatMat_NAO_OTIM");
  multMatMat (mRow_1, mRow_2, n, resMat);
  LIKWID_MARKER_STOP ("multMatMat_NAO_OTIM");
  
  LIKWID_MARKER_START ("multMatMat_COM_OTIM");
  multMatMat (mRow_1, mRow_2, n, resMat);
  LIKWID_MARKER_STOP ("multMatMat_COM_OTIM");
    
#ifdef DEBUG
    prnVetor (res, n);
    prnMat (resMat, n, n);
#endif /* DEBUG */

  liberaVetor ((void*) mRow_1);
  liberaVetor ((void*) mRow_2);
  liberaVetor ((void*) resMat);
  liberaVetor ((void*) vet);
  liberaVetor ((void*) res);
  LIKWID_MARKER_CLOSE;

  return 0;
}

