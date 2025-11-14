from datetime import datetime

class UsuarioModel:
    funcionarios = [{"id":1, "nome":"Kiki", "email":"gabrielokimura@gmail.com", "senha":"senha123", "perfil":"admin"},
                {"id":2, "nome":"Roberto Akashi Almeida", "email":"robertin@gmail.com", "senha":"12345", "perfil":"recepcionista"},
                {"id":3, "nome":"Assef Jam", "email":"assef@gmail.com", "senha":"cabul", "perfil":"camareira"}]
    


    quartos = [{"id":1,"numero":123, "tipo":"simples", "capacidade":2, "preco_diaria":106.38, "descricao":"Quarto básico com uma cama de casal e banheiro", "status":"limpo", "localização":"Ala Nordeste", "disponivel":True},
               {"id":2,"numero":321, "tipo":"luxo", "capacidade":4, "preco_diaria":246.98, "descricao":"Quarto com duas camas de casal, televisão, ar condicionado e 1 banheiro com secador de cabelo", "status":"limpo", "localização":"Ala leste", "disponivel":False},
               {"id":3,"numero":555, "tipo":"presidencial", "capacidade":12, "preco_diaria":1086.68, "descricao":"2 quartos grandes, 3 banheiros com hidromassagem, 2 televisões de plasma, ar condicionado em todos os cômodos e privada tecnológica", "status":"limpo", "localização":"Ala sul", "disponivel":True}]
    


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
    id_quarto = 4

    def atualizar_quarto(self, id ,numero, tipo, capacidade,preco_diaria, descricao,status, localizacao, disponivel ):
        for quarto in self.quartos:
            if quarto["id"] == int(id):
                quarto_certo = quarto
                break
        else:
            return "Quarto não encontrado"
        indice = self.quartos.index(quarto_certo)
        if disponivel =="sim":
            disponivel = True
        else:
            disponivel = False
        self.quartos[indice] = {"id":self.id_quarto, "numero":numero, "tipo":tipo, "capacidade":capacidade, "preco_diaria":preco_diaria,"descricao":descricao,"status":status,"localizacao":localizacao,"disponivel":disponivel}
        self.id_quarto+=1
        

        

    def atualizar_status_quarto(self, numero,status):
        for quarto in self.quartos:
            if quarto["numero"] == int(numero):
                quarto_certo =quarto
                break
        indice = self.quartos.index(quarto_certo)
        self.quartos[indice]["status"] = status


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
        return novo_hospede
                




    def remover_hospede(self,nome,cpf):
        for hospede in self.hospedes:
            if hospede["nome"] == nome and hospede["cpf"] == cpf:
                self.hospedes.remove(hospede)



    def adicionar_reserva(self,id_hospede, numero_quarto,data_checkin,data_checkout, status_reserva):
        for quarto in self.quartos:
            if int(numero_quarto) == quarto["numero"] and quarto["disponivel"]:
                quarto["disponivel"] = False
                preco_quarto = quarto["preco_diaria"]
                break
        else:
            return "Quarto indisponivel ou inexistente"
        
        for hospede in self.hospedes:
            if int(id_hospede) == hospede["id"]:
                break
        else:
            return "hospede inexistente"
        
        data1 = datetime.strptime(data_checkin, '%d/%m/%Y')
        data2 = datetime.strptime(data_checkout, '%d/%m/%Y')

        diferenca = data2 - data1

        dias = diferenca.days


        nova_reserva = {"id":self.id_reserva, "id_hospede":int(id_hospede), "numero_quarto":int(numero_quarto), "data_checkin":data_checkin, "data_checkout":data_checkout,"status_reserva":status_reserva, "valor_total":preco_quarto*dias }

        self.reservas.append(nova_reserva)
        self.id_reserva+=1






    def alterar_reserva(self,id_reserva,id_hospede, numero_quarto,data_checkin,data_checkout, status_reserva):
        for reserva in self.reservas:
            if int(id_reserva) == reserva["id"]:
                reserva_certa =reserva
        if reserva_certa["numero_quarto"] != int(numero_quarto):
            for quarto in self.quartos:
                if int(numero_quarto) == quarto["numero"] and quarto["disponivel"]:
                    quarto["disponivel"] = False
                    preco_quarto = quarto["preco_diaria"]
                    break
                        
            else:
                return "Quarto indisponivel ou inexistente"
        else:
            for quarto in self.quartos:
                if reserva_certa["numero_quarto"] == quarto["numero"]:
                    preco_quarto = quarto["preco_diaria"]
                    break
                    
        for hospede in self.hospedes:
            if int(id_hospede) == hospede["id"]:
                break
        else:
            return "hospede inexistente"
        data1 = datetime.strptime(data_checkin, '%d/%m/%Y')
        data2 = datetime.strptime(data_checkout, '%d/%m/%Y')

        diferenca = data2 - data1

        dias = diferenca.days

        
        for reserva in self.reservas:
            if reserva == reserva_certa:
                indice = self.reservas.index(reserva)
                self.reservas[indice] = {"id":self.id_reserva, "id_hospede":int(id_hospede), "numero_quarto":int(numero_quarto), "data_checkin":data_checkin, "data_checkout":data_checkout,"status_reserva":status_reserva, "valor_total":preco_quarto*dias }
                self.id_reserva+=1
                break
            
        
        
        


       