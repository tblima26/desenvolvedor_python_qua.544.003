pg = lambda x: x*2
def main():
  numeros = [42, 7, 19, 88, 3, 56, 23, 91, 14, 65]
  listaPg = list(map(pg, numeros))

  for n in listaPg:
    print(n)


if __name__ == "__main__":
  main()