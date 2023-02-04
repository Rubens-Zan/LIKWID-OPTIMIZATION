#!/bin/bash
#TAMANHOS="3000"
TAMANHOS="64 100 128 1000"

TESTES="L3 L2CACHE FLOPS_DP"
TAM2="1 2 3 4"
CORE_ID=3

rm RUNTIME_*.txt &>/dev/null

echo "performance" > /sys/devices/system/cpu/cpufreq/policy3/scaling_governor

for teste in $TESTES; do
    rm "$teste"_*.txt &>/dev/null
   
    for tam in $TAMANHOS; do
        ./perfctr $CORE_ID $teste ./matmult -n $tam > tmp.txt
        if [ "$teste" = "L3" ]; then
            cat tmp.txt | grep "L3 bandwidth" | cut -d'|' -f3 >> "$teste"_"$tam".txt
            cat tmp.txt | grep "Runtime (RDTSC)" | cut -d'|' -f3 >> RUNTIME_"$tam".txt
            i=$((0))
            while read line; do
                if (( $i % 4 == 0 )); then
                    echo -n "$tam | $line" >> RUNTIME_multMatRowVet.txt                
                elif (( $i % 4 == 1 )); then
                    echo " | $line" >> RUNTIME_multMatRowVet.txt
                elif (( $i % 4 == 2 )); then
                    echo -n "$tam | $line" >> RUNTIME_multMatMatRow.txt
                elif (( $i % 4 == 3 )); then
                    echo " | $line" >> RUNTIME_multMatMatRow.txt
                fi
                i=$((i+1))
            done < RUNTIME_"$tam".txt
            rm RUNTIME_"$tam".txt

        elif [ "$teste" = "L2CACHE" ]; then
            cat tmp.txt | grep "miss ratio" | cut -d'|' -f3 >> "$teste"_"$tam".txt
        elif [ "$teste" = "FLOPS_DP" ]; then
            cat tmp.txt | grep "DP " | cut -d'|' -f3 >> "$teste"_"$tam"_dp.txt            
            cat tmp.txt | grep "AVX " | cut -d'|' -f3 >> "$teste"_"$tam"_avx.txt
            # retira linha por linha dos arquivos dp e avx
            for i in $TAM2; do
                DP=$(head -1 "$teste"_"$tam"_dp.txt)
                AVX=$(head -1 "$teste"_"$tam"_avx.txt)
                echo "$DP | $AVX" >> "$teste"_"$tam".txt
                sed -i '1d' "$teste"_"$tam"_dp.txt
                sed -i '1d' "$teste"_"$tam"_avx.txt
            done
            rm "$teste"_"$tam"_dp.txt "$teste"_"$tam"_avx.txt
        fi
        i=$((0))
        while read line; do
            if (( $i % 4 == 0 )); then
                echo -n "$tam | $line" >> "$teste"_multMatRowVet.txt                
            elif (( $i % 4 == 1 )); then
                echo " | $line" >> "$teste"_multMatRowVet.txt
            elif (( $i % 4 == 2 )); then
                echo -n "$tam | $line" >> "$teste"_multMatMatRow.txt
            elif (( $i % 4 == 3 )); then
                echo " | $line" >> "$teste"_multMatMatRow.txt
            fi
            i=$((i+1))
        done < "$teste"_"$tam".txt
        
        rm "$teste"_"$tam".txt
        rm tmp.txt
    done
done

echo "powersave" > /sys/devices/system/cpu/cpufreq/policy3/scaling_governor 
