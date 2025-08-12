import random
def main():
    item=["rock","paper","scissors"]
    user_cnt=0
    comp_cnt=0
    while True:
        print()
        print("1.rock")
        print("2.paper")
        print("3.scissor")
        print("4.exit")
        
        choice=int(input("enter your choice="))
        computer_choice=random.choice(item)
        if choice==1 and computer_choice=='paper':
            print("you loose!!!")
            comp_cnt+=1
        elif choice==1 and computer_choice=='scissors':
            print("you won!!!")
            user_cnt+=1
        elif choice==1 and computer_choice=='rock':
            print("draw")
        elif choice==2 and computer_choice=='rock':
            print("you won!!!")
            user_cnt+=1
        elif choice==2 and computer_choice=='scissors':
            print("you loose!!!")
            comp_cnt+=1
        elif choice==2 and computer_choice=='paper':
            print("draw")
        elif choice==3 and computer_choice=='scissors':
            print("draw")
        elif choice==3 and computer_choice=='paper':
            print("you win!!!")
            user_cnt+=1
        elif choice==3 and computer_choice=='rock':
            print("you loose!!!")
            comp_cnt+=1
        elif choice==4:
            print("exiting game...")
            print("your score is=",user_cnt)
            print("computer score is=",comp_cnt)
            if user_cnt>comp_cnt:
                print("Hurray! you are the winner")
            else:
                print("computer is winner\nGood luck")
            break

        else:
            print("enter valid choice")
            
main()