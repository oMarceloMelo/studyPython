# coding: utf-8
#REQUISITOS DO SISTEMA:
#apenas permitir 3 tentativas para realizar o login OK
#permitir o usuário indicar quantos usuários deseja cadastrar OK
#dentro do cadastro indicar a posição que ele está na lista de usuários cadastrados OK
#salvar os usuários em um arquivo txt OK
#Não deixar criar o mesmo usuário que já existe, salvo no arquivo OK
#Quando pedir o login, conferir com todos os usuários do arquivo OK
#Salvar a “posição” do usuário, junto no arquivo, para quando ele logar, apresentar a posição OK
#Exibir menu com opções: LOGIN, CADASTRAR, BUSCAR USUÁRIO, SAIR

#criando variaveis
options = {0:'1: Login',1:'2: Cadastro',2:'3: BUSCAR USUÁRIO',3:'4: SAIR'}

#pegar tamanho das opções do menu
def lenOption():
	lenOption = len(options)
	return lenOption

#definindo numero de usuários para cadastro
#cadastrando em um arquivo txt
def createAccount():
	users_login = input('\n'+'Quantos usuários você deseja cadastrar?')
	while not users_login.isnumeric():
		users_login = input('\n'+'Digite um numero! quantos usuários deseja cadastrar?'+ '\n')
	users_login = int(users_login)
	i = 0
	end_while = False
	with open('/home/marcelokoper/Documentos/ref_users_saved.txt', 'r') as f:
		userid = len(f.readlines()) + 1
		f.close()
	while i < users_login:
		account_name = str(input('\n'+'Digite seu nome de usuário para cadastro: '))
		account_password = input('\n'+'Digite uma senha para cadastro: '+'\n')
		ref_users_saved = open('/home/marcelokoper/Documentos/ref_users_saved.txt', 'r')
		list_users = ref_users_saved.readlines()
		for line in list_users:
			value_line = line.split(':')
			if account_name == value_line[1]:
				print('\n'+'Usuário já existe'+'\n')
				i = i - 1
				list_user_position = value_line[0]
				end_while = True
				break
			else:
				continue
		ref_users_saved.close()
		if end_while == False:
			with open('/home/marcelokoper/Documentos/ref_users_saved.txt', 'a') as ref_users_saved:
				ref_users_saved.write(f'{userid}:{account_name}:{account_password}' + '\n')
			print('\n'+f'Você é o número {userid} da lista'+'\n')
		i = i + 1
		print('****'*10 + '\n')
		if i == users_login:
			exibirMenu()

#Entrando na conta
def login():
	login = False
	try_login = 0
	while login == False and try_login < 3:
		insert_account = input('Digite seu usuário para entrar: ')
		insert_password = input('Digite sua senha para entrar: ')
		ref_users_saved = open('/home/marcelokoper/Documentos/ref_users_saved.txt', 'r')
		list_users = ref_users_saved.readlines()
		for list_u in list_users:
			value_lines = list_u.split(':')
			value_lines[2] = value_lines[2].rstrip('\n')
			if insert_account == value_lines[1] and insert_password == value_lines[2]:
				if insert_account == 'marcelo' and insert_password == 'pikadasgalaxias':
					print('\n'+'Bem vindo ó marcelo pika das galáxias, obrigado por mais um dia sendo nosso pika das galáxias ó marcelo!! uma excelente semana para você'+'\n')
				else:
					print('\n'+f'Realizado login {insert_account}, você é o usuário {value_lines[0]}')
				login = True
				break
		else:
			print('\n'+'Usuário ou senha inválidos, por favor digite novamente :)' + '\n')
			continue
		try_login = try_login + 1
		if try_login >= 3:
			print('Máximo de tentativas realizadas (3 de 3), por favor tente mais tarde!')
			login = True
		if try_login <= 3 and login == False:
			print('Você realizou a tentativa ' + str (try_login) + ' de 3 tentativas, por favor tente novamente :)')

def findUsers():
	return True
#menu
def exibirMenu():
	iOption = 0
	while iOption < lenOption():
		print(options[iOption])
		iOption = iOption + 1
		if iOption == lenOption():
			print('\n')
			break
#perguntando opção do menu que deseja realizar e garantir que usuário digitou uma opção correta
	option_selected = input('Escolha uma opção acima com o respectivo número: ')
	while not option_selected.isnumeric() and option_selected < 1 and option_selected > 4:
		exibirMenu()
		option_selected = input('Escolha apenas uma opção disponível acima: ')
	option_selected2 = int(option_selected)
	if option_selected2 == 1:
		login()
	if option_selected2 == 2:
		createAccount()

exibirMenu()