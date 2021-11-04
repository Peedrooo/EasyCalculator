def traduzGit(lista):
    lista = lista.replace("V", "v")
    lista = lista.replace("^", "&")
    lista = lista.replace("∧", "&")
    lista = lista.replace("-", "")
    lista = lista.replace("=>", "|")
    lista = lista.replace("→", ">")

    return lista

conteudo = ''
while conteudo != " ":
    conteudo = input("Digite a expressão: ")
    print(traduzGit(conteudo))
