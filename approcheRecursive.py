def factorielle(n):
  if n < 0:
      raise ValueError("La factorielle existe que pour n>=0 !")
  resultat = 1
  # Attention la boucle commence à 1 !
  # Donc si n=0 on n'entre pas dans la boucle
  for i in range(1, n + 1):s
      resultat *= i
  return resultat

def factorielle_recursive(n):
  if n == 0:  # Cas de base
      return 1
  return n * factorielle_recursive(n - 1)  # Cas récursif

def recherche_binaire_recursive(arr, target, min, max):
    # Cas de base : Si la plage de recherche est invalide
    if min > max:
        return -1  # L'élément n'a pas été trouvé

    # Calcul de la position du pivot
    pivot = (min + max) // 2

    # Si l'élément au pivot est celui recherché
    if arr[pivot] == target:
        return pivot

    # Si l'élément recherché est plus grand que l'élément au pivot
    elif arr[pivot] < target:
        return recherche_binaire_recursive(arr, target, pivot + 1, max)

    # Si l'élément recherché est plus petit que l'élément au pivot
    else:
        return recherche_binaire_recursive(arr, target, min, pivot - 1)

# Exemple d'utilisation
tableau = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
print(recherche_binaire_recursive(tableau, 7, 0, len(tableau) - 1))  # Sortie : 3

# Exemple d'utilisation
print(factorielle(2))  # Affiche 120