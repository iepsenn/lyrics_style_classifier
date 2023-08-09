# Lyrics Style Classifier

Repositório contendo modelos de ML para a tarefa de classificação do estilo musical de uma música através de sua letra.

## Gerando o conjunto de dados

O conjunto de dados foi obtido através do site [Letras](https://www.letras.mus.br/). Para gerar o arquivo `lyrics.csv` com os dados agrupados por estilo basta executar o script `make_dataset.py`:

```bash
python make_dataset.py numero_de_samples_por_estilo
```
