from constants import AccountType, ClientType
from models import Bank, CreditAccount, DepositAccount, Client


def main():
    bank = Bank("All world money")
    bank2 = Bank("Mono")
    client1 = Client(name="Alex", client_type=ClientType.PERSON)
    # bank.open_account(client1, account_type=AccountType.DEBIT_CARD)
    # bank.open_account(client1, account_type=AccountType.MORTGAGE)
    bank2.open_account(client1, account_type=AccountType.MORTGAGE)

    client_legal = Client(name="Brabus CORP", client_type=ClientType.LEGAL)
    bank.open_account(client_legal, account_type=AccountType.CREDIT)

    # da = DepositAccount(AccountType.CURRENT, client)
    # ca = CreditAccount(AccountType.CREDIT, client)
    client_legal.accounts[0]

    print(bank <= bank2)
    pass


if __name__ == "__main__":
    main()
