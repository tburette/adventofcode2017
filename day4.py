# Partie 1 : 7:16
# Partie 2 : 8:40
# ralenti par exception
# return len(passphrase) == len(set(passphrase))
# TypeError: unhashable type: 'list'
# Le probleme vient du fait que sorted(str) génère une list
# et une liste ne peut être hashée donc set([ [] ]) ne fonctionne pas
# hashing voir:
# https://docs.python.org/3/glossary.html
# https://docs.python.org/3/reference/datamodel.html#object.__hash__


def no_duplicate(passphrase):
    return len(passphrase) == len(set(passphrase))


def no_anagram(passphrase):
    return no_duplicate([''.join(sorted(word)) for word in passphrase])


def valid(passphrase):
    return no_duplicate(passphrase) and no_anagram(passphrase)


data = open('day4.txt').read().strip()
passphrases = [line.split(' ') for line in data.split('\n')]
print(len([passphrase for passphrase in passphrases if valid(passphrase)]))
