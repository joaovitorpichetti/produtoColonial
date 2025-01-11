
# Sistema de Vendas de Produtos Coloniais

## Introdução

Este projeto tem como objetivo conectar pequenos produtores da Serra Gaúcha a clientes, oferecendo uma plataforma intuitiva para compra e venda de produtos coloniais. O sistema permite o cadastro e gestão de produtos, clientes, além da geração de pedidos de produção, tudo de maneira eficiente e fácil de usar.

Desenvolvido utilizando Django, Bootstrap, CSS e Python, esta aplicação web oferece uma experiência moderna e prática tanto para produtores quanto para consumidores.

---

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Framework:** Django
- **Banco de Dados:** SQLite3
- **IDE Sugerida:** PyCharm
- **Controle de Versão:** Git

---

## Estrutura do Projeto

O projeto segue o padrão **MTV (Model-Template-View)** do Django, onde a estrutura de pacotes é organizada da seguinte forma:

- **`produtoColonial/`**: Diretório que contém as configurações globais do projeto Django.
- **`produtosColoniais/`**: Aplicação principal, onde estão os modelos, views e templates.
- **`static/`**: Diretório para arquivos estáticos, como CSS, imagens e JavaScript.
- **`templates/`**: Arquivos HTML utilizados na renderização das páginas.
- **`manage.py`**: Script principal para comandos administrativos no Django.

---

## Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto localmente:

1. **Clone o repositório para sua máquina local**:
   ```bash
   git clone https://github.com/joaovitorpichetti/produtoColonial.git
   cd produtoColonial
   ```

2. **Instale as dependências do projeto**:
   ```bash
   pip install -r requirements.txt
   ```
   Este comando instala todas as bibliotecas e pacotes necessários listados no arquivo `requirements.txt`.

3. **Crie as migrações para o banco de dados**:
   ```bash
   python manage.py makemigrations
   ```
   Este comando gera os arquivos de migração com base nos modelos definidos, preparando-os para serem aplicados ao banco de dados.

4. **Aplique as migrações**:
   ```bash
   python manage.py migrate
   ```
   Este comando executa as migrações, criando as tabelas e estruturas necessárias no banco de dados SQLite.

5. **Crie um superusuário (administrador)**:
   ```bash
   python manage.py createsuperuser
   ```
   Este comando cria um usuário administrador para acessar o painel de administração do Django. Insira as informações solicitadas, como nome de usuário, e-mail e senha.

6. **Inicie o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
   ```
   Este comando inicia o servidor local do Django. Você pode acessar o sistema pelo navegador no endereço: [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias, correções ou novas funcionalidades.

---

## Licença

Este projeto está licenciado sob a licença [MIT](LICENSE). Consulte o arquivo LICENSE para mais detalhes.

---

Se precisar de ajuda ou tiver dúvidas, entre em contato com o mantenedor do projeto.

