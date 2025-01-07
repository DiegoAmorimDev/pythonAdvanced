# Guia de Uso do Git para Controle de Versão

Este guia descreve as etapas para configurar um repositório Git, realizar alterações, e trabalhar com branches no GitHub.

---

## INÍCIO

Siga as etapas abaixo para inicializar um repositório Git e fazer o primeiro commit:

1. Inicialize um novo repositório Git:
   ```bash
   git init
   ```

2. Adicione todos os arquivos ao estágio (stage):
   ```bash
   git add .
   ```

3. Faça o primeiro commit:
   ```bash
   git commit -m "primeiro commit"
   ```

4. Renomeie a branch principal para `main`:
   ```bash
   git branch -M main
   ```

5. Conecte o repositório local ao remoto:
   ```bash
   git remote add origin <link>
   ```

6. Envie o código para o repositório remoto:
   ```bash
   git push -u origin main
   ```

---

## PARA FAZER ALTERAÇÃO

Sempre que você fizer alterações nos arquivos e desejar enviá-las para o repositório remoto, siga os passos abaixo:

1. Verifique o status do repositório para identificar os arquivos alterados:
   ```bash
   git status
   ```

2. Adicione todos os arquivos modificados ao estágio:
   ```bash
   git add .
   ```

3. Envie as alterações para o repositório remoto:
   ```bash
   git push origin main
   ```

---

## CRIANDO UMA BRANCH

Para criar uma nova branch e trabalhar nela, siga as etapas abaixo:

1. Crie e troque para uma nova branch chamada `testes`:
   ```bash
   git checkout -b "testes"
   ```

2. Verifique o status da branch atual:
   ```bash
   git status
   ```

3. Adicione todos os arquivos alterados ao estágio:
   ```bash
   git add .
   ```

4. Faça um commit com as alterações:
   ```bash
   git commit -m "commit"
   ```

5. Envie a branch para o repositório remoto:
   ```bash
   git push origin testes
   ```

---

## ATUALIZANDO DADOS DO REPOSITÓRIO LOCAL

1. Verifique se está na branch que quer, por exemplo main
   ```bash
   git status
   ```

2. Dê o comando git pull para puxar os dados do rep remoto para o local
   ```bash
   git puull
   ```

## Observações

- **Não esqueça de substituir `<link>` pelo link do repositório remoto ao executar o comando `git remote add origin`.**
- Sempre revise o status (`git status`) para evitar enviar arquivos indesejados para o repositório remoto.
- Quando terminar de trabalhar em uma branch, você pode integrá-la à branch principal (`main`) com o comando `git merge`.

---

### Contato

Para dúvidas ou sugestões, entre em contato pelo [seu email ou link para redes sociais].
