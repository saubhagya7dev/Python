import random

def reverse_martingale_strategy(initial_bet, initial_bankroll, target_profit):
    current_bet = initial_bet
    current_bankroll = initial_bankroll
    total_profit = 0

    while total_profit < target_profit and current_bankroll > 0:
        game_result = random.choice(["win", "lose"])

        if game_result == "win":
            current_bankroll += current_bet * 1.94
            total_profit += current_bet * 0.94
            current_bet *= 2
        else:
            current_bankroll -= current_bet
            total_profit -= current_bet
            current_bet = initial_bet

        if current_bet > current_bankroll:
            print("Bankroll insufficient to continue the Reverse Martingale strategy.")
            break

    return current_bankroll, total_profit

def dalembert_strategy(initial_bet, initial_bankroll, target_profit):
    current_bet = initial_bet
    current_bankroll = initial_bankroll
    total_profit = 0

    while total_profit < target_profit and current_bankroll > 0:
        game_result = random.choice(["win", "lose"])

        if game_result == "win":
            current_bankroll += current_bet * 1.94
            total_profit += current_bet * 0.94
            if current_bet > initial_bet:
                current_bet -= initial_bet
        else:
            current_bankroll -= current_bet
            total_profit -= current_bet
            current_bet += initial_bet

        if current_bet > current_bankroll:
            print("Bankroll insufficient to continue the D'Alembert strategy.")
            break

    return current_bankroll, total_profit

# Example usage
initial_bet = int(input("Enter the initial bet: "))
initial_bankroll = int(input("Enter the initial bankroll: "))
target_profit = int(input("Enter the target profit: "))

# Reverse Martingale
final_bankroll, final_profit = reverse_martingale_strategy(initial_bet, initial_bankroll, target_profit)
print(f"Reverse Martingale - Final Bankroll: {final_bankroll}, Final Profit: {final_profit}")

# D'Alembert
final_bankroll, final_profit = dalembert_strategy(initial_bet, initial_bankroll, target_profit)
print(f"D'Alembert - Final Bankroll: {final_bankroll}, Final Profit: {final_profit}")













