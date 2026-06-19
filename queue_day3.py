l=[]
while(True):
    print("""
          1.Add a element
          2.Remove Element
          3.Display first three elements
          4.Display last three elements
          5.Print
          6.Exit""")
    ch = int(input("Enter your choice:"))

    if ch == 1:
        e=int(input("Enter the element to be added:"))
        l.append(e)
    elif ch == 2:
        if len(l) == 0:
            print("Queue is empty")
        else:
            l.pop(0)
    elif ch == 3:
        if len(l) == 0:
            print("Queue is empty")
        else:
            for i in l[0:3]:
                print("First three elements:",i)
    elif ch == 4:
        if len(l) == 0:
            print("Queue is empty")
        else:
            print("Last three elements:",l[-3:-1])
    elif ch == 5:
        print(l)
    elif ch == 6:
        break
    else:
        print("Invalid choice")
