# system_hellocall.py
# Core logic for HelloCall app

class HelloCallSystem:
    def __init__(self):
        self.coins = 0
        self.free_trial_used = False

    # Activate free trial
    def activate_free_trial(self):
        if not self.free_trial_used:
            self.coins += 500
            self.free_trial_used = True
            return f"Free Trial Activated! Balance: {self.coins} Coins"
        return "Free trial already used."

    # Earn coins
    def earn_coins(self, amount):
        self.coins += amount
        return f"You earned {amount} coins! Balance: {self.coins}"

    # Spend coins
    def spend_coins(self, amount):
        if amount > self.coins:
            return f"Not enough coins. Balance: {self.coins}"
        self.coins -= amount
        return f"You spent {amount} coins. Balance: {self.coins}"


# Example usage
if __name__ == "__main__":
    system = HelloCallSystem()
    print(system.activate_free_trial())
    print(system.earn_coins(20))
    print(system.spend_coins(10))
