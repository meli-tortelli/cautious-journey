client = input("Digite o nome do cliente:")
due_date = input("Digite o dia de vencimento: ")
due_month = input("Digite o mês de vencimento: ")
invoice = input("Digite o valor da fatura: ")

print(
    f"Olá, {client}\nA sua fatura com vencimento em {due_date} de {due_month} no valor de R$ {invoice} está fechada."
)
