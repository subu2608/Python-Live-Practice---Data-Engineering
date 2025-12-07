from transformers import GPT2Tokenizer

#Loading Pre-trained GPT2 Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

#Input Text
text= input("enter text")

#Tokenise the input
tokens = tokenizer.tokenize(text)
tokens_id = tokenizer.convert_tokens_to_ids(tokens)

#Print Input text, Token Split, Token ID
print("Input text: ", text)
print("Input tokens: ", tokens)
print("Input Token IDs:", tokens_id)

#Encode directly(token +ids)
encoded = tokenizer.text()
print("Encoded text: ", encoded)

#Decode back from IDs to String
decoded = tokenizer.decode(tokens_id, clean_sentence=True)
print("Decoded text: ", decoded)


