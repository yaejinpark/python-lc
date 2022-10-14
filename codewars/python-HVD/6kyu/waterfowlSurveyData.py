

def create_report(names):
    duck_dic={}
    output=[]
    for name in names:
        x=1
        while name[x].isnumeric()== False:
            x+=1
        duck = name[:(x-1)]
        quant= name[x:]
        # duck = duck.replace('-', ' ')
        # duck = duck.split(' ')
        duck = " ".join(duck.split())
        duck = duck.split(' ')
        print(duck)
        if len(duck)== 1:
            duck_abv=duck[0][:6].upper()
        elif len(duck)==2:
            duck_abv=(duck[0][:3]+duck[1][:3]).upper()
        elif len(duck)==3:
            duck_abv=(duck[0][:2]+duck[1][:2]+duck[2][:2]).upper()
        else:
            duck_abv=(duck[0][:1]+duck[1][:1]+duck[2][:2]+duck[3][:2]).upper()
        print(duck_abv)
        if duck_abv in duck_dic:
            duck_dic[duck_abv]=int(duck_dic[duck_abv])+int(quant)
        else:
            duck_dic[duck_abv]= int(quant)

        duck_dic = {key: value for key, value in sorted(duck_dic.items())}
    for key, value in duck_dic.items():
        output.extend([key,value])
    return output







import codewars_test as test

test.assert_equals(create_report(["Redhead 3", "Gadwall  1", "Smew 4", "Greater Scaup 10", "Redhead 3", "Gadwall 9", "Greater Scaup  15", "Common Eider 6"]), ["COMEID", 6, "GADWAL", 10, "GRESCA", 25, "REDHEA", 6, "SMEW", 4])