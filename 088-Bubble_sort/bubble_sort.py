def bubble_sort(liste):
    """Simple implementation of a bubble sorting algorithm

    Args:
        liste ([list]): [list containing integers]
    """
    i = 0
    while i < len(liste) - 1:
        if liste[i] > liste[i+1]:
            liste[i], liste[i+1] = liste[i+1], liste[i]
            i = 0
        else:
            i += 1
    return(liste)

#l = [40, 16, 80, 2, 90, -1, -1]
#print(bubble_sort(l))