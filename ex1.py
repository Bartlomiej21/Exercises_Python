'''
Funkcja sprawdzająca, czy w danej liście są parzyste czy nieparzyste liczby w zależności od zmiennej boolean.
'''



numbers = [10, 20 , 17 , 13 ]
even_or_odd = True

def filter_even_odd(numbers,even_or_odd):
    filtered_list = []
    if even_or_odd is False:  #parzyste
        for i in numbers:
            if i%2==0:
                filtered_list.append(i)
        
        return filtered_list
    else:   # nieparzyste
        for i in numbers:
            if i%2!=0:
                filtered_list.append(i)
                
        return filtered_list
