def eh_triangulo(a, b, c):
  """Verifica se os valores a, b e c formam um triângulo.

  Args:
    a: O comprimento do lado a do triângulo.
    b: O comprimento do lado b do triângulo.
    c: O comprimento do lado c do triângulo.

  Returns:
    True se os valores formam um triângulo, False caso contrário.
  """

  return a <= b + c and b <= a + c and c <= a + b


def calcular_area_triangulo(a, b, c):
  """Calcula a área de um triângulo a partir dos comprimentos dos seus lados.

  Args:
    a: O comprimento do lado a do triângulo.
    b: O comprimento do lado b do triângulo.
    c: O comprimento do lado c do triângulo.

  Returns:
    A área do triângulo.
  """

  s = (a + b + c) / 2
  return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def main():
  """Função principal."""

  a = int(input("Digite o valor de a: "))
  b = int(input("Digite o valor de b: "))
  c = int(input("Digite o valor de c: "))

  if eh_triangulo(a, b, c):
    area = calcular_area_triangulo(a, b, c)
    print(f"Os valores formam um triângulo e sua área é {area}")
  else:
    print(f"Os valores {a}, {b} e {c} não formam um triângulo")


if __name__ == "__main__":
  main()