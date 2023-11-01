def eh_primo(numero):
  """Verifica se um número é primo.

  Args:
    numero: O número a ser verificado.

  Returns:
    True se o número for primo, False caso contrário.
  """

  if numero <= 1:
    return False

  for i in range(2, numero):
    if numero % i == 0:
      return False

  return True


def main():
  """Função principal."""

  for numero in range(1, 101):
    if eh_primo(numero):
      print(numero, "é primo")
    else:
      print(numero, "não é primo")


if __name__ == "__main__":
  main()