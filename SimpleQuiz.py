
import json
import random
import operator


dictScore = {}
dictQuestoes = {}

#função para cadastrar o jogador e a sua pontuação no arquivo.
def cadastrar():
    with open("Score.txt") as f:
        data = f.read()
        j = json.loads(data)
        dictScore = j  
    nome = input('        Digite o seu Nome: ')
    print('        ------------------------------------------')
    pontuacao = 0
    dictScore[nome] = pontuacao
    with open("Score.txt", "w") as fw:
            fw.write(json.dumps(dictScore))
            fw.close
    return nome
#Função para procurar uma questão especifica atraves do seu numero.
def buscaQuestoes():
    with open("Questoes.txt") as f:
        data = f.read()
    j = json.loads(data)
    dictQuestoes = j
    numeroQuestao = (input('        Digite o numero da questão que deseja buscar: '))
    print('        ------------------------------------------')
    #Verificar se a questão está no dicionario e printar questão e resposta.
    if numeroQuestao in dictQuestoes:
            x = numeroQuestao
            print(x+')'+str(dictQuestoes[x][0])+'?'+'  Nivel de Dificudade:'+str(dictQuestoes[x][6]))
            print()
            y = 1
            while y <=4:
                print(dictQuestoes[x][y])
                y+=1
            
            print('Resposta: '+str(dictQuestoes[x][5]))
    else:
        print('        A pergunta não está no banco de dados!')
        print('        ------------------------------------------')
#Função para deletar pergunta especifica do arquivo.
def removerQuestoes():
    with open("Questoes.txt") as f:
        data = f.read()
    j = json.loads(data)
    dictQuestoes = j
    numeroQuestao = (input('        Digite o numero da questão que deseja remover: '))
    print('        ------------------------------------------')
    #Verificar se a questão já existe no dicionario de questoes.
    if numeroQuestao in dictQuestoes:
        #Apagar questão do dicionario com .pop e atualizar arquivo.
        dictQuestoes.pop(numeroQuestao)
        with open("Questoes.txt", "w") as fa:
            fa.write(json.dumps(dictQuestoes))
            fa.close
        print('        Pergunta removida com sucesso!')
        print('        ------------------------------------------')
    #caso a questão não esteja no banco de dados perguntar se deseja cadastrar uma nova.
    else:
         print('        ------------------------------------------')
         print('        Questão não está cadastrada, deseja cadastrar uma nova questão digite "S" para sim e "N" para não: ')
         r = input().upper()
         if r == 'S':
            cadastrarQuestoes()
         elif r == 'N':
            print('')
            return
def carregaQuestoes(nome):
    with open("Questoes.txt") as f:
        data = f.read()
    j = json.loads(data)
    dictQuestoes = j
    with open("Score.txt") as fr:
        data = fr.read()
        ja = json.loads(data)
        dictScore = (ja)
    fa = open("Score.txt", "a")
    k= 1
    l = len(dictQuestoes)
    for x in dictQuestoes:
        y= 0
        r = random.sample(range(1, l), 10)
    #loop para gerar as questões aleatorias do arquivo.
        while k <= 10:
         with open("Score.txt", "w") as fa:
            pontuacao = int(dictScore[nome])    
            x = r[y]
            x = str(x)
            print('        '+x+')'+str(dictQuestoes[x][0])+'?'+'   Nivel de Dificudade:'+str(dictQuestoes[x][6]))
            print('                                                '+'Nome: '+str(nome)+'  Score: '+str(pontuacao))
            z = 1
            fa.close
            while z <=4:
                print('        '+(dictQuestoes[x][z]))
                z+=1
            resposta = str(dictQuestoes[x][5]).upper()
            dificuldade = (dictQuestoes[x][6])
            valor = dificuldade.translate(str.maketrans('','','#$%&:;^_`{|}~'))
            print()
            resultado = input('        Resposta: ').upper()
            y+= 1
            if resultado == resposta: 
                #Adiciona pontos ao jogador e salvar no arquivo.
                with open("Score.txt", "w") as fa:
                    pontuacao = int(dictScore[nome])    
                    pontuacao += int(valor)
                    dictScore[nome] = pontuacao
                    fa.write(json.dumps(dictScore))
                    fa.close
                print('        Resposta Correta ')
                print('        ------------------------------------------')
                print()
            else:
                print('        Resposta Incorreta ')
                print('        ------------------------------------------')
                print()
            k+= 1
    f.close()
    return 
#Fução para cadastrar novas questões ao arquivo.
def cadastrarQuestoes():
    with open("Questoes.txt") as f:
        data = f.read()
    j = json.loads(data)
    dictQuestoes = j
    f = open("Questoes.txt", "r")
    ultimaChave = list(dictQuestoes.keys())[-1]
    proximoNumero = int(ultimaChave)+1
    numeroQuestao = proximoNumero
    print('        ------------------------------------------')
    if  numeroQuestao in dictQuestoes:
        print('        numero da questão já existente tente novamente')
        print('        ------------------------------------------')  
    else:
        enuciadoQuestao = input("        Digite o enuciado da questão: ")
        print('        ------------------------------------------')
        translateQuestao = enuciadoQuestao.translate(str.maketrans('','','#$%&:;^_`{|}~'))
        a = '1. '+input("        Digite a altenativa '1.': ")
        print('        ------------------------------------------')
        b = '2. '+input("        Digite a altenativa '2.': ")
        print('        ------------------------------------------')
        c = '3. '+input("        Digite a altenativa '3.': ")
        print('        ------------------------------------------')
        d = '4. '+input("        Digite a altenativa '4.': ")
        print('        ------------------------------------------')
        respostaCorreta = input('        Digite a alternativa correta: ')
        print('        ------------------------------------------')
        nivelDificuldade = (input('        Digite a dificuldade de 1 a 3 da questão: '))
        print('        ------------------------------------------')
        #Juntar os dados dos inputs em um dicionario temporario que será armazenado no arquivo para ser usado posteriormente.
        dictQuestoes[numeroQuestao] = [translateQuestao, a, b, c, d, respostaCorreta, nivelDificuldade]
        with open("Questoes.txt", "w") as fw:
            fw.write(json.dumps(dictQuestoes))
            fw.close

#Função para mostrar o 10 melhores jogadores em ordem decrescente tirando os valores do arquivo de score onde há o nome e os pontos do jogador em um dicionario.
def score():
    with open("Score.txt") as f:
        data = f.read()
        j = json.loads(data)
        dictScore = j
        scoreOrdenado= dict(sorted(dictScore.items(), key=operator.itemgetter(1),reverse=True))
        x = 0
        print('        ==============[ RANKING ]=================')
        while x <= 9:
            listaChaves = list(scoreOrdenado)
            chavesDecrescentes = listaChaves[x]
            print('        ------------------------------------------')
            print('        '+str(x+1)+". "+chavesDecrescentes+" : "+str(scoreOrdenado[chavesDecrescentes]))
            x+=1
#Função para alterar pergunta atraves do numero da pergunta escolhida.
def alterarQuestoes():
    with open("Questoes.txt") as f:
        data = f.read()
    j = json.loads(data)
    dictQuestoes = j
    print('        ------------------------------------------')
    numeroQuestao = (input('        Digite o numero da questão que deseja Alterar: '))
    print('        ------------------------------------------')
    if numeroQuestao in dictQuestoes:
        enuciado = input("        Digite o enuciado da questão: ")
        print('        ------------------------------------------')
        questao = enuciado.translate(str.maketrans('','','#$%&:;^_`{|}~'))
        a = '1. '+input("        Digite a altenativa '1.': ")
        print('        ------------------------------------------')
        b = '2. '+input("        Digite a altenativa '2.': ")
        print('        ------------------------------------------')
        c = '3. '+input("        Digite a altenativa '3.': ")
        print('        ------------------------------------------')
        d = '4. '+input("        Digite a altenativa '4.': ")
        print('        ------------------------------------------')
        respostaCorreta = input('        Digite a alternativa correta: ')
        print('        ------------------------------------------')
        nivelDificuldade = (input('        Digite a dificuldade de 1 a 3 da questão: '))
        print('        ------------------------------------------')
        dictQuestoes[numeroQuestao] = [questao, a, b, c, d, respostaCorreta, nivelDificuldade]
        with open("Questoes.txt", "w") as fw:
            fw.write(json.dumps(dictQuestoes))
            fw.close
    else:
        print('        ------------------------------------------')
        print('        Questão não está cadastrada, deseja cadastrar uma nova questão digite "S" para sim e "N" para não: ')
        print('        ------------------------------------------')
        r = input('        Resposta: ').upper()
        if r == 'S':
            cadastrarQuestoes()
        elif r == 'N':
            print('')
            return


#Menu de abertura com a pergunta se deve ou não iniciar o codigo.
print(''' 
        ======[ BEM VINDO AO SIMPLEQUIZ ]========
        -----------------------------------------
        Deseja iniciar o programa? 
        digite 'S' para sim e 'N' para não:
        -----------------------------------------''')
#Se sim ir para o loop do menu principal com as opções que poderam ser acessadas.
escolha = input('        Resposta: ').upper()
print('        ------------------------------------------')
while escolha != ('N'):
  if escolha == ('S').upper():
    print('''
        ===========[ MENU PRINCIPAL ]=============
        ------------------------------------------
        1. Iniciar
        2. Opções
        3. Ranking
        4. Sair
        ------------------------------------------''')
    opcao = input('        Resposta: ')
    print('        ------------------------------------------')
    print()
    if opcao == '1':
        carregaQuestoes(cadastrar())
        print('        ------------------------------------------')
        print()
    elif opcao == '2':
        print('''
        ===========[ MENU OPÇÕES ]=============
        ------------------------------------------
        1. Adicionar Questão
        2. Alterar Questão
        3. Remover Questão
        4. Buscar Questão
        5. Voltar ao Menu Principal
        ------------------------------------------
        
        ''')
        resposta = input('        Resposta: ')
        print('        ------------------------------------------')
        print()
        if resposta == '1':
            cadastrarQuestoes()
            print('        ------------------------------------------')
            print()
            
        elif resposta == '2':
            alterarQuestoes()
            print('        ------------------------------------------')
            print()
            
        elif resposta == '3':
            removerQuestoes()
            print('        ------------------------------------------')
            print()
            
        elif resposta == '4':
            buscaQuestoes()
            print('        ------------------------------------------')
            print()
            
    elif opcao == '3':
        score()
        print('        ------------------------------------------')
        print()
        
    elif opcao == '4':
        print('        ------------------------------------------')
        print('        ================[ SAIR ]==================')
        exit()
        