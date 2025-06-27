# execption = inturup flow of a programm
# (type error,zero division,value errror 
# try except finally


try:
    number = int(input("enter no.:"))
    print(1/number)
except ZeroDivisionError:
    print("cant divede by zero")
except ValueError:
    print("enter number only")

except Exception:                       ## GENERAL
    print("something went wrong")

finally:
    print("do some clean up")  # always excecutes

