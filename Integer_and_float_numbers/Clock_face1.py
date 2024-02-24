H = int(input())
M = int(input())
S = int(input())

hour_angle = (H % 12) * 30 + M / 60 * 30 + S / 3600 * 30

print(hour_angle)