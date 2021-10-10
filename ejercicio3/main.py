_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", 
"Navidad2x1", "heladoFrozen"]

def validate_discount_code(discount_code):
    """
    Ejemplo: 
    "primavera2021" deberia devolver True, ya que al compararlo:
    vs "Primavera2021" = 2 caracteres de diferencia ("p" y "P")
    vs "Verano2021" = 7 caracteres de diferencia ('i', 'n', 'o',
    'm', 'V', 'p', 'v')
    vs "Navidad2x1" = 8 caracteres de diferencia ('N', 'm', '0',
    'x', 'e', 'd', 'p', 'r')
    vs "heladoFrozen" = 14 caracteres de diferencia ('z', 'i',
    'v', 'n', 'o', 'm', '2', '0', 'd', 'p', '1', 'F', 'h', 'l')
    """

    listaTemporal = []
    discountList = []
    discountList.append(discount_code)
    for i in range(len(_AVAILABLE_DISCOUNT_CODES)):
        listaTemporal.append(_AVAILABLE_DISCOUNT_CODES.pop(0))
        a = [caracter for caracter in listaTemporal[0]]
        b = [caracter for caracter in discountList[0]]
        valoresDiferentes = list(set(a) ^ set(b))
        if len(valoresDiferentes) < 3:
            return True
        listaTemporal.clear()


discount = input('Ingrese su codigo de descuento: ')

validate_discount_code(discount)