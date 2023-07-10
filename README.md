Inicia as variáveis saldo, deposito, HDdepositos (histórico de depósitos) e HDsaques (histórico de saques) com valores iniciais.
Entra em um loop infinito usando while True.
Exibe um menu de opções para o usuário: Depósito, Saque, Extrato e Sair.
Com base na escolha do usuário, executa o código correspondente a cada opção selecionada.
Se a opção for Depósito:
Solicita ao usuário o valor do depósito.
Verifica se o valor do depósito é válido (maior ou igual a 1).
Solicita ao usuário a confirmação do valor do depósito.
Se a confirmação for positiva, atualiza o saldo, registra o depósito no histórico de depósitos e exibe uma mensagem de sucesso.
Se a confirmação for negativa, exibe uma mensagem de cancelamento.
Se a opção for Saque:
Solicita ao usuário o valor do saque.
Obtém a data atual.
Verifica quantos saques foram realizados na data atual.
Se o número de saques for menor que o limite diário, verifica se o valor do saque é válido (entre 1 e 500) e se há saldo suficiente.
Se as condições forem atendidas, atualiza o saldo, registra o saque no histórico de saques e incrementa o número de saques realizados na data atual.
Se o número de saques atingir o limite diário, exibe uma mensagem informando o limite atingido.
Se a opção for Extrato:
Exibe o histórico de depósitos, histórico de saques e saldo atual.
Se a opção for Sair, o programa é encerrado.
Se a opção não for válida, exibe uma mensagem de erro.
O código inclui verificações para garantir que os valores inseridos pelo usuário sejam válidos e realiza as operações correspondentes com base nas escolhas feitas.
