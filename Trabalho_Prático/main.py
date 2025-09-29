import csv

# ==========================
# Funções de Usuários
# ==========================

def carregar_usuarios():
    usuarios = {}
    try:
        with open("usuarios.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for linha in reader:
                usuarios[linha["id"]] = linha
    except FileNotFoundError:
        pass
    return usuarios

def salvar_usuarios(usuarios):
    with open("usuarios.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "nome", "senha", "categoria"])
        writer.writeheader()
        for u in usuarios.values():
            writer.writerow(u)

def criar_usuario(usuarios):
    novo_id = str(len(usuarios) + 1)
    nome = input("Nome: ")
    senha = input("Senha: ")
    categoria = input("Categoria (gerente/funcionario/estagiario): ")
    usuarios[novo_id] = {"id": novo_id, "nome": nome, "senha": senha, "categoria": categoria}
    salvar_usuarios(usuarios)
    print("✅ Usuário criado com sucesso!")

def listar_usuarios(usuarios):
    print("\n📋 Lista de usuários:")
    for u in usuarios.values():
        print(f"{u['id']} - {u['nome']} ({u['categoria']})")

def editar_usuario(usuarios):
    listar_usuarios(usuarios)
    uid = input("ID do usuário a editar: ")
    if uid in usuarios:
        nome = input("Novo nome: ")
        senha = input("Nova senha: ")
        categoria = input("Nova categoria: ")
        usuarios[uid] = {"id": uid, "nome": nome, "senha": senha, "categoria": categoria}
        salvar_usuarios(usuarios)
        print("✏️ Usuário atualizado.")
    else:
        print("❌ Usuário não encontrado.")

def remover_usuario(usuarios):
    listar_usuarios(usuarios)
    uid = input("ID do usuário a remover: ")
    if uid in usuarios:
        del usuarios[uid]
        salvar_usuarios(usuarios)
        print("🗑️ Usuário removido.")
    else:
        print("❌ Usuário não encontrado.")

# ==========================
# Funções de Produtos
# ==========================

def carregar_produtos():
    produtos = []
    try:
        with open("produtos.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for linha in reader:
                produtos.append(linha)
    except FileNotFoundError:
        pass
    return produtos

def salvar_produtos(produtos):
    with open("produtos.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "nome", "preco", "quantidade"])
        writer.writeheader()
        for p in produtos:
            writer.writerow(p)

def adicionar_produto(produtos):
    novo_id = str(len(produtos) + 1)
    nome = input("Nome do produto: ")
    preco = input("Preço: ")
    quantidade = input("Quantidade: ")
    produtos.append({"id": novo_id, "nome": nome, "preco": preco, "quantidade": quantidade})
    salvar_produtos(produtos)
    print("✅ Produto adicionado.")

def listar_produtos(produtos):
    print("\n📦 Produtos:")
    for p in produtos:
        print(f"{p['id']} - {p['nome']} | R${p['preco']} | Estoque: {p['quantidade']}")

def editar_produto(produtos):
    listar_produtos(produtos)
    pid = input("ID do produto a editar: ")
    for p in produtos:
        if p["id"] == pid:
            p["nome"] = input("Novo nome: ")
            p["preco"] = input("Novo preço: ")
            p["quantidade"] = input("Nova quantidade: ")
            salvar_produtos(produtos)
            print("✏️ Produto atualizado.")
            return
    print("❌ Produto não encontrado.")

def remover_produto(produtos):
    listar_produtos(produtos)
    pid = input("ID do produto a remover: ")
    produtos = [p for p in produtos if p["id"] != pid]
    salvar_produtos(produtos)
    print("🗑️ Produto removido.")
    return produtos

def buscar_produto(produtos):
    nome = input("Nome do produto: ").lower()
    encontrados = [p for p in produtos if p["nome"].lower() == nome]
    if encontrados:
        for p in encontrados:
            print(f"{p['id']} - {p['nome']} | R${p['preco']} | Estoque: {p['quantidade']}")
    else:
        print("❌ Produto não encontrado.")

def ordenar_por_nome(produtos):
    ordenados = sorted(produtos, key=lambda x: x["nome"].lower())
    listar_produtos(ordenados)

def ordenar_por_preco(produtos):
    ordenados = sorted(produtos, key=lambda x: float(x["preco"]))
    listar_produtos(ordenados)

# ==========================
# Login e Menus
# ==========================

def login(usuarios):
    print("\n🔐 Login")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    for u in usuarios.values():
        if u["nome"] == usuario and u["senha"] == senha:
            print(f"✅ Bem-vindo, {usuario}!")
            return u["categoria"]
    print("❌ Credenciais inválidas.")
    return None

def menu_gerente(usuarios, produtos):
    while True:
        print("\n📋 Menu Gerente")
        print("1. Criar usuário")
        print("2. Listar usuários")
        print("3. Editar usuário")
        print("4. Remover usuário")
        print("5. Adicionar produto")
        print("6. Listar produtos")
        print("7. Editar produto")
        print("8. Remover produto")
        print("9. Buscar produto")
        print("10. Ordenar produtos por nome")
        print("11. Ordenar produtos por preço")
        print("0. Sair")
        op = input("Opção: ")
        if op == "1":
            criar_usuario(usuarios)
        elif op == "2":
            listar_usuarios(usuarios)
        elif op == "3":
            editar_usuario(usuarios)
        elif op == "4":
            remover_usuario(usuarios)
        elif op == "5":
            adicionar_produto(produtos)
        elif op == "6":
            listar_produtos(produtos)
        elif op == "7":
            editar_produto(produtos)
        elif op == "8":
            produtos = remover_produto(produtos)
        elif op == "9":
            buscar_produto(produtos)
        elif op == "10":
            ordenar_por_nome(produtos)
        elif op == "11":
            ordenar_por_preco(produtos)
        elif op == "0":
            break
        else:
            print("⚠️ Opção inválida.")

def menu_funcionario(produtos):
    while True:
        print("\n📋 Menu Funcionário")
        print("1. Listar produtos")
        print("2. Buscar produto")
        print("3. Ordenar por nome")
        print("4. Ordenar por preço")
        print("0. Sair")
        op = input("Opção: ")
        if op == "1":
            listar_produtos(produtos)
        elif op == "2":
            buscar_produto(produtos)
        elif op == "3":
            ordenar_por_nome(produtos)
        elif op == "4":
            ordenar_por_preco(produtos)
        elif op == "0":
            break
        else:
            print("⚠️ Opção inválida.")

# ==========================
# Execução principal
# ==========================

def main():
    usuarios = carregar_usuarios()
    produtos = carregar_produtos()

    print("🛠️ Sistema de Gerência - Trabalho Prático")
    categoria = login(usuarios)

    if categoria == "gerente":
        menu_gerente(usuarios, produtos)
    elif categoria in ["funcionario", "estagiario"]:
        menu_funcionario(produtos)
    else:
        print("🚫 Acesso negado.")

if __name__ == "__main__":
    main()