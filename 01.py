def zamen(slovo, pozice, novy_znak):
    """V daném slově zamění znak na dané pozici za daný nový znak."""
    zacatek = slovo[:pozice]
    konec = slovo[pozice + 1:]
    nove_slovo = zacatek + novy_znak + konec
    return nove_slovo

print(zamen('kočka', 1, 'a'))
print(zamen('kačka', 2, 'p'))

""" def meno_fce(parametre fce):
    tělo fce - příkazy, které fce dělá, väčšinou začína popisom, čo funkcia roví - v troch úvodzovkách
    
    return - vrátiš nejakú hodnotu
    
"""