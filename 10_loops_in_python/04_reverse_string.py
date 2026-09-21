string = str(input("Enter a string : ")).strip()

rev = ""
for i in string:
    rev = i + rev
print(rev)

#Initial: rev = ""

#i = 'r' → rev = 'r' + ""      → "r"
#i = 'o' → rev = 'o' + "r"     → "or"
#i = 's' → rev = 's' + "or"    → "sor"
#i = 'h' → rev = 'h' + "sor"   → "hsor"
#i = 'a' → rev = 'a' + "hsor"  → "ahsor"
#i = 'n' → rev = 'n' + "ahsor" → "nahsor"
