"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(
        self,
        first_name,
        last_name,
        email,
        password,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hashed_password = hash(password)

    def __repr__(self):
        """Convenience method to show information about customer in console."""
        return(
            f"<Customer: {self.first_name}, {self.last_name}, {self.email}, {self.password}>"
        )    
    
    def is_correct_password(self, password):
        """Check if password is correct password for this customer.

        Compare the hash of password to the stored hash of the
        original password.
        """

        return password == self.hashed_password

def read_customer_info_from_file(filepath):
    """Create dictionary from customer info text file"""

    cx_info = {}

    with open(filepath) as file:
        for line in file:
            (
                first_name,
                last_name,
                email,
                password,
            ) = line.strip().split("|")

            cx_info[email] = Customer(
                first_name,
                last_name,
                email,
                password,
            )
    
    return cx_info

def get_by_email(email):

    if email not in cx_info:
        return 0
    return cx_info[email]


cx_info = read_customer_info_from_file("customers.txt")