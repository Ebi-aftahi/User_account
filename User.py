class User:
    def __init__(self, acc_num, cust_name, acc_type="01-Deposit", balance= 0.0):
        self.acc_num = acc_num
        self.cust_name = cust_name
        self.acc_type = acc_type
        self.balance = balance

    def make_deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            print("Deposit Successful!")
        else:
            print("Error: Invalid Amount!")


    def make_withdrawal(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print("Withdrawal Successful!")
        else:
            print(f"Error!: Not enough money in Acc#:{self.acc_num}") 

    def display_user_balance(self):
        print("Acc#: {}\n Account Type: {}\n Customer Name: {}\n balance: ${:,.2f}\n"
        .format(self.acc_num,self.acc_type,self.cust_name,self.balance))
    

    def transfer_money(self, other_user, amount):
        print("Transferring ${:,.2f} from Account# {} to Account# {}"
        .format(amount, self.acc_num, other_user.acc_num))
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        print("Money transfer Done!")
        
########################################
print("Making two instances...")
acc1 = User("12345C001", "Dr. XXXX", "02-Checking")
acc1.display_user_balance()

acc2 = User("12345D002", "Dr. YYYY", "01-Deposit" ,1000.58)
acc2.display_user_balance()

print("Making deposit to Acc1...")
acc1.make_deposit(1000.00)

print("Display Acc1...")
acc1.display_user_balance()

print("Making withdraw from Acc2...")
acc2.make_withdrawal(500.58)

print("Display Acc2...")
acc2.display_user_balance()

print("Transfer from Acc1 to Acc2...")
acc1.transfer_money(acc2, 500.00)

print("Display Accounts after Transfer...")
acc1.display_user_balance()
acc2.display_user_balance()


