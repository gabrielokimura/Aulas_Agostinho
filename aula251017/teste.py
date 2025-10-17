class UsuarioModel:
    
    # Simulador de um banco de dados, normalmente SQLAlchemy
    
    _usuarios = [
        {"id":1, "nome": "Ana Silva", "email":"ana@gmail.com", "senha":"ana", "logado":False, "admin":True},
        {"id":2, "nome": "Bruno Costa", "email":"bruno@gmail.com", "senha":"bruno", "logado":False, "admin":False}
    ]

    _proximo_id = 3
    mensagem = ""
    mensagem2 =""




    def get_todos(self):
        return self._usuarios
    
    def get_um(self, id_usuario):
        for usuario in self._usuarios:
            if usuario["id"] == id_usuario:
                return usuario
        return None
    
    def salvar(self, nome, email, senha):
        novo_usuario = {"id":self._proximo_id, "nome":nome, "email": email, "senha":senha, "logado":False, "admin":False}
        self._usuarios.append(novo_usuario)
        self._proximo_id+=1
        return novo_usuario
    

    def remover(self, nome, email):
        for usuario in self._usuarios:
            if usuario["nome"] == nome and usuario["email"] == email:
                self._usuarios.pop((usuario["id"]-1))
                for usuario2 in self._usuarios:
                    usuario2["id"] = usuario2["id"]-1
                self._proximo_id = self._proximo_id-1
                return
        self.mensagem ="email ou senha incorretos"
        
        


    def logar(self,nome, email, senha):
        for usuario in self._usuarios:
            if usuario["logado"] == True:
                usuario["logado"] = False
        for usuario in self._usuarios:
            if usuario["nome"] == nome and usuario["email"] == email and usuario["senha"] == senha:
                usuario["logado"] = True
                return
        self.mensagem2 = "email ou senha incorretos"





        <ul>
        {% for produto in produtos %}
        <li>{{ produto.nome }}</li>
        {% endfor %}
    </ul>

    <nav>
        <ul class="pagination">
            {% for page_num in range(1, total_pages+1) %}
            <li class="page-item {% if page == page_num %} active {% endif %}">
                <a class="page-link" href="{{ url_for('listar_produtos_paginados', page = page_num) }}">
                    {{ page_num }}
                </a>
            </li>
            {% endfor %}
        </ul>
    </nav>













































@app.route('/produtos_paginados')
def listar_produtos_paginados():
    page = request.args.get('page', 1, type=int)
    per_page = 5

    start = (page - 1) * per_page
    end = start + per_page
    total_pages = math.ceil(len( produto._PRODUTOS) / per_page)

    produtos_da_pagina =  produto._PRODUTOS[start:end]

    return render_template('produtos_paginados.html', produtos = produtos_da_pagina, page=page, total_pages=total_pages)