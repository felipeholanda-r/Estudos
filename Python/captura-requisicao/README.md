# Info
Endpoint que captura as informações enviadas para ele e retorna a requisição que foi recebida.
Interessante quando se quer saber como a requisição está chegando no destino e se está no padrão desejado.

# Como executar
Para rodar basta rodar o seguinte comando no terminal:
~~~ bash
uvicorn app:app --host 0.0.0.0 --port 3000 --reload
~~~