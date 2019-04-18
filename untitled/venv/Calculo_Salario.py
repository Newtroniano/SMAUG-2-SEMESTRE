horas_trababalhadas = int(input("Digite quantas horas você trabalhou esse mês?"))
valor_hora = int(input("Digite o valor recebido por hora?"))
percentual_desconto = int(input("Digite o percentual de desconto?"))

salario_brut = (horas_trababalhadas * valor_hora)

desconto =  ((percentual_desconto * salario_brut)/100)

salario_liq = (salario_brut - desconto)

print ("Salário Bruto:",salario_brut)

print ("Desconto:",desconto)

print ("Salário Líquido:",salario_liq)