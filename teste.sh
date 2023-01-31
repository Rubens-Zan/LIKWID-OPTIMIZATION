#!/bin/bash

METRICA="L3 L2CACHE FLOPS_DP"
TAMANHOS="64 100 128"

echo "performance" > /sys/devices/system/cpu/cpufreq/policy3/scaling_governor

for n in $TAMANHOS
do
    for k in $METRICA
    do
        likwid-perfctr -C 3 -g ${k} -m -O ./matmult ${n} >${k}_${n}_SemOtimiz.log
    done
done

for n in $TAMANHOS
do
    for k in $METRICA
    do
        likwid-perfctr -C 3 -g ${k} -m -O ./matmult ${n} >${n}_${k}_ComOtimiz.log
    done 
done

echo "powersave" > /sys/devices/system/cpu/cpufreq/policy3/scaling_governor 