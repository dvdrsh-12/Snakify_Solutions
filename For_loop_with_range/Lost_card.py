N = int(input())
sum_all_cards = (N * (N + 1)) // 2 
sum_remaining_cards = 0

for _ in range(N - 1):
    num = int(input())
    sum_remaining_cards += num

lost_card = sum_all_cards - sum_remaining_cards

print(lost_card)
