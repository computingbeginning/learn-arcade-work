class Person():
    def __init__(self):
        self.name = ""


class Employee(Person):

    def __init__(self):
        # Call the parent/super class constructor first
        super().__init__()

        # Now set up our variables
        self.job_title = ""


class Customer(Person):

    def __init__(self):
        super().__init__()
        self.email = ""


def main():
    john_smith = Person()
    john_smith.name = "John Smith"

    jane_employee = Employee()
    jane_employee.name = "Jane Employee"
    jane_employee.job_title = "Web Developer"

    bob_customer = Customer()
    bob_customer.name = "Bob Customer"
    bob_customer.email = "send_me@spam.com"


main()
