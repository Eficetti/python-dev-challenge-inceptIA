import pandas as pd
import numpy as np

_PRODUCT_DF = pd.DataFrame({"product_name": ["Chocolate", 
"Granizado", "Limon", "Dulce de Leche"], "quantity": 
[3,10,0,5]})
def is_product_available(product_name, quantity):
    reqp_Index = _PRODUCT_DF[_PRODUCT_DF['product_name']==product_name]
    result = reqp_Index.values
    list1 = result.tolist()
    if result[0][1] >= quantity:
        return True 
    else:
        return False
    
is_product_available("Chocolate", 6)