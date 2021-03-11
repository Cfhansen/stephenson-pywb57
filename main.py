print("Enter year:")
year = int(input())
result = False

if (not year % 400) or ((not year % 4) and (year % 100)):
  result = True

print(result)
