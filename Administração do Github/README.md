# Introdução aos Conceitos de Git Hub

## Princípios do Git e GitHub

Vamos aprender sobre Git, GitHub, colaboração de código, focando em facilitar processos para guardar códigos e construção de histórias.

Trabalhar com versionamento de código. 

### O que é Git e Github

Git: possiblita ter um controle melhor e organizado de versões do software. Traz um sistema que altere, gerencie as versões do nosso código. Como funciona a colaboração e como.

Github: Uma plataforma online que serve cmo repositório para guardar todos os nossos códigos fontes, como foco também no trabalho colaborativo. Plataforma online para comportar o nosso código.


### Como ambos se relacionam

- Hospedagem de repositórios: gerencia controle de versões e hospeda repositórios git remotamente.
- Colaboração em Equipe: Possiblita colaboração em equipe, varios desenvolvedores atuando em colaboração no mesmo projeto.
- Rastramento de Problemas e Projetos: Ferramentas para reasrear problemas, gerenciar integrações, além de controle de versão
- Forks e Branches: Isolar desenvolvimento de novos crecursos ou construçaõ de bugs.

### Instalação Git

Passo a passo para instalação

Download: [Download GIT](https://git-scm.com/downloads)
- Processo de instalação simples, next, next finish. 
- Adicionar o gitBash

Git bash vai ser a principal ferramente que vamos utilizar. "Terminal do Git"

Configuração:
- Atribuir nome
    - configuração: git config --global "wsilva"
- Atribuir e-mail
    - git config --global user.mail "*****@gmail.com"


### Criando conta no Git:

Processo de instalação:
- Ir para a página do git: [GIT](https://github.com/)
    - Inscrever-se
    - e-mail
    - senha
    - nome de usuário
    - Colocar o dódigo de verificacao
    - Conta pronta

### Princiapais comandos do Git


- git init 
    - inicia um novo respositório Git no diretório atual
- git clone [URL]
    - Clona um respositório do Git hub
- git add .
    - adicionar as alterações para peraparalas para commit
- git commit -m "mensagem"
    - Realiza o commit com as alterações adiconadas, incluindo uma mensagem que descreve as alterações feitas. 
- git status
    - Exibe o estado atual do repositorio, mostrando alterações pendentes e ja adicionadas
- git log
    - Mostra o historico de commits do repositório
- git branch
    - Lista todas as branch's
- git branch [nome-da-branch]
    - Cria uma nova branch
- git chackout [nome-da-branch]
    - Altera para uma branch específica
- git pull
    - Atualiza o respositório local com as alterações
- git push [remote][branch]
    - Envia os commits locasi para o repositório remoto.
- git remote -v
    - Lista os repositórios remotos configurados
- git fetch
    - Recupera as ultimas alterações do repositório, mas não faz merge automáticamente
- git reset
    - Desfaz as alterações no arquivo especifico, removendo-o do indice
- git rm [arquivo]
    - Remove um arquivo do repositório e inclui no próximo commit
- git diff
    - Mostra as diferenças entre as alterações que ainda não foram adicionadas ao indice
- git remote add [nome-remoto][URL]
    - adicionar um repositorio remoto com um nome especifico.
- git push add origin main
    - Execuando para efetuar push das alterações locais para o repositório online. 

### Questionário

Como interagir com comunidades de código aberto no GitHub?
Apenas enviando sugestões por e-mail.
Envolva-se em discussões em issues, participe de pull requests e contribua para projetos abertos.
Ignorando discussões existentes.
Limitando-se a apenas observar repositórios.
Criando repositórios privados.

Como fazer e acompanhar alterações no código usando Git?
git save guarda instantâneos das alterações.
git push envia alterações para o repositório remoto.
git track monitora automaticamente todas as mudanças.
git add para preparar alterações, git commit para confirmá-las e git log para exibir o histórico.
git show exibe apenas alterações não confirmadas.

Como criar um novo projeto Git e configurá-lo?
Utilize git new para iniciar um repositório.
Crie um novo projeto com git create.
Execute git start para começar um novo projeto.
Inicie um projeto com git setup.
Use "git init" para iniciar repositório e configure com "git config".

Quais são os recursos fundamentais do GitHub?
Histórico de atividades.
Templates e plugins.
Documentação e tutoriais.
Ferramentas de edição de código.
Repositórios, issues, pull requests, branches e colaboradores.

O que é controle de versão?
Um método para compactar documentos.
Um sistema de organização de pastas.
Registro de alterações em arquivos ao longo do tempo.
Um software para editar código.
Uma técnica para backup de arquivos.

O que são sistemas de controle de versão distribuídos, como Git?
São sistemas que não permitem rastrear alterações.
São sistemas sem a capacidade de ramificação.
São sistemas que permitem a colaboração em projetos através de cópias locais completas do repositório.
São sistemas exclusivos para grandes empresas.
São sistemas que funcionam apenas com conexão à internet.

## Autenticações 

### Nome e senha, Token e SSH


Tipos de autenticações para acessar os projetos
- Usuario e Senha
- tokens de acesso pessoal
- chaves SSH

### Chaves de implementação, SSO da SAML e LPDA

Chaves de Implementação: Chaves de implementação são como chaves especiais que permitem acesso a apenas um lugar específico no GitHub. Esa chave somente da permissão de leitura. Para algo diferente, deve ser configurado a chave para dar acesso a escrita.

Autenticação de dois fatores - SFA: É adicionar uma camada extra de segurança quanvo cê entra em sistes ou aplicativos além de mais uma prova de autenticação, sendo este um código adicional.

SSO do SAML:  é uma forma segura do GITHUB que permite constrolar os acesso da organização de maneira centralizada. São direcionados para acesso através de um login de um controle de LDAP.

LDPA: Protocolo usado para acessar e organizar informações em diretórios em grandes empresas. No contexto Enterprise Server é permitido integrar e gerenciar centralmente o acesso aos repositórios usando contas existentes. É compativel com vários serviços LDAP. 

### Nome e Senha e Token - Parte Prática 1

Primeiramente vamos acessa a nossa conta do Git
Vamos fazer um repositório de um projeto para testes

Primeiramente criamos um repositório: meu-repositorio-de-autenticacoes, colocamos descrição simples e marcamos o reade.me

Configuramos o nosso usuário e senha no git:

Configuração:
- Atribuir nome
    - configuração: git config --global "wsilva"
- Atribuir e-mail
    - git config --global user.mail "*****@gmail.com"
- Ver as configurações do git
    - git config --list

Agora vamos clonar o repositório que criamos e vamos clonar ele: "https://github.com/Wastiel/meu-respositorio-de-autenticacoes.git"

Utilizamos o comando "git clone https://github.com/Wastiel/meu-respositorio-de-autenticacoes.git", para puxar o nosso repositório.

Primeiro erro que enfrentamos é tentarmos adicionar coisas ao nosso reposiotorio, temos o err "fatal: not a git repository (or any of the parent directories): .git". Isto ocorre por que quando clonamos o repositório não caimos dentro do mesmo diretório.

Entramos dentro do diretório com o comando "cd" do linux.

git add .: adicionamos dados para preparar o commit
git. commit -m "mensagem": executamos a confirmação dos dados que irão para o nosso respositório
git push -u origin main: Mandamos as alterações para o nosso repositório.

Ao adicionarmos o comando anterior, nos é solicitado usuário e senha.
    - Este Usuáro e senha, ficam salvos dentro do gerenciador de senhas do windows

- Podemos criar tamém um token. Para isto vamos dentro de:
    - Perfil
    - Settings
    - <> Developer settings
    - colocamos tempos de expiração
    - Configurações de projetos
    - Posterior é nos gerado o token

Ao solicitar a autenticação no momento que subirmos as alterações, vamos adicionar o nosso token ao invés de usuário e senha. 

### SSH - Parte prática 2

Autenticação via chave de SSH, onde conseguimos utilizar multplas contas no nosso computador.

ssh-keygen: comando para gerar a nossa chave ssh

Ao criarmos a chave ssh, vamos no diretório criado a chave, entramos com o git bach e adicioanrmos a chamave publica no github.

cat id_***.pub, onde verificamos a chava publica.
Posteiror vamos no nosso git , vamos em settings, Chaves SSh e GPG e ali dentro colocamos esta determinada chave. 

Pegamos a chave do ssh do repositório e setamos a url:
    - git remote set-url origin **chave SSH**

### 2FA - Parte prática 3

Autenticação em 2 fatores

Entramos em Setting - Password nad authentication.
Duas formas de autenticação, via QR Code ou via sms, por um numero que esteja funcionando.

Vai ser gerado alguns tokens de segurança. Deve ser feito download do mesmo e salvo em um lugar super seguro. 

### Questionario: 

Como você pode habilitar a autenticação de dois fatores no GitHub?
Alterando sua foto de perfil.
Através das configurações de segurança da sua conta.
Enviando um e-mail para o suporte do GitHub.
Atualizando seu navegador.
Instalando um aplicativo de terceiros.

Como as chaves SSH tornam as interações com o GitHub mais seguras e convenientes?
Configurando Chaves de Implementação.
Permitindo conexões seguras a computadores remotos sem digitar senha ou token.
Utilizando Tokens de Acesso Pessoal (PATs).
Ativando a 2FA.
Integrando LDAP.

Como você pode adicionar uma camada extra de segurança ao acessar sua conta do GitHub, além de usar nome de usuário e senha?
Ativando a Autenticação de Dois Fatores (2FA)
Configurando Chaves SSH
Utilizando Tokens de Acesso Pessoal (PATs)
Integrando SSO do SAML
Implementando LDAP

Qual é a atual medida adicional de segurança implementada no GitHub para dificultar o acesso não autorizado?
SSO do SAML
Autenticação de Dois Fatores (2FA)
Configurando LDAP
Chaves de Implementação
Utilizando Tokens de Acesso Pessoal (PATs)













