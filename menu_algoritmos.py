"""
╔══════════════════════════════════════════════════════════╗
║         MENU INTERATIVO - 8 ALGORITMOS COM LISTAS        ║
╚══════════════════════════════════════════════════════════╝
"""

# ─────────────────────────────────────────────
#  Funções auxiliares de exibição
# ─────────────────────────────────────────────

def cabecalho(titulo):
    largura = 56
    print()
    print("═" * largura)
    print(f"  {titulo}")
    print("═" * largura)


def separador():
    print("─" * 56)


def ler_inteiro(mensagem):
    """Lê e valida um número inteiro do usuário."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("  ⚠  Entrada inválida. Digite um número inteiro.")


def ler_lista(quantidade, rotulo="número"):
    """Lê uma lista de inteiros do usuário."""
    numeros = []
    for i in range(1, quantidade + 1):
        n = ler_inteiro(f"  Digite o {i}º {rotulo}: ")
        numeros.append(n)
    return numeros


# ─────────────────────────────────────────────
#  Algoritmo 1 – Maior e menor de 10 números
# ─────────────────────────────────────────────

def algoritmo1():
    cabecalho("ALGORITMO 1 — Maior e Menor Valor")
    print("  Leia 10 números inteiros.")
    separador()

    numeros = ler_lista(10)

    maior = numeros[0]
    menor = numeros[0]

    for n in numeros:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    separador()
    print(f"  Lista     : {numeros}")
    print(f"  ✔ Maior   : {maior}")
    print(f"  ✔ Menor   : {menor}")


# ─────────────────────────────────────────────
#  Algoritmo 2 – Pares e ímpares de 15 números
# ─────────────────────────────────────────────

def algoritmo2():
    cabecalho("ALGORITMO 2 — Pares e Ímpares")
    print("  Leia 15 números inteiros.")
    separador()

    numeros = ler_lista(15)

    pares   = []
    impares = []

    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    separador()
    print(f"  Números pares   : {pares}")
    print(f"  Números ímpares : {impares}")


# ─────────────────────────────────────────────
#  Algoritmo 3 – Busca em lista de 8 números
# ─────────────────────────────────────────────

def algoritmo3():
    cabecalho("ALGORITMO 3 — Busca na Lista")
    print("  Leia 8 números inteiros.")
    separador()

    numeros = ler_lista(8)

    separador()
    print(f"  Lista : {numeros}")
    separador()
    busca = ler_inteiro("  Digite o número a buscar: ")

    encontrado = False
    for n in numeros:
        if n == busca:
            encontrado = True
            break

    if encontrado:
        print(f"  ✔ O número {busca} ESTÁ presente na lista.")
    else:
        print(f"  ✘ O número {busca} NÃO está presente na lista.")


# ─────────────────────────────────────────────
#  Algoritmo 4 – Remoção de ocorrências
# ─────────────────────────────────────────────

def algoritmo4():
    cabecalho("ALGORITMO 4 — Remoção de Ocorrências")
    print("  Leia 10 números inteiros.")
    separador()

    numeros = ler_lista(10)

    separador()
    print(f"  Lista original : {numeros}")
    separador()
    remover = ler_inteiro("  Digite o número a remover: ")

    ocorrencias = 0
    nova_lista  = []

    for n in numeros:
        if n == remover:
            ocorrencias += 1
        else:
            nova_lista.append(n)

    if ocorrencias == 0:
        print(f"  ✘ O número {remover} não existe na lista.")
    else:
        print(f"  ✔ {ocorrencias} ocorrência(s) de {remover} removida(s).")
        print(f"  Lista atualizada : {nova_lista}")


# ─────────────────────────────────────────────
#  Algoritmo 5 – Positivos, negativos e zeros
# ─────────────────────────────────────────────

def algoritmo5():
    cabecalho("ALGORITMO 5 — Positivos, Negativos e Zeros")
    print("  Leia 20 números inteiros.")
    separador()

    numeros   = ler_lista(20)
    positivos = 0
    negativos = 0
    zeros     = 0

    for n in numeros:
        if n > 0:
            positivos += 1
        elif n < 0:
            negativos += 1
        else:
            zeros += 1

    separador()
    print(f"  Lista      : {numeros}")
    separador()
    print(f"  Positivos  : {positivos}")
    print(f"  Negativos  : {negativos}")
    print(f"  Zeros      : {zeros}")


# ─────────────────────────────────────────────
#  Algoritmo 6 – Interseção e exclusivos
# ─────────────────────────────────────────────

def algoritmo6():
    cabecalho("ALGORITMO 6 — Interseção e Exclusivos")
    print("  Crie duas listas com 5 números cada.")
    separador()

    print("  » Lista A:")
    lista_a = ler_lista(5)
    print("  » Lista B:")
    lista_b = ler_lista(5)

    comuns       = []
    exclusivos_a = []
    exclusivos_b = []

    # Comuns (interseção)
    for n in lista_a:
        if n in lista_b and n not in comuns:
            comuns.append(n)

    # Exclusivos de A
    for n in lista_a:
        if n not in lista_b and n not in exclusivos_a:
            exclusivos_a.append(n)

    # Exclusivos de B
    for n in lista_b:
        if n not in lista_a and n not in exclusivos_b:
            exclusivos_b.append(n)

    separador()
    print(f"  Lista A            : {lista_a}")
    print(f"  Lista B            : {lista_b}")
    separador()
    print(f"  Valores em comum   : {comuns if comuns else '(nenhum)'}")
    print(f"  Exclusivos de A    : {exclusivos_a if exclusivos_a else '(nenhum)'}")
    print(f"  Exclusivos de B    : {exclusivos_b if exclusivos_b else '(nenhum)'}")


# ─────────────────────────────────────────────
#  Algoritmo 7 – Cadastro de produtos
# ─────────────────────────────────────────────

def algoritmo7():
    cabecalho("ALGORITMO 7 — Cadastro de Produtos")
    print("  Cadastre 5 produtos (nome, preço, estoque).")
    separador()

    nomes     = []
    precos    = []
    estoques  = []

    for i in range(1, 6):
        print(f"\n  [ Produto {i} ]")
        nome = input("  Nome      : ").strip()
        while not nome:
            nome = input("  Nome (obrigatório): ").strip()

        while True:
            try:
                preco = float(input("  Preço (R$): ").replace(",", "."))
                if preco < 0:
                    print("  ⚠  Preço não pode ser negativo.")
                    continue
                break
            except ValueError:
                print("  ⚠  Digite um valor numérico.")

        estoque = ler_inteiro("  Estoque   : ")

        nomes.append(nome)
        precos.append(preco)
        estoques.append(estoque)

    # Produto mais caro
    indice_caro = 0
    for i in range(1, 5):
        if precos[i] > precos[indice_caro]:
            indice_caro = i

    separador()
    print("  PRODUTOS COM ESTOQUE < 10:")
    algum = False
    for i in range(5):
        if estoques[i] < 10:
            print(f"    • {nomes[i]}  (estoque: {estoques[i]})")
            algum = True
    if not algum:
        print("    (nenhum produto com estoque crítico)")

    separador()
    print(f"  PRODUTO MAIS CARO:")
    print(f"    • {nomes[indice_caro]}  — R$ {precos[indice_caro]:.2f}")


# ─────────────────────────────────────────────
#  Algoritmo 8 – Ordenação e contagem
# ─────────────────────────────────────────────

def algoritmo8():
    cabecalho("ALGORITMO 8 — Ordenação e Contagem")
    print("  Leia 12 números inteiros.")
    separador()

    numeros = ler_lista(12)

    # Ordenação crescente (bubble sort manual)
    crescente = numeros[:]
    n = len(crescente)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if crescente[j] > crescente[j + 1]:
                crescente[j], crescente[j + 1] = crescente[j + 1], crescente[j]

    decrescente = crescente[::-1]

    pares   = 0
    impares = 0
    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

    separador()
    print(f"  Lista original  : {numeros}")
    print(f"  Ordem crescente : {crescente}")
    print(f"  Ordem decrescente: {decrescente}")
    separador()
    print(f"  Pares   : {pares}")
    print(f"  Ímpares : {impares}")


# ─────────────────────────────────────────────
#  Menu principal
# ─────────────────────────────────────────────

def exibir_menu():
    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║        MENU INTERATIVO — ALGORITMOS COM LISTAS       ║")
    print("╠══════════════════════════════════════════════════════╣")
    print("║  1. Maior e menor de 10 números                      ║")
    print("║  2. Pares e ímpares de 15 números                    ║")
    print("║  3. Busca em lista de 8 números                      ║")
    print("║  4. Remoção de ocorrências em lista de 10 números    ║")
    print("║  5. Positivos, negativos e zeros de 20 números       ║")
    print("║  6. Interseção e exclusivos de duas listas           ║")
    print("║  7. Cadastro e análise de 5 produtos                 ║")
    print("║  8. Ordenação e contagem de 12 números               ║")
    print("╠══════════════════════════════════════════════════════╣")
    print("║  0. Sair                                             ║")
    print("╚══════════════════════════════════════════════════════╝")


def main():
    algoritmos = {
        1: algoritmo1,
        2: algoritmo2,
        3: algoritmo3,
        4: algoritmo4,
        5: algoritmo5,
        6: algoritmo6,
        7: algoritmo7,
        8: algoritmo8,
    }

    while True:
        exibir_menu()
        opcao = ler_inteiro("\n  Escolha uma opção: ")

        if opcao == 0:
            print()
            print("  Encerrando o programa. Até logo! 👋")
            print()
            break
        elif opcao in algoritmos:
            algoritmos[opcao]()
            separador()
            input("  Pressione ENTER para voltar ao menu...")
        else:
            print("  ⚠  Opção inválida! Escolha entre 0 e 8.")


# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()
