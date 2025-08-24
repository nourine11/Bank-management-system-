class Node:
    def __init__(self):
        self.next = None  #self: لازم نستخدنها عشان نوصل لاى دالة
        # عشان نشوف الحاجات اللى فى الدالة
        self.prev = None
        self.name = None       # هنعمل النود 
        self.id = None
        self.password = None
        self.balance = 0
        self.limit = 0


class Bank:
    def __init__(self):
        self.head = None     
        self.id = 2000

    def is_empty(self):
        return self.head is None # هنشوف لو ال head=None يبقى مقيش ليستة

    def create_account(self, name, password, limit, balance):
        new_node = Node()
        new_node.name = name
        new_node.password = password 
        new_node.balance = balance
        new_node.limit = limit
        new_node.id = self.id + 1
        self.id += 1

        if self.is_empty():
            new_node.prev = None
            new_node.next = None
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node

        print(f"A new account has been created for {new_node.name}.\n"
              f"Balance: {new_node.balance} $\n"
              f"Monthly limit: {new_node.limit} $\n"
              f"ID: {new_node.id}\n")
        return

    def display(self):
        if self.is_empty():
            print("There are no accounts to display.")
            return

        temp = self.head
        while temp:
            print(f"Account Information:\n"
                  f"Account Name: {temp.name}\n"
                  f"Account ID: {temp.id}\n"
                  f"Account Balance: {temp.balance} $\n")
            temp = temp.next

    def delete_account(self, id, password):
        if self.is_empty():
            print("There are no accounts to delete.")
            return

        temp = self.head
        while temp and temp.id != id:
            temp = temp.next

        if not temp:
            print("This account does not exist.")
            return

        if temp.password != password:
            print("Wrong password.")
            return

        if temp == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            if temp.prev:
                temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev

        print(f"{temp.name}'s account has been deleted.\n")
        return

    def transfer(self, sender_id, sender_pass, receiver_id, amount):
        if self.is_empty():
            print("There are no accounts.")
            return

        sender = None
        receiver = None
        temp = self.head

        while temp:
            if temp.id == sender_id:
                if temp.password == sender_pass:
                    sender = temp
                else:
                    print("Wrong password for sender.")
                    return
            if temp.id == receiver_id:
                receiver = temp
            temp = temp.next

        if not sender:
            print("Sender account not found.")
            return
        if not receiver:
            print("Receiver account not found.")
            return
        if sender.balance < amount:
            print("Insufficient balance.")
            return

        sender.balance -= amount
        receiver.balance += amount
        print(f"Transaction from {sender.name} to {receiver.name} of {amount} $ completed.\n")
        return

    def change_password(self, id, old_password):
        if self.is_empty():
            print("There are no accounts.")
            return

        temp = self.head
        while temp:
            if temp.id == id:
                if temp.password == old_password:
                    new_password = input("Enter your new password: ")
                    temp.password = new_password
                    print("Your password has been updated successfully.")
                    return
                else:
                    print("Your old password is incorrect.")
                    return
            temp = temp.next

        print("Account ID not found.")
        return

    def purchase(self, id, password, value):
        if self.is_empty():
            print("There are no accounts.")
            return

        temp = self.head
        while temp:
            if temp.id == id and temp.password == password:
                if value > temp.limit:
                    print(f"Your daily limit is {temp.limit} $, you cannot purchase this item.")
                    return
                if temp.balance < value:
                    print("Insufficient balance for this purchase.")
                    return
                temp.balance -= value
                print(f"Purchase successful. Remaining balance: {temp.balance} $.\n")
                return
            temp = temp.next

        print("Account not found or incorrect credentials.")
        return

    def withdraw(self, id, password, value):
        if self.is_empty():
            print("There are no accounts.")
            return

        temp = self.head
        while temp:
            if temp.id == id:
                if temp.password == password:
                    if temp.balance - value < 500:
                        print("Withdrawal not allowed. Minimum balance of 500 $ required.")
                        return
                    temp.balance -= value
                    print(f"{value} $ has been withdrawn from your account.\n"
                          f"New balance: {temp.balance} $\n")
                    return
                else:
                    print("Wrong password.")
                    return
            temp = temp.next

        print("Account not found.")
        return

    def deposit(self, id, password, value):
        if self.is_empty():
            print("There are no accounts.")
            return

        temp = self.head
        while temp:
            if temp.id == id:
                if temp.password == password:
                    temp.balance += value
                    print(f"{value} $ has been added to your account.\n"
                          f"New balance: {temp.balance} $\n")
                    return
                else:
                    print("Wrong password.")
                    return
            temp = temp.next

        print("Account not found.")
        return

    def search(self, id, password):
        if self.is_empty():
            print("There are no accounts.")
            return

        temp = self.head
        while temp:
            if temp.id == id:
                if temp.password == password:
                    print(f"Account Information:\n"
                          f"Account Name: {temp.name}\n"
                          f"Account ID: {temp.id}\n"
                          f"Account Balance: {temp.balance} $\n")
                    return
                else:
                    print("Wrong password.")
                    return
            temp = temp.next

        print("Account not found.")
        return
