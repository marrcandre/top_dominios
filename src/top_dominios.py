def carrega_dados():
    return open('emails.txt', encoding='utf-8').readlines()


def extrai_dominio(email):
    inicio = email.find('@') + 1
    email = email[inicio:].strip()
    return email


def tabula_dominios(emails):
    dominios = {}
    for email in emails[1:]:
        dominio = extrai_dominio(email)
        if not dominio: 
            continue
        if dominio not in dominios:
            dominios[dominio] = 0
        dominios[dominio] += 1
    return dominios


def ordena_dominios(dominios):
    from operator import itemgetter
    return sorted(dominios.items(), key=itemgetter(1), reverse=True)


def grava_csv(dominios):
    saida = open('top_dominios.csv', 'w')

    saida.write('%s,%s\n' % ('dominio', 'ocorrencias'))
    for dominio, ocorrencias in dominios:
        saida.write('%s,%d\n' % (dominio, ocorrencias))

    saida.close()


def separa_dados(dados):
    rotulos = []
    valores = []
    for rotulo, valor in dados:
        rotulos.append(rotulo)
        valores.append(valor)
    return rotulos, valores


def plota_grafico(dados):
    import matplotlib.pyplot as plt

    rotulos, valores = separa_dados(dados)

    plt.pie(valores[:5], labels=rotulos[:5], autopct='%.1f%%', shadow=True, startangle=140)
    plt.title("Domínios mais usados")
    plt.show()
    plt.savefig('top_dominios.png')
    plt.close()

def main():
    emails = carrega_dados()
    dominios = tabula_dominios(emails)
    dominios_ordenados = ordena_dominios(dominios)
    grava_csv(dominios_ordenados)
    plota_grafico(dominios_ordenados)

if __name__ == "__main__":
    main()
