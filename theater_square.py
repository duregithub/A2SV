values = input()
g = values.split()

m = int(g[0])
n = int(g[1])
a = int(g[2])

x = m/a
y = n/a

if x != m//a:
    
    x = m//a + 1
if y != n//a:
    y = m//a + 1

print ( x + y)

# nor solved
