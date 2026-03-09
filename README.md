# 💘 Dating App – Projeto Full Stack (Angular + .NET)

Um aplicativo de namoro full-stack construída com Angular (frontend) e .NET (backend).
Este projeto foi criado como parte de portfólio para demonstrar arquitetura de aplicações do mundo real, autenticação, upload de arquivos e implementação de regras de negócio.

## 🚀 Features

- Registro e autenticação de usuários (JWT)
- Criação e edição de perfil
- Upload de fotos
- Sistema de likes
- Detecção de match
- Mensagens em tempo real (se implementado posteriormente)

## 🔐 Fluxo de Autenticação

1. O usuário faz login com email e senha.
2. O backend valida as credenciais.
3. Um token JWT é gerado.
4. O Angular armazena o token.
5. Um HTTP Interceptor anexa o token às requisições protegidas.

## ⚙️ Executando o Projeto

### Backend
1. Navegue até a pasta da API
2. Execute:
   dotnet run

### Frontend
1. Navegue até a pasta client
2. Execute:
   2.1: npm install
   2.2: ng serve

## 📝 Registro
1. Na página inicial, clique no botão de registro:

![Register screen](images/register.png)

2. Agora você precisa inserir suas credenciais: email, nome de exibição, senha, confirmar senha e então clicar em Next:

![Credentials screen](images/register_2.png)

3. Agora defina as informações do seu perfil, como data de nascimento e localização (lembre-se de que você precisa ter mais de 18 anos), e então clique em Register:

![Profile screen](images/register_3.png)

## 👤 Configurando seu perfil

1. Agora que você já é um usuário, clique na sua foto de perfil no canto superior direito e depois clique em Edit profile:

![Profile screen](images/edit_profile.png)

2. Na página do seu perfil, clique em Edit para enviar uma nova imagem. Você pode arrastar uma nova imagem de qualquer lugar e então verá a seguinte tela, onde poderá clicar no botão Upload image:

![Profile screen](images/upload_photo.png)

3. Agora você terá uma nova foto no seu perfil e, como esta foto é a primeira foto upada, ela será automaticamente definida como foto principal do perfil, assim:

![Profile screen](images/profile_updated.png)
Você pode adicionar quantas imagens quiser usando o botão Edit.

## 💘 Matching

1. Agora que você tem um bom perfil, volte para a página de matches e encontre um perfil que você goste. Você pode curtir esse perfil usando o ícone de coração:

![Profile screen](images/like.png)
Neste exemplo, eu curti o perfil da Lisa, então o ícone de coração dela ficou vermelho. Posso clicar novamente no ícone de coração para desfazer essa ação.

2. Você pode ir para a página de listas e encontrar os usuários que você curtiu até agora, assim como os usuários que curtiram você:

![Profile screen](images/like_2.png)

## ⚠️ Observações importantes:

1. Esta aplicação ainda está em desenvolvimento
2. Uma futura funcionalidade de mensagens está atualmente em desenvolvimento
3. Esta aplicação será publicada quando estiver 100% completa
4. Quando publicada, também terá uma versão em Português do Brasil
