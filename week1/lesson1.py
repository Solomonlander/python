# '''the creativity used was to change all variables to upprcase so that they display as capital lettters when the prgram is run''''''

print("Hello user! Welcome to my story.")

#series of words"""""""

verb1 = input('Please enter a verb: ').upper()
noun = input('Please enter a noun: ').upper()
verb2 = input('Please enter a verb: ')
exclamation = input('Please enter an exclamation: ').capitalize()
adjective = input('Please enter an adjective: ').upper()
animal = input('Please enter an animal: ').upper()

# My story line"""

words = f'''The other day, after returning from church. 
 \n I decided to {verb1} my {noun} and prepare for my next week course work.
 \nI head my siblings crying and some were very {adjective} and i asked.
 \nWhat happen, they said that my {animal} gave birth, i was like 
 \n{exclamation}.
 \nOut of excitement i {verb2} my friend one of the puppy.'''

print(words)