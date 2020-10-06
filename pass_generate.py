import random

lower="qwertyuiopasdfghkjlzxcvbnm"
upper="QWERTYUIOPASDFGHJKLZXCVBNM"
numbers="0987654321"
symbols="(){}[]#@&$-,!?"
p1="".join(random.sample(lower,6))
p2="".join(random.sample(upper,2))
p3="".join(random.sample(numbers,4))
p4="".join(random.sample(symbols,2))
p=p1+p2+p3+p4
password="".join(random.sample(p,14))

print(password)