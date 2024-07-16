import re

with open('regex.txt','r') as f:
    f_content=f.read()
    
    ##finding a particular pattern
    # pattern=re.compile(r'abc')
    # matches=pattern.finditer(f_content)
    # for match in matches:
    #     print(match)
        
    # pattern=re.compile(r'.') # instead of finding for . it show result for each letter/character including spaces also, this is because . is a MetaCharacter and these characters need to be escaped
    # matches=pattern.finditer(f_content)
    # for match in matches:
    #     print(match)
    # pattern=re.compile(r'\.') # on adding '\' before the metacharacter this is will work as expected
    # matches=pattern.finditer(f_content)
    # for match in matches:
    #     print(match)
        
    # pattern=re.compile(r'codelvl\.com')
    # matches=pattern.finditer(f_content)
    # for match in matches:
    #     print(match)
    # print(f_content[138:149])
    '''
     Use this      |      To find
    -------------------------------------------------------
     .             |      any character except newline(/n) 
     \d            |      digits (0-9)
     \D            |      Not a digit (0-9)
     \w            |      word charcters (a-z, A-Z, 0-9, _)
     \W            |      not a word character
     \s            |      whitespaces (space, tab, newline)
     \S            |      not whitespace
     Cross check from below code '''
    # pattern=re.compile(r'\S')
    # matches=pattern.finditer(f_content)
    # for match in matches:
    #     print(match)
  
    phn=re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
    matches=phn.finditer(f_content)
    for match in matches:
        print(match)
    phn=re.compile(r'\+91.\d\d\d\d\d\d\d\d\d\d') # similarly for other phn no. patterns
    matches=phn.finditer(f_content)
    for match in matches:
        print(match)
    
    '''
    Anchors:
    \b -> Word Boundary
    \B -> Not a word boundary
    ^  -> Beginning of a string
    $  -> End of a string
    Cross check from below code ''' 
    # pattern=re.compile(r'\BAlpha')
    # matches=pattern.finditer(f_content)
    # for match in matches:
    #     print(match)
    # sentence='Start a sentence and then bring it to an end'
    # pattern = re.compile(r'^Start')
    # matches = pattern.finditer(sentence)
    # for match in matches:
    #     print(match)
    # pattern = re.compile(r'end$')
    # matches = pattern.finditer(sentence)
    # for match in matches:
    #     print(match)
        