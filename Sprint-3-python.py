APPS_BLOQUEADOS = ["Instagram", "TikTok"]
APPS_LIBERADOS = ["Khan Academy", "Wikipedia"]

MATERIAS = {
    "Matemática": {
        "Geometria Plana": {
            "flashcards": [("Fórmula da área de um triângulo?", "A = (base x altura) / 2", [0, 0])],
            "questoes": [("Fórmula da área de um círculo?", ["A = 2πr", "A = πr²"], 1)],
        }
    },
    "Física": {
        "Leis de Newton": {
            "flashcards": [("O que diz a 1ª Lei de Newton?", "Inércia.", [0, 0])],
            "questoes": [("Fórmula da 2ª Lei de Newton?", ["F = m . a", "V = v0 + at"], 0)],
        }
    },
}


def ler_numero(msg, minimo, maximo):
    while True:
        entrada = input(msg).strip()
        if entrada.isdigit() and minimo <= int(entrada) <= maximo:
            return int(entrada)
        print(f"Digite um número entre {minimo} e {maximo}.")


def ler_confirmacao(msg):
    return input(msg + " (s/n): ").strip().lower() == "s"


def login():
    print("=" * 40, "\n  JOVI V70 - MODO ESTUDO\n" + "=" * 40)
    while True:
        usuario = input("Usuário (ou 'sair'): ").strip()
        if usuario.lower() == "sair":
            print("Encerrando o Jovi V70. Até logo!")
            exit()
        senha = input("Senha: ").strip()
        if usuario == "aluno" and senha == "1234":
            print("\nLogin realizado com sucesso! Bem-vindo, Aluno!")
            return usuario
        print("Usuário ou senha inválidos. (dica: aluno / 1234)\n")


def escolher_topico():
    lista = [(m, t) for m, topicos in MATERIAS.items() for t in topicos]
    print("\nTópicos disponíveis:")
    for i, (m, t) in enumerate(lista, 1):
        print(i, "-", m, ":", t)
    escolha = ler_numero("Escolha um tópico: ", 1, len(lista))
    materia, topico = lista[escolha - 1]
    return MATERIAS[materia][topico], topico


def escanear():
    _, topico = escolher_topico()
    texto = ""
    while not texto:
        texto = input("Digite o texto do quadro/caderno: ").strip()
    print(f"\nResumo de {topico}: {texto[:40]}...")


def flashcards():
    dados, topico = escolher_topico()
    cards = dados["flashcards"]
    if not cards:
        print("Este tópico não possui flashcards.")
        return
    for pergunta, resposta, placar in cards:
        print("\nPergunta:", pergunta)
        input("ENTER para ver a resposta...")
        print("Resposta:", resposta)
        placar[0 if ler_confirmacao("Você acertou?") else 1] += 1
    acertos = sum(c[2][0] for c in cards)
    tentativas = sum(c[2][0] + c[2][1] for c in cards)
    progresso = round(acertos / tentativas * 100, 1) if tentativas else 0
    print(f"\nProgresso: {progresso}%")


def simulado():
    dados, _ = escolher_topico()
    questoes = dados["questoes"]
    if not questoes:
        print("Este tópico não possui questões.")
        return
    acertos = 0
    for enunciado, alternativas, correta in questoes:
        print("\n" + enunciado)
        for i, alt in enumerate(alternativas):
            print(i, "-", alt)
        resposta = ler_numero("Digite o número da alternativa: ", 0, len(alternativas) - 1)
        if resposta == correta:
            print("Resposta correta!")
            acertos += 1
        else:
            print("Resposta incorreta. A correta era:", alternativas[correta])
    print(f"\nVocê acertou {acertos} de {len(questoes)} questões.")


def modo_estudo(estado):
    estado["ativo"] = not estado["ativo"]
    if estado["ativo"]:
        print("\nModo Estudo ATIVADO.")
        print("Bloqueados:", ", ".join(APPS_BLOQUEADOS))
        print("Liberados:", ", ".join(APPS_LIBERADOS))
    else:
        print("\nModo Estudo DESATIVADO.")


def main():
    usuario = login()
    estado = {"ativo": False}
    acoes = {1: escanear, 2: flashcards, 3: simulado, 4: lambda: modo_estudo(estado)}

    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Escanear conteúdo\n2. Revisar flashcards\n3. Realizar simulado\n4. Modo Estudo\n5. Sair")
        opcao = ler_numero("Escolha: ", 1, 5)
        if opcao == 5:
            print(f"\nAté logo, {usuario}! Bons estudos.")
            break
        acoes[opcao]()


if __name__ == "__main__":
    main()