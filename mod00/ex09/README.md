# ft_package

Pacote Python criado para o exercício 09 do módulo 00 da Piscina Python for Data Science.

## Descrição
O `ft_package` contém funções utilitárias desenvolvidas como parte do aprendizado de criação de pacotes Python. Atualmente, inclui a função `count_in_list`.

## Estrutura
```
ft_package/
	__init__.py
	count_in_list.py
```

## Instalação
Para instalar o pacote localmente, execute:

```bash
cd ex09
pip install build
python setup.py sdist
python -m build
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Uso
Exemplo de uso da função `count_in_list`:

```python
from ft_package.count_in_list import count_in_list

lista = [1, 2, 2, 3, 2, 4]
resultado = count_in_list(lista, 2)
print(resultado)  # Saída: 3
```

## Autor
Everton Vaz

## Licença
Veja o arquivo LICENSE para mais informações.
