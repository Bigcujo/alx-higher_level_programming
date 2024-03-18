import string
getattr(__import__('sys', fromlist=['stdout']), 'stdout').write(getattr(string, 'ascii_uppercase'))
"this will print out uppercase alphabets"
