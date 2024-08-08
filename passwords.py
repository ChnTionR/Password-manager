def decrypt(string):
    strng = list(string)
    out = ""
    lttrs = "abcdefghijklmnopqrstuvwxyz0123456789!'^+%&/()=?_-\}][{½$#£<>|.ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    index = 0
    for i in strng:
        currentindex = 0
        i = str(i)

        if i not in lttrs:
            pass
        else:
            currentindex = lttrs.index(i)
            targetindex = currentindex - 5
            if targetindex > len(lttrs):
                targetindex = targetindex - len(lttrs)
            strng[index] = lttrs[targetindex]
        index += 1
    for i in strng:
        out = out + i
    return out

def encrypt(string):
    strng = list(string)
    out = ""
    lttrs = "abcdefghijklmnopqrstuvwxyz0123456789!'^+%&/()=?_-\}][{½$#£<>|.ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    index = 0
    for i in strng:
        currentindex = 0
        i = str(i)

        if i not in lttrs:
            pass
        else:
            currentindex = lttrs.index(i)
            targetindex = currentindex + 5
            if targetindex > len(lttrs):
                targetindex = targetindex - len(lttrs)
            strng[index] = lttrs[targetindex]
        index += 1
    for i in strng:
        out = out + i
    return out

def append_details(site, username, password):
    details = encrypt(f"{site}: {username}, {password}")
    with open("passwords.txt","a") as file:
        file.write(f"{details}\n")

def locate_details(site):
    foundlines = []
    with open("passwords.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if site in line.split(":")[0]:
                foundlines.append(line)
        return foundlines

def find():
    firstturn = True
    line_no = 1
    infos = []
    sitename = input("//////////////////////////////////////////////////////////////////////////////////////////////////////////////\nsite name?\n(b)ack\n")
    if sitename.lower() != "b":
        for line in locate_details(encrypt(sitename)):
            if firstturn == True:
                print()
                firstturn = False
            print(f"{str(line_no) +') '+ decrypt(line)}")
            infos.append(str(line_no) +') '+ decrypt(line))
            line_no += 1
        if len(infos) == 0:
            print("there is no logged in details of that site\n")
            return 1
        return infos
    else:
        return True
        
action = ""
while True:
    action = input("//////////////////////////////////////////////////////////////////////////////////////////////////////////////\n if you want to enter new login details, type 'enter'\n if you want to retrieve login details, type 'find'\n if you want to remove login details, type 'remove' \n (q)uit\n").lower()
    if action == "removeall":
        open("passwords.txt","w").close
        
    elif action == "enter":
        site = input("//////////////////////////////////////////////////////////////////////////////////////////////////////////////\nfor which site?\n(b)ack\n")
        if site.lower() != "b":
            username = input("your username?\n(b)ack\n")
            if username.lower() != "b":
                password = input("your password?\n(b)ack\n")
                if password.lower() != "b":
                    append_details(site, username, password)
                    print("done!")
    
    elif action == "find":
        find()

    elif action == "remove":
        goback = False
        targetline = ""
        with open("passwords.txt", "r") as fpas:
            fpas.seek(0)
            file = fpas.readlines()
        
        details = find()
        if details != 1:
            if details != True:
                removelineno = input("enter the no. of the info that you would like to remove:\n(b)ack\n")
                while not removelineno.isnumeric() or int(removelineno) > len(details) or int(removelineno) == 0:
                    if removelineno.lower() == "b":
                        goback = True
                    if goback:
                        break
                    removelineno = input("please input a valid no.:\n(b)ack\n")
                if goback:
                    pass
                else:
                    index = 0
                    for i in details:
                        info = str(details[index])
                        if int(removelineno) == int(info[0]):
                            targetline = str(info)
                        index += 1
                    
                    open("passwords.txt","w").close()
                    fpas = open("passwords.txt","a")
                    
                    for i in file:
                        if decrypt(file[file.index(i)]) not in targetline:
                            fpas.write(i)
                        else:
                            pass
                        
                    fpas.close()

    elif action == "q":
        break
        
    else:
        print("please enter a valid operation\n")

                
