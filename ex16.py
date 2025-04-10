nota1, nota2, nota3= float(input("insira 1º nota:")), float(input("insira 2º nota:")), float(input("insira 3º nota:"))
media= nota1 + nota2 + nota3
media_aritimetica= media/3
if media_aritimetica >= 7:
    print("aluno aprovado")
elif media_aritimetica >=5 and <=7:
    print("aluno em recuperação")
else media_aritimetica >5:
    print("aluno reprovado")
    
    
    