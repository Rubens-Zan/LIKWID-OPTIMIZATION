#!/bin/bash

METRICA="L3 L2CACHE FLOPS_DP"
TAMANHOS="64 100 128 1024 2000 2048 3000 4000 5000"

echo "performance" > /sys/devices/system/cpu/cpufreq/policy3/scaling_governor

for n in $TAMANHOS
do
    for k in $METRICA
    do
        likwid-perfctr -C 3 -g ${k} -m -O ./matmult ${n} >${k}_${n}.log
    done
done

echo "powersave" > /sys/devices/system/cpu/cpufreq/policy3/scaling_governor 
