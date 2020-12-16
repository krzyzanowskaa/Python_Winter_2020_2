class Customer:
    last_id = 0
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Customer.last_id += 1
        self.customer_id = Customer.last_id

    def __repr__(self):
        return self.__class__.__name__ + "(" + str(self.customer_id) + "): " + self.first_name + " " + self.last_name + " (" + self.email + ")"


class Account:
    last_id = 0
    def __init__(self, customer):
        self.customer = customer
        self._balance = 0
        self.interest_rate = 0.05
        Account.last_id += 1
        self.account_id = Account.last_id

    def deposit(self, amount):
        if amount <= 1000:
            self._balance += amount
            print("Deposited: " + str(amount) + ". The new balance is: " + str(self._balance))
        else: print("Max deposit amount is 1 000.")

    def charge(self, pincode, amount):
        if pincode == 1234:
            if self._balance >= amount:
                self._balance -= amount
                print("Charged: " + str(amount) + ". The new balance is: " + str(self._balance))
            else:
                print("Sorry, you do not have that much money on your account to withdraw: " + amount)
        else: print("Pin code incorrect, try again.")


    def calc_interest(self, interest_rate, time):
        #TODO - add implementation based on self.interest_rate
        self.interest_rate = interest_rate
        self.time = time
        interest = (self._balance * self.interest_rate * self.time)/100
        total_balance = self._balance + interest

        print("The interest after " + str(time) + " month(s) is: " + str(interest) + ". Total account balance is: " + str(total_balance))
        return interest


    def get_balance(self):
        print("The balance is: " + self._balance)
        return self._balance

    def __repr__(self):
        return "{0} ({1}): {2} belonging to: {3} {4} ".format(self.__class__.__name__, self.account_id, self._balance, self.customer.first_name, self.customer.last_name)
        #return self.__class__.__name__ + "(" +  + ")" + " belonging to: " + self.customer.first_name + " " + self.customer.last_name  + " (" + self.customer.email + ")"

class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def create_customer(self, first_name, last_name, email):
        c = Customer(first_name, last_name, email)
        self.customers.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.accounts.append(a)
        return a

    def transfer(self, acc_id_from, acc_id_to, amount):
        # TODO - implement it (input parameters are account ids)
        pass

    def __repr__(self):
        return 'Bank(cust: {0}, acc: {1})'.format(self.customers, self.accounts)


bank = Bank()

c1 = bank.create_customer("Jan", "Kowalski", "j.kowalski@gmail.com")
print(c1)
a1 = bank.create_account(c1)
print(a1)
a1.deposit(300)
a1.charge(1234, 100)
a1.calc_interest(0.08, 12)
print(bank)