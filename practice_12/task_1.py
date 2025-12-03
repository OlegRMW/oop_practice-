class BankAccount:
    def __setattr__(self, name, value):
        if name == "account_number":
            if not (isinstance(value, str) and value.isdigit() and len(value) == 10):
                raise ValueError("Account number must be a string of 10 digits.")

        elif name == "owner":
            if not (isinstance(value, str) and value.strip()):
                raise ValueError("Owner must be a non-empty string.")

        elif name == "balance":
            if not (isinstance(value, (int, float)) and value >= 0):
                raise ValueError("Balance must be a non-negative number.")

        super().__setattr__(name, value)

    def __getattribute__(self, name):
        try:
            return super().__getattribute__(name)
        except AttributeError:
            if name == "Currency":
                return "EUR"
            return None

    def __getattr__(self, name):
        if name == "Currency":
            return "EUR"
        return None

    def __delattr__(self, name):
        if name in ("account_number", "owner", "balance"):
            raise AttributeError(f"Cannot delete attribute '{name}'")
        super().__delattr__(name)
