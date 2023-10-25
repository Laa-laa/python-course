def table_multi(n):
    result = []
    for i in range (1, 11):
        produit = n * i
        if produit % 3 == 0:
            result.append(f'{produit}*')
        else:
            result.append(produit)
    return result

entier = 5

result = table_multi(entier)
print(result)