
line = input('Alguna vez conte el cuento de la Buena Pipa? ')
while True:
    print("No te dije -" , line, "-")
    line = input('Te dije: "Alguna vez conte el cuento de la Buena Pipa?" ')
    if line == 'magia':
        break
    
print('Me parecio haberlo contado!')
