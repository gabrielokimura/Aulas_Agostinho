class Produto:
    _PRODUTOS = [
    {"id": 1, "nome": "Notebook Gamer X", "preco": 5200.00},
    {"id": 2, "nome": "Mouse sem fio", "preco": 150.00},
    {"id": 3, "nome": "Teclado mecanico RGB", "preco": 350.00},
    {"id": 4, "nome": "Monitor 27 polegadas", "preco": 1800.00},
    {"id": 5, "nome": "Notebook cromossomo Y", "preco": 6000.00},
    {"id": 6, "nome": "Controle do the last of us 8", "preco": 800.00},
    {"id": 7, "nome": "Mouse com fio infinito", "preco": 80.00},
    {"id": 8, "nome": "Cosplay de nier aut", "preco": 2000.00},
    {"id": 9, "nome": "Oculos vr 2", "preco": 20.00},
    {"id": 10, "nome": "Gabriel Okimura", "preco": 15.00},
    {"id": 11, "nome": "Controle do god of war ps3", "preco": 40.00},
    {"id": 12, "nome": "Play 2 desbloqueado", "preco": 180.00}
]
    _proximo_id = 13

    def adicionar_produto(self, nome, preco):
        novo_produto = {"id":self._proximo_id, "nome":nome, "preco": preco}
        self._proximo_id +=1
        self._PRODUTOS.append(novo_produto)




    def remover_produto(self, nome):
        for produto in self._PRODUTOS:
            if produto["nome"] == nome:
                self._PRODUTOS.remove(produto)


    def achar_produtos(self, id):
        produto_encontrado = None
        for produto in self._PRODUTOS:
            if produto["id"] == id:
                produto_encontrado = produto
                return produto_encontrado
        if produto_encontrado is None:
            return None

        


        


