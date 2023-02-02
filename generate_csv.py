def grep(file_path, substring):
    with open(file_path, 'r') as file:
        for line in file:
            if substring in line:
                yield line


# print('Tamanho', end=" ")
# collumnNames = ['Teste de tempo s otim','Teste de tempo c otim','Banda de Memoria s otim','Banda de Memoria c otim','Cache miss L2 s otim','Cache miss L2 c otim','Operações aritméticas s otim','Operações aritméticas c otim']
TAMANHOS=[64,100,128]
COLLUMNAMES = ['Tamanho', 'MatXMat','MatxMatOtim','MatxVet','MatxVetOtim']

for col in COLLUMNAMES:
    print(",",col, end=" ")
print()

for line in grep('log/L3_100_SemOtimiz.log', 'L3 bandwidth [MBytes/s]'):
    formattedLine =line.replace(',', ' ') 
    words = formattedLine.split()
    print(words[-1], end=", ")

for line in grep('log/100_L2CACHE_ComOtimiz.log', 'L2 miss ratio'):
    formattedLine =line.replace(',', ' ') 
    words = formattedLine.split()
    print(words[-1],end=", ")

# for line in grep('log/FLOPS_DP_100_SemOtimiz.log', 'DP MFLOP/s'):
#     formattedLine =line.replace(',', ' ') 
#     words = formattedLine.split()
#     print(words[-1],end=", ")
# print()


# Banda de Memória: MEM ou L3
# Memory bandwidth [MBytes/s] 

# Cache miss L2: CACHE ou L2CACHE
# data cache miss ratio

# Operações aritméticas: FLOPS_DP 
# FLOPS_DP  e FLOPS_AVX 