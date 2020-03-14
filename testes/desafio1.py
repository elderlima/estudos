def saque(a):
   saldo = 50
   transacao = a + 5
   if transacao >= saldo:
       return("Valor Indisponivel\nSeu saldo é de R$ %s" % saldo)
   else:
       saldo = saldo - transacao
       print("\nSaque: - R$ %s" % a)
       print("Taxa de Serviço - R$ 5,00\n")
       print("Total do saque R$ %s \n" % transacao)
       return("Saque efetuado com sucesso\n\nSeu saldo atual é de R$ %s" % saldo)

def deposito(b):
   saldo = 50
   transacao = b - 5
   if b <= 5:
       return("O deposito precisa ser acima da taxa de R$ 5,00\nSeu saldo atual é de R$ %s" % saldo)
   else:
       saldo = transacao + saldo
       print("\n+ R$ %s" % b)
       print("- R$ 5,00\n")
       print("Total do deposito R$ %s \n" % transacao)
       return("Deposito efetuado com sucesso\n\nSeu saldo é R$%s" % saldo)


saldo = 50
#continuar = 1

#while continuar == 2:
#    print("Operação encerrada")
#else:
    print("Saldo Atual: R$ %s" % saldo)
    opcao = int(input("\nEscolha a função desejada:\
        \n\
        \n1 - Saque\
        \n2 - Deposito\
        \n\
        \nA taxa para deposito ou Saque é de R$5,00\
        \n\
        \nOpção: "))

    if opcao > 2:
        print("Opção Incorreta, por favor, digitar uma das opcoes listadas")
    elif opcao == 1:
        valor = int(input("\nInformar valor do Saque: R$ "))
        print(saque(valor))
    elif opcao == 2:
        valor = int(input("\nInformar valor do Deposito: R$ "))
        print(deposito(valor))
#continuar = int(input("\nDeseja Continuar\
#    \n1 - Sim\
#    \n2 - Não\
#    \nR: "))