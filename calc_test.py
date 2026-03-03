def test_sum():
    sum = 2 + 2
    assert sum == 4

    def test_sum():
        sum = 2 + 2
        assert sum == 5

# Função que inverte uma string
def reverse_string(word):
    return ''.join(reversed(word))

# Teste. Verificação da função reverse_string
def test_reverse_string():
    input_str = "TripleTen"

    # Realize a operação inversa
    reversed_str = reverse_string(input_str)

    # Verifique se a string invertida corresponde ao resultado esperado
    assert reversed_str == "neTelpirT"

    print("Teste Aprovado! " + input_str + " invertido é " + reversed_str)
    