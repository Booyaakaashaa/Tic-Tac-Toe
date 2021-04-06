text = input().split()
text = [t for t in text if t[-1] == 's']
print("_".join(text))
