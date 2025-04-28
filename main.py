import json
import os
import sys
import hashlib as hl

with open("user-data.json", "r") as file:
  user_data = json.load(file)
  
def Clean():
  os.system('cls')
Clean()

login_attemps = 3
def Login(user, password):
  
  hash_key_password = hl.sha256(password.encode()).hexdigest()
  
  if user in user_data and user_data[user]["hash-key"] == hash_key_password:
    print("✅ Login bem sucedido ✅")
    return True
    
  else:
    global login_attemps
    login_attemps -= 1
    print(f"❌ Usuário ou senha incorretos. Você tem apenas mais {login_attemps} tentativas. Tente novamente! ❌")
    return False

def CheckBalance(user):
  return print(f"O saldo do usúario {user_data[user]["nickname"]} é de R${user_data[user]["balance"]}")

def DepositMoney(amount):
  user_data[user]["balance"] += amount
  with open ("user-data.json", "w") as file:
    json.dump(user_data, file, indent=2)
    
  return print(f"O valor de R${amount} foi inserido com sucesso!")

def DrawMoney(amount):
  
  if amount > user_data[user]["balance"]:
    return print('Você não tem saldo suficiente para sacar.')
  
  else:
    user_data[user]["balance"] -= amount
    
    with open ("user-data.json", "w") as file:
      json.dump(user_data, file, indent=2)
      
    return print(f"Você sacou R${amount} da sua conta.")

def TransferMoney(amount, receiver):  
  if amount > user_data[user]["balance"]:
    return print('Você não tem saldo suficiente para transferir.')
  
  else:
    user_data[user]["balance"] -= amount
    user_data[receiver]["balance"] += amount
    
    with open ("user-data.json", "w") as file:
      json.dump(user_data, file, indent=2)
    
    print(f"O saldo de R${amount} foi transferido para {user_data[receiver]["nickname"]}")

print('💵 Seja bem-vindo ao ATM-Python 💵')

while True: # verifying login
  user = str(input("Por favor, digite o seu usuário: "))
  password = str(input("Por favor, digite a sua senha: "))
  Clean()
  
  
  if Login(user, password):
    break

  if login_attemps == 0: # will verifies if the usuarie tried to acess 3 times
    Clean()
    print("❌ Você tentou muitas vezes! Aguarde um instante e tente novamente. ❌")
    sys.exit()
  
while True:
  main_options = int(input("""Oque você deseja fazer?
      
1 - Consultar Saldo
2 - Depositar Dinheiro
3 - Sacar Dinheiro
4 - Transferir Dinheiro
5 - Sair do Sistema

"""))
  
  Clean()
  
  if main_options == 1:
    CheckBalance(user)
    
  elif main_options == 2:
    Clean()
    
    amount = float(input("Qual o valor você deseja inserir? "))
    Clean()
    DepositMoney(amount)
    
  elif main_options == 3:
    Clean()
    
    amount = float(input("Qual o valor você deseja sacar? "))
    Clean()
    DrawMoney(amount)
    
  elif main_options == 4:
    while True:
      if user_data[user]["balance"] == 0:
        print(f"Impossível realizar transferências no momento, pois seu saldo é {user_data[user]["balance"]}")
        break
      
      receiver = str(input("Para quem você deseja transferir? "))
      Clean()
      if receiver in user_data:
        amount = float(input("Quanto você deseja transferir? "))
        Clean()
        TransferMoney(amount, receiver)
        break
      
      else:
        Clean()
        print('Usuário não encontrado, por favor, digite novamente.')
        continue
    
  elif main_options == 5:
    sys.exit()
    
  else:
    print("Você digitou uma opção inválida. Por favor, tente novamente!")
    continue