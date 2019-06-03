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
options = {0:'1: Login',1:'2: Cadastro',2:'3: Buscar usuário',3:'4: Sair'}
optionsLogin = {0:'1: Cadastrar um novo usuário',1:'2: Buscar usuários',2:'3: Deletar usuário'}
optionEnd = {0:'1: Continuar?',1:'2: Voltar ao menu'}

#pegar tamanho das opções do menu
def lenOption():
	lenOption = len(options)
	return lenOption

#pegar tamanho das opções ao buscar usuário
def lenOptionEnd():
	lenOptionEnd = len(optionEnd)
	return lenOptionEnd

#pegar tamanho das opções pós login
def lenOptionLogin():
	lenOptionLogin = len(optionsLogin)
	return lenOptionLogin

#exibindo opções para parar uma ação
def optionsEnd():
	iOptionEnd = 0
	print('\n')
	while iOptionEnd < lenOptionEnd():
		print(optionEnd[iOptionEnd])
		iOptionEnd = iOptionEnd + 1
		if iOptionEnd == lenOptionEnd():
			print('\n')
			break

#exibindo opções pós login
def optionsLoginSee():
	iOptionLogin = 0
	print('\n')
	while iOptionLogin < lenOptionLogin():
		print(optionsLogin[iOptionLogin])
		iOptionLogin = iOptionLogin + 1
		if iOptionLogin == lenOptionLogin():
			print('\n')
			break

def optionSelectLogin():
	optionsLoginSee()
	option_selected = input('Escolha apenas uma opção acima: ')
	while not option_selected.isnumeric() and option_selected < 1 and option_selected > 3:
		optionsLoginSee()
		option_selected = input('Escolha apenas uma opção acima: ')
	option_selected2 = int(option_selected)
	if option_selected2 == 1:
		createAccount()
	if option_selected2 == 2:
		findUsers()
	if option_selected2 == 3:
		deleteUsers()
	if option_selected2 < 1 or option_selected2 > 3:
		print('\n'+'Opção inválida mô quiridu'+'\n')
		optionSelectLogin()

#perguntando se deseja parar a opção selecionada
def optionSelectEnd():
	optionsEnd()
	option_selected = input('Escolha apenas uma opção disponível acima: ')
	while not option_selected.isnumeric() and option_selected < 1 and option_selected > 2:
		optionsEnd()
		option_selected = input('Escolha apenas uma opção disponível acima: ')
	option_selected2 = int(option_selected)
	if option_selected2 == 2:
		exibirMenu()
	else:
		pass


#definindo numero de usuários para cadastro
#cadastrando em um arquivo txt
def createAccount():
	users_login = input('\n'+'Quantos usuários você deseja cadastrar?')
	while not users_login.isnumeric():
		users_login = input('\n'+'Digite um numero! quantos usuários deseja cadastrar?'+ '\n')
	users_login = int(users_login)
	i = 0
	end_while = False
	with open('/home/marcelo/Documentos/programas/studyPython/ref_users_saved.txt', 'r') as f:
		userid = len(f.readlines()) + 1
		f.close()
	while i < users_login:
		account_name = str(input('\n'+'Digite seu nome de usuário para cadastro: '))
		account_password = input('\n'+'Digite uma senha para cadastro: '+'\n')
		ref_users_saved = open('/home/marcelo/Documentos/programas/studyPython/ref_users_saved.txt', 'r')
		list_users = ref_users_saved.readlines()
		for line in list_users:
			value_line = line.split(':')
			if account_name == value_line[1]:
				print('\n'+'Usuário já existe'+'\n')
				i = i - 1
				list_user_position = value_line[0]
				end_while = True
				optionSelectEnd()
				break
			else:
				continue
		ref_users_saved.close()
		if end_while == False:
			with open('/home/marcelo/Documentos/programas/studyPython/ref_users_saved.txt', 'a') as ref_users_saved:
				ref_users_saved.write(f'{userid}:{account_name}:{account_password}' + '\n')
			print('\n'+f'Você é o número {userid} da lista'+'\n')
			if i < users_login:
				optionSelectEnd()
		i = i + 1
		print('****'*10 + '\n')
		if i == users_login:
			exibirMenu()
	return account_name, account_password

#Entrando na conta
def login():
	login = False
	try_login = 0
	while login == False and try_login < 3:
		insert_account = input('\n'+'Digite seu usuário para entrar: ')
		insert_password = input('Digite sua senha para entrar: ')
		ref_users_saved = open('/home/marcelo/Documentos/programas/studyPython/ref_users_saved.txt', 'r')
		list_users = ref_users_saved.readlines()
		for list_u in list_users:
			value_lines = list_u.split(':')
			value_lines[2] = value_lines[2].rstrip('\n')
			if insert_account == value_lines[1] and insert_password == value_lines[2]:
				if insert_account == 'marcelo' and insert_password == 'pikadasgalaxias':
					print('\n'+'Bem vindo ó marcelo pika das galáxias, obrigado por mais um dia sendo nosso pika das galáxias ó marcelo!! uma excelente semana para você'+'\n')
					login = True
					optionSelectLogin()
				else:
					print('\n'+f'Realizado login {insert_account}, você é o usuário {value_lines[0]}')
					login = True
					optionSelectLogin()
				break
			else:
				print('\n'+'Usuário ou senha inválidos, por favor digite novamente :)' + '\n')
				break
		try_login = try_login + 1
		if try_login >= 3:
			print('Máximo de tentativas realizadas (3 de 3), por favor tente mais tarde!')
			login = True
		if try_login <= 3 and login == False:
			print('Login inválido')
			optionSelectEnd()

#Buscar usuários
def findUsers():
	find = False
	askAction = 0
	while find == False:
		insert_account = input('Digite o usuário: ')
		ref_users_saved = open('/home/marcelo/Documentos/programas/studyPython/ref_users_saved.txt', 'r')
		list_users = ref_users_saved.readlines()
		for list_u in list_users:
			value_lines = list_u.split(':')
			if insert_account == value_lines[1]:
				if insert_account == 'marcelo':
					print('\n'+'*'*20)
					print('\n'+'Você descobriu o marcelo pika das galáxias, easter egg encontrado!!'+'\n')
					print('*'*20+'\n')
					optionSelectEnd()
				else:
					print('\n'+f'Usuário {insert_account} encontrado com sucesso, você é o usuário {value_lines[0]}')
					find = True
					optionSelectEnd()
				break
		else:
			print('\n'+'Usuário inválido')
			optionSelectEnd()
			continue

#deletar usuário
def deleteUsers():
	insert_account = input('\n'+'Digite o usuário para deletar: ')
	ref_users_saved = open('/home/marcelo/Documentos/programas/studyPython/ref_users_saved.txt', 'r')
	list_users = ref_users_saved.readlines()
	for list_u in list_users:
		value_lines = list_u.split(':')
		if insert_account == value_lines[1]:
			if insert_account == 'marcelo':
				print('\n'+'Você não pode excluir o marcelo pika das galáxias'+'\n')
				optionSelectLogin()
			else:
				print('\n'+f'Deletando usuário {insert_account}')
				value_lines[1]
				optionSelectLogin()
			break
		else:
			print('\n'+'Usuário inválido, por favor digite novamente :)' + '\n')
			optionSelectLogin()
			continue

#menu
def exibirMenu():
	iOption = 0
	print('\n')
	while iOption < lenOption():
		print(options[iOption])
		iOption = iOption + 1
		if iOption == lenOption():
			print('\n')
			break
	optionSelectMenu()

#perguntando opção do menu que deseja realizar e garantir que usuário digitou uma opção correta
def optionSelectMenu():
	option_selected = input('Escolha uma opção acima com o respectivo número: ')
	while not option_selected.isnumeric():
		exibirMenu()
		option_selected = input('Escolha apenas uma opção disponível acima: ')
	option_selected2 = int(option_selected)
	if option_selected2 == 1:
		login()
	if option_selected2 == 2:
		createAccount()
	if option_selected2 == 3:
		findUsers()
	if option_selected2 == 4:
		print('\n'+'Saindo...'+'\n')
	if option_selected2 < 1 or option_selected2 > 4:
		print('\n'+'opção inválida mô quiridu'+'\n')
		exibirMenu()

exibirMenu()