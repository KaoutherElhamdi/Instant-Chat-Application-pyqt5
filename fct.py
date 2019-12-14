def f(m,msg):
    msg=msg.split(" ")
    nv = []
    p = m+msg[0]
    test = True
    while True :
        if len(msg)>(1) :
            if len(p+" "+msg[1]) <= 68 :
                p = p+" "+msg[1]
                msg = msg[1:]
            else :
                msg = msg[1:]
                nv.append(p)
                break
        else :
            nv.append(p)
            test = False
            break
    if test and (len(msg) != 0) :
        p = " "*(len(m))+msg[0]
        while True :
        
            if len(msg)>(1) :
                if len(p+" "+msg[1]) <= 57 :
                    p = p+" "+msg[1]
                    msg = msg[1:]
                else :
                    nv.append(p)
                    msg = msg[1:]
                    p=" "*len(m)+msg[0]
            else :
                nv.append(p)
                break
    return nv


def afficher_message(m,msg):
    msg = f(m,msg)
    msg = "\n".join(msg)
    return msg

if __name__ == "__main__":
    msg = "hi koukou cv sava sa cmkh monu bien tres bien alors merci beacuoup je taime mon cherie ma belle beacuoup je taime mon cherie ma belle beacuoup je taime mon cherie ma belle"
    print(afficher_message("You : ",msg))
