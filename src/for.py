
# percorrer range 

# for variavel in range(10):
#   print(variavel)

# Pedir nota
acc = 0;
for i in range(1, 4): 
  nota = float(input(f'informe sua nota {i}: '))
  acc += nota

if(acc / 3) >= 7 :
  print('Você passou de ano')
else :
  print('Tu ta bem lascadin')
