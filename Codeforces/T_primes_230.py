def main():
  from sys import stdin, stdout
  tprime = [True] * (1000007)
  tprime[0] = False
  tprime[1] = False

  for i in range(2,len(tprime)):
    if tprime[i]:
      for j in range(i*2, 1000007, i):
        tprime[j] = False

  numeros = stdin.readline()
  valor = stdin.readline().split()

  for i in valor:
    if int(i) ** 0.5 == int((int(i) ** 0.5)) and tprime[int(int(i) ** 0.5)]:	
      stdout.write("YES\n")
    else:
      stdout.write("NO\n")

if __name__ == "__main__":
  main()
