transactions = [1200, -500, 3000, -800, 4500, -200, 700]

def bank_transaction_analyzer(transactions):
    
    def add_cashback(amount):
        return amount + (amount * 0.10)

    credits = list(filter(lambda x: x > 0, transactions))
    debits = list(filter(lambda x: x < 0, transactions))

    credits_after_cashback = list(
        map(lambda x: add_cashback(x) if x > 2000 else x, credits)
    )

    print("===== BANK TRANSACTION REPORT =====\n")
    print("Credit Transactions:")
    print(credits)
    print("\nDebit Transactions:")
    print(debits)
    print("\nCredits After Cashback:")
    print(credits_after_cashback)

bank_transaction_analyzer(transactions)