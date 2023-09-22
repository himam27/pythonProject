#Par Mathéo Hima
#Fait en 2023
#Code TP1
print ('Ce programme compte le nombre de mots dan une phrase.')
def count_words (phrase) :
  print(len(phrase.split(" ")), "mots")
count_words(str(input("Écrivez votre texte: ")))