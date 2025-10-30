class UsuarioModel:
    funcionarios = [{"id":1, "nome":"Kiki", "email":"gabrielokimura@gmail.com", "senha":"senha123", "perfil":"admin"},
                {"id":2, "nome":"Roberto Akashi Almeida", "email":"robertin@gmail.com", "senha":"12345", "perfil":"recepcionista"},
                {"id":3, "nome":"Assef Jam", "email":"assef@gmail.com", "senha":"cabul", "perfil":"camareira"}]
    


    quartos = [{"numero":123, "tipo":"simples", "capacidade":2, "preco_diaria":106.38, "descricao":"Quarto básico com uma cama de casal e banheiro", "status":"limpo", "localização":"Ala Nordeste", "disponivel":True},
               {"numero":321, "tipo":"luxo", "capacidade":4, "preco_diaria":246.98, "descricao":"Quarto com duas camas de casal, televisão, ar condicionado e 1 banheiro com secador de cabelo", "status":"limpo", "localização":"Ala leste", "disponivel":False},
               {"numero":555, "tipo":"presidencial", "capacidade":12, "preco_diaria":1086.68, "descricao":"2 quartos grandes, 3 banheiros com hidromassagem, 2 televisões de plasma, ar condicionado em todos os cômodos e privada tecnológica", "status":"limpo", "localização":"Ala sul", "disponivel":False}]
    


    reservas = [{"id":1, "id_hospede":1, "numero_quarto":123, "data_checkin":"31/02/2025", "data_checkout":"03/03/2025", "status_reserva":"confirmada", "valor_total":425.52}]



    hospedes = [{"id":1, "nome":"Márcia dos Almeidas", "cpf": "12345678910121", "telefone":"1234567891012345690", "email":"marcia@gmail.com", "perfil":"hospede"}]



    servicos = [{"id":1, "nome":"toalha extra", "preco":22}]



    faturas = [{"id":1, "id_reserva":1, "data_emissao":"03/03/2025", "valor_servicos":22, "valor_diarias":425.52, "status_pagamento":"pago"}]



    itens_fatura= [{"id":1, "id_fatura":1, "id_servico":1, "quantidade":1, "valor":22, "data_consumo":"02/03/2025"}]


    id_usuario = 4
    id_fatura = 2
    id_servico = 2
    id_hospede = 2
    id_reserva =2



    def adicionar_funcionario(self, nome, email, senha, perfil):
        novo_usuario = {"id":self.id_usuario, "nome":nome, "email":email, "senha":senha, "perfil":perfil}
        self.funcionarios.append(novo_usuario)
        self.id_usuario+=1
        return novo_usuario
    



    def remover_funcionario(self, nome, email):
        for usuario in self.funcionarios:
            if usuario["nome"] == nome and usuario["email"] == email:
                self.funcionarios.remove(usuario)



    def adicionar_hospede(self,nome, cpf, telefone, email):
        novo_hospede = {"id": self.id_hospede, "nome":nome, "cpf": cpf, "telefone":telefone, "email":email, "perfil":"hospede"}
        self.id_hospede+=1
        self.hospedes.append(novo_hospede)
                




    def remover_hospede(self,nome,cpf):
        for hospede in self.hospedes:
            if hospede["nome"] == nome and hospede["cpf"] == cpf:
                self.hospedes.remove(hospede)


