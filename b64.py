import base64 

args = b'word'
args = base64.b64encode(args)
word = str(args).strip('b')
#args = args.strip('b')
#base64.standard_b64encode(args)
print(word)

#testing git