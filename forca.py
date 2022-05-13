from random import randint

def imprime_mensagem_abertura():
    print('-' * 30)
    print(f'{" Jogo da Forca ": ^30}')
    print('-' * 30)

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    lista_palavras = []
    for linha in arquivo:
        linha = linha.strip()
        lista_palavras.append(linha)
    arquivo.close()

    sortear_palavra = lista_palavras[randint(0,(len(lista_palavras) - 1))]
    palavra_secreta = sortear_palavra
    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]


def imprime_mensagem_numero_letras(letras_acertadas):
    print(f'A palavra tem {len(letras_acertadas)} letras.')
    print(letras_acertadas)
    print('-' * 30)


def pede_chute():
    return str(input('\nTeste uma letra: ')).lower().strip()


def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index = index + 1


def marca_erro(erros):
    erros += 1
    print(f'→ {erros} erro(s)')
    return erros


def imprime_resultado_do_chute(letras_acertadas, chute):
    print(f'→ Temos {letras_acertadas.count(chute)} letra(s) "{chute.lower()}".')
    print(letras_acertadas)


def imprime_mensagem_final(palavra_secreta, enforcou, acertou, erros):
    if enforcou:
        print(f'\nVocê atingiu {erros} erros. Fim do jogo.')
        print('(╯°□°）╯︵ ┻━┻')
    elif acertou:
        print(f'\nVocê ganhou! Após {erros} tentativas erradas.')
        print('╰(*°▽°*)╯')
    print(f'Palavra secreta: {palavra_secreta}.')


def imprime_letras_chutadas(letras_chutadas, chute):
    letras_chutadas.append(chute)
    print(f'→ Chutes: {letras_chutadas}')


def jogar():

    # TÍTULO
    imprime_mensagem_abertura()

    # ABRINDO ARQUIVO DAS PALAVRAS
    palavra_secreta = carrega_palavra_secreta()

    # VARIÁVEIS
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    letras_chutadas = []

    enforcou = False
    acertou = False
    erros = 0

    # IMPRIME MENSAGEM DIZENDO QUANTAS LETRAS TEM NA PALAVRA
    imprime_mensagem_numero_letras(letras_acertadas)

    # LAÇO DE CHUTES: O QUE ACONTECE NOS ERROS E ACERTOS
    while not enforcou and not acertou:
        chute = pede_chute()


        if chute in palavra_secreta:
           marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros = marca_erro(erros)

        imprime_resultado_do_chute(letras_acertadas, chute)
        imprime_letras_chutadas(letras_chutadas, chute)

        # SAÍDAS DO LAÇO
        enforcou = erros == 10
        acertou = "_" not in letras_acertadas

    # FINAL DO JOGO
    imprime_mensagem_final(palavra_secreta, enforcou, acertou, erros)


if (__name__ == '__main__'):
    jogar()