def converter_idade_em_anos_meses_dias(idade_em_dias):
  """Converter a idade em dias para idade em anos, meses e dias.

  Args:
    idade_em_dias: A idade em dias da pessoa.

  Returns:
    Uma tupla com a idade em anos, meses e dias.
  """

  anos = idade_em_dias // 365
  meses = (idade_em_dias % 365) // 30
  dias = (idade_em_dias % 365) % 30

  return anos, meses, dias


idade_em_dias = int(input("Digite a idade em dias: "))

anos, meses, dias = converter_idade_em_anos_meses_dias(idade_em_dias)

print(f"A idade em anos, meses e dias é: {anos} anos, {meses} meses e {dias} dias.")
