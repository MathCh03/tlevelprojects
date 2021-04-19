cq1=input("Please enter what currency you wish to convert. \nGBP \nUSD \nJPY \nEUR \n")
print(cq1)
if cq1=="GBP":
  cq2=input("Please enter what currency you wish to convert to. \nUSD \nJPY \nEUR \n")
  print(cq2)
  cq3=float(input("Please enter the amount of "+cq1+" you wish to convert \n"))
  print(cq3)
  if cq2=="USD":
      gbp2usd=float(1.34)
      print("Your amount is $",cq3*gbp2usd,". Thank you!")
  if cq2=="JPY":
      gbp2jpy=float(139.75)
      print("Your amount is ¥",cq3*gbp2jpy,". Thank you!")
  else:
      gbp2eur=float(1.11)
      print("Your amount is €",cq3*gbp2eur,". Thank you!")
if cq1=="USD":
  cq2=input("Please enter what currency you wish to convert to. \nGBP \nJPY \nEUR \n")
  print(cq2)
  cq3=float(input("Please enter the amount of "+cq1+" you wish to convert \n"))
  print(cq3)
  if cq2=="GBP":
      usd2gbp=float(0.75)
      print("Your amount is £",cq3*usd2gbp,". Thank you!")
  if cq2=="JPY":
      usd2jpy=float(104.24)
      print("Your amount is ¥",cq3*usd2jpy,". Thank you!")
  else:
      usd2eur=float(0.83)
      print("Your amount is €",cq3*usd2eur,". Thank you!")
if cq1=="JPY":
  cq2=input("Please enter what currency you wish to convert to. \nGBP \nUSD \nEUR \n")
  print(cq2)
  cq3=float(input("Please enter the amount of "+cq1+" you wish to convert \n"))
  print(cq3)
  if cq2=="GBP":
      jpy2gbp=float(0.0072)
      print("Your amount is £",cq3*jpy2gbp,". Thank you!")
  if cq2=="USD":
      jpy2usd=float(0.0096)
      print("Your amount is $",cq3*jpy2usd,". Thank you!")
  else:
      jpy2eur=float(0.0079)
      print("Your amount is €",cq3*jpy2eur,". Thank you!")
if cq1=="EUR":
  cq2=input("Please enter what currency you wish to convert to. \nGBP \nUSD \nJPY \n")
  print(cq2)
  cq3=float(input("Please enter the amount of "+cq1+" you wish to convert \n"))
  print(cq3)
  if cq2=="GBP":
      eur2gbp=float(0.90)
      print("Your amount is £",cq3*eur2gbp,". Thank you!")
  if cq2=="USD":
      eur2usd=float(1.21)
      print("Your amount is $",cq3*eur2usd,". Thank you!")
  else:
      eur2jpy=float(126.26)
      print("Your amount is €",cq3*eur2jpy,". Thank you!")
