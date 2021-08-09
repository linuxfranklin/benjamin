print("""
 /'\
                 /
                /                 ,
             c-'                 /
            /'-._         ,____,' .-'''-.
       .-'.// \  '-;-========,"-,'       '
     ,`   /,   \_//\       ,/  (  '- *)   )
    (   ./  )   {,}========'===='- '      ,
     ,     ,   \/               ', -muse.
 _____'-.-`_______________________'-..-'____
 
 """)


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1_2=name1+name2
name1_2_lower=name1_2.lower()

t=name1_2_lower.count("t")
r=name1_2_lower.count("r")
u=name1_2_lower.count("u")
e=name1_2_lower.count("e")
true=t+r+u+e

l=name1_2_lower.count("l")
o=name1_2_lower.count("o")
v=name1_2_lower.count("v")
e=name1_2_lower.count("e")
love=l+o+v+e

score=str(true)+str(love)
print(score)

result=int(score)
if result <10 or result >90 :
    print(f"Your score is : {result}, you go togather like coke & mentos")
elif result >=40 and result <=50 :
    print(f"Your score is : {result}, You are alright togather")
else :
    print(f"Your score is : {result}")

