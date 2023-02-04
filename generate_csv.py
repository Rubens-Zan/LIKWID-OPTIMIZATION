def grep(file_path, substring):
    myLine = {'line': '', 'index':0}
    with open(file_path, 'r') as file:
        i = 0
        for line in file:
            if substring in line:
                myLine['line'] =line 
                myLine['index'] =i  
                i+=1
                yield myLine

TAMANHOS=['64','100','128','1024', '2000','2048', '3000', '4000', '5000']
# HEADER = ['MatXMat','MatxMatOtim','MatxVet','MatxVetOtim']
TYPESDICTIONARY = {
    'L3': 'L3 bandwidth [MBytes/s]', 
    'L2CACHE': 'L2 miss ratio',
    'FLOPS_DP' : 'DP MFLOP/s'
}
    # 'time':'RDTSC Runtime [s]'

def generate_csv(file_path, type, typeMetric):
    with open(file_path, 'w') as f:
                # print('Tamanho', end=" ",file=f)
                # for col in HEADER:
                #     print(",",col, end=" ",file=f)
                # print(file=f)
                for tam in TAMANHOS:
                    print(tam, end=" ",file=f)
                    for myLine in grep('log/'+type+'_'+tam+'.log', typeMetric):
                        formattedLine = myLine['line'].replace(',', ' ') 
                        words = formattedLine.split()
                        print(",",words[-1], end=" ", file=f)
                    print(file=f)
                    

for type in TYPESDICTIONARY.keys():
    generate_csv('log'+type+'.csv', type, TYPESDICTIONARY[type])
generate_csv('logTIME.csv', 'L3', 'RDTSC Runtime [s]')

# Banda de Memória: MEM ou L3
# Memory bandwidth [MBytes/s] 

# Cache miss L2: CACHE ou L2CACHE
# data cache miss ratio

# Operações aritméticas: FLOPS_DP 
# FLOPS_DP  e FLOPS_AVX 