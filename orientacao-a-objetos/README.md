# Orientação a Objetos

Atividade 3 do curso.

## Quiz relâmpago

**Qual a diferença de uma classe e um objeto?**
A classe é o molde, tipo a planta do carro. O objeto é o carro que foi feito a partir dela, com valores próprios (cor, km rodado etc). Da mesma classe dá pra criar vários objetos.

**Pra que serve o self?**
É a referência ao próprio objeto. É por ele que um método acessa os atributos e os outros métodos daquele objeto, como `self.marca`.

**O que o método `__init__` faz?**
É o construtor. Ele roda quando o objeto é criado e define quais dados precisam ser passados e quais atributos o objeto começa tendo.

**Por que usar getter/setter em vez de mexer no atributo direto?**
Pra ter controle sobre como o atributo é lido e alterado. No setter dá pra validar o valor antes de salvar, e se a regra mudar depois é só mexer no método, sem precisar caçar todo lugar do código que usava o atributo.
