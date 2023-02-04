def grep(file_path, substring):
    with open(file_path, 'r') as file:
        for line in file:
            if substring in line:
                yield line

TAMANHOS=['64','100','128']
HEADER = ['MatXMat','MatxMatOtim','MatxVet','MatxVetOtim']
TYPESDICTIONARY = {
    'L3': 'L3 bandwidth [MBytes/s]', 
    'L2CACHE': 'L2 miss ratio',
    'FLOPS_DP' : 'DP MFLOP/s' 
}

def generate_csv(file_path, type, typeMetric):
    with open(file_path, 'w') as f:
                print('Tamanho', end=" ",file=f)
                for col in HEADER:
                    print(",",col, end=" ",file=f)
                print(file=f)
                for tam in TAMANHOS:
                    print(tam, end=" ",file=f)
                    for line in grep('log/'+type+'_'+tam+'.log', typeMetric):
                        formattedLine =line.replace(',', ' ') 
                        words = formattedLine.split()
                        print(",",words[-1], end=" ", file=f)
                    print(file=f)

for type in TYPESDICTIONARY.keys():
    generate_csv('log'+type+'.csv', type, TYPESDICTIONARY[type])
# Banda de Memória: MEM ou L3
# Memory bandwidth [MBytes/s] 

# Cache miss L2: CACHE ou L2CACHE
# data cache miss ratio

# Operações aritméticas: FLOPS_DP 
# FLOPS_DP  e FLOPS_AVX 