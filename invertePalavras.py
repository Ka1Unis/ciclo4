def inverter_palavras(frase):
  """Inverte as letras de cada palavra de uma frase.

  Args:
    frase: A frase a ser alterada.

  Returns:
    Uma nova frase com as letras de cada palavra invertidas.
  """

  palavras = frase.split()
  nova_frase = ""

  for palavra in palavras:
    palavra_invertida = palavra[::-1]
    nova_frase += palavra_invertida + " "

  return nova_frase.strip()


def main():
  """Função principal."""

  frase = input("Digite uma frase: ")

  nova_frase = inverter_palavras(frase)
  print(f"Frase com as palavras invertidas: {nova_frase}")


if __name__ == "__main__":
  main()