import uuid
from abc import ABCMeta, abstractmethod
from functools import wraps


class Bank(object):
    """Class representing a bank. It has operations that a bank would allow a user to do.

    Attributes:
        user_accounts: stores account info mapped to a user object
    """

    class User(object):
        """Class representing a user of the bank. Since it is specific to the bank, it is nested inside the Bank class.
        It is immutable so that it can be used as a key for the dictionary containing the accounts.

        Attributes:
            name: Name of the user
            id: Unique id of the user accoun
        """

        def __init__(self, name):
            self._name = name
            self._id = uuid.uuid1()

        @property
        def id(self):
            return self._id

        @property
        def name(self):
            return self._name

        def __hash__(self):
            return hash((self._name, self._id))

        def __eq__(self, other):
            return self.id == other.id

        def __ne__(self, other):
            return self == other

    def __init__(self):
        self._user_accounts = {}

    def create_user(self, name):
        return self.User(name)

    def create_account(self, account_cls, user, *args):
        """Creates an *account_cls* instance for *user*. Boolean return indicates success."""
        if account_cls not in Account.__subclasses__():
            raise ValueError("*account_cls* must be a direct subclass of Account class.")

        if user not in self._user_accounts:
            self._user_accounts[user] = {}
        # Account of this type already exists for this user
        elif account_cls.__name__ in self._user_accounts[user]:
            return False

        self._user_accounts[user][account_cls.__name__] = account_cls(user.id, *args)
        return True

    def close_account(self, account):
        """Tries to close *account*, which deletes its entry in self._user_accounts. Boolean return indicates success"""
        if account is None:
            raise TypeError("*account* is None. Must be an instance of a subclass of Account class")
        elif not isinstance(account, Account):
            raise TypeError("*account* is not an instance of Account.")

        account_type = type(account).__name__

        for user in self._user_accounts.keys():
            if user.id == account.user_id and self._user_accounts[user].get(account_type, None) == account:
                del self._user_accounts[user][account_type]
                return True

        return False

    def get_account(self, user, account_type):
        """Gets the account for user of *account_type*. Returns None if the account doesn't exist"""
        if user is None:
            raise ValueError("*user* must be a valid Bank.User object. It cannot be None.")

        if user not in self._user_accounts:
            return None

        return self._user_accounts[user].get(account_type, None)



# Just for fun, validates amount for any functions involving amount
def amount_validator(f):
    @wraps(f)
    def wrapper(account_self, amount, *args):
        if amount is not None and amount <= 0:
            raise ValueError("Non-positive value not allowed. *amount must be > 0")

        return f(account_self, amount, *args)

    return wrapper


class Account(metaclass=ABCMeta):
    """Abstract class for a bank account. Has basic properties and methods all bank accounts share.

    Attributes:
        user_id: id of user associated with account, once it's set, it cannot be changed
        balance: balance of business account
        account_id: unique id of the account, once it's set, it cannot be changed
    """

    def __init__(self,  user_id, balance=0):
        if balance < 0:
            raise ValueError("*balance* must be non-negative")

        self._account_id = uuid.uuid1()
        self._balance = balance
        self._user_id = user_id

    def __eq__(self, other):
        return (self._account_id, self._user_id) == (other.account_id, other.user_id)

    def __ne__(self, other):
        return not self == other

    @property
    def balance(self):
        return self._balance

    @property
    def account_id(self):
        return self._account_id

    @property
    def user_id(self):
        return self._user_id

    @abstractmethod
    def withdraw(self, amount):
        raise NotImplementedError("withdraw() not implemented")

    @abstractmethod
    def deposit(self, amount):
        raise NotImplementedError("deposit() not implemented")


class CheckingAccount(Account):
    """Basic checking account class. Has a transaction limit which can be changed. Setting it to None would remove the limit.

    Attributes:
        transaction_limit: A limit of how much money can be used in a withdrawal/deposit
    """

    def __init__(self, user_id, balance=0, transaction_limit=250):
        super().__init__(user_id, balance)

        if transaction_limit is not None and transaction_limit <= 0:
            raise ValueError("*transaction_limit* must be non-negative")

        self._transaction_limit = transaction_limit

    @property
    def transaction_limit(self):
        return self._transaction_limit

    @transaction_limit.setter
    @amount_validator
    def transaction_limit(self, amount):
        self._transaction_limit = amount

    @amount_validator
    def withdraw(self, amount):
        if amount > self._balance or amount > self._transaction_limit:
            return False

        self._balance -= amount
        return True

    @amount_validator
    def deposit(self, amount):
        self._balance += amount
        return True


class SavingsAccount(Account):
    """Basic savings account class. Has a base amount limit which can be changed. Setting it to None would remove the limit.

    Attributes:
        base_amount: A minimum balance that must be in the bank account. This adds an additional factor when withdrawing
    """

    def __init__(self, user_id, balance=0, base_amount=1000):
        super().__init__(user_id, balance)

        if base_amount is not None and base_amount <= 0:
            raise ValueError("*base_amount* must be non-negative")

        self._base_amount = base_amount

    @property
    def base_amount(self):
        return self._base_amount

    @base_amount.setter
    @amount_validator
    def base_amount(self, amount):
        self._base_amount = amount

    @amount_validator
    def withdraw(self, amount):
        if (self._base_amount is not None and self._base_amount > self._balance - amount) or amount > self._balance:
            return False

        self._balance -= amount
        return True

    @amount_validator
    def deposit(self, amount):
        self._balance += amount
        return True


class BusinessAccount(Account):
    """Class that subclasses Account that represents a business account. A business account must be created
    and associated with a business name. A business account has no transaction limits and can go into negative balance.

    Attributes:
        business_name: name of business associated with account
    """

    def __init__(self, user_id, business_name, balance=0):
        super().__init__(user_id, balance)

        if not business_name:
            raise ValueError("Business name must be a non-empty string.")

        self._business_name = business_name

    @property
    def business_name(self):
        return self._business_name

    @business_name.setter
    def business_name(self, name):
        if not name:
            raise ValueError("Business name must be a non-empty string.")

        self._business_name = name

    @amount_validator
    def withdraw(self, amount):
        self._balance -= amount
        return True

    @amount_validator
    def deposit(self, amount):
        self._balance += amount
        return True

