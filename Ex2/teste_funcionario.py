from funcionario import Funcionario

funcionario = Funcionario ('Elias', 'elias@algumacoisa.com')

funcionario.cadastro_hora('Jan',300)
funcionario.cadastro_hora('Fev', 200)
funcionario.cadastro_salario_hora('Jan', 9)
funcionario.cadastro_salario_hora('Fev', 9)
print(funcionario)
print(funcionario.calcula_salario('Jan'))
print(funcionario.calcula_salario('Fev'))