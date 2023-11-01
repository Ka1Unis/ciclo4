def menor_valor(a, b, c):
  """Retorna o menor dos três valores a, b e c.

  Args:
    a: O primeiro valor.
    b: O segundo valor.
    c: O terceiro valor.

  Returns:
    O menor dos três valores.
  """

  menor = a
  if b < menor:
    menor = b
  if c < menor:
    menor = c

  return menor


def main():
  """Função principal."""

  a = int(input("Digite o primeiro valor: "))
  b = int(input("Digite o segundo valor: "))
  c = int(input("Digite o terceiro valor: "))

  menor = menor_valor(a, b, c)
  print(f"O menor valor é {menor}")


if __name__ == "__main__":
  main()