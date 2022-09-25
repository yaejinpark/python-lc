# https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python
def stock_list(listOfArt, listOfCat):
    if len(listOfArt) == 0 or len(listOfCat) == 0: return ""
    
    category_counter = {}
    
    for cat in listOfCat:
        category_counter[cat] = 0
        
    quant = [int(listOfArt[i].split(" ")[1]) for i in range(len(listOfArt))]
    first_char = [listOfArt[i].split(" ")[0][0] for i in range(len(listOfArt))]
    
    for i in range(len(first_char)):
        if first_char[i] in listOfCat:
            category_counter[first_char[i]] += quant[i]
    
    stock_list = [f"({k} : {v})" for k,v in category_counter.items()]
    
    output = " - ".join(stock_list)
    return output