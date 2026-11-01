# ATM USING EXCEPTION AND CUSTOME EXCEPTION


class InsufficientBalanceError(Exception):
    pass
class InvalidAmountError(Exception):
    pass


balance = 5000
while True:
    try:
        amount = int(input("Enter your withdrawal amount:"))

        if amount > balance:
            raise InsufficientBalanceError("Insufficient balance in Your account")


        if amount <= 0:
            raise InvalidAmountError("Amount is not less than zero or zero")
        balance = balance - amount

        print("Withdrwal successfull")
        print("New Balance :",balance)

    except InsufficientBalanceError as e:
        print("Error:", e)
        break
    
    except InvalidAmountError as e:
        print("Error:", e)
        break

    except ValueError:
        print("Enter numbers only !")
        break
    
    try:
        deposit_amount = int(input("Enter your deposit amount:"))

        if deposit_amount <= 0:
            raise InvalidAmountError("Amount cannot be zero")

    # else:
    #     print("Your amount is deposit sucessfully")

        balance = balance + deposit_amount 
        print("Your amount is deposite successfully")
        print("New_Balance:",balance)
        break

    except InvalidAmountError as e:
        print("Error:", e)
        break

    except ValueError:
        print("Enter numbers only !")
        break

print("ATM TRANSACTION IS COMPLETED...!")
print("VISIT AGAIN ...!")
print("THANK YOU...!")


