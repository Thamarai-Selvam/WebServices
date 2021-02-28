def encode(message): 
	encoded_message = "" 
	i = 0

	while (i <= len(message)-1): 
		count = 1
		ch = message[i] 
		j = i 
		while (j < len(message)-1): 
			if (message[j] == message[j+1]): 
				count = count+1
				j = j+1
			else: 
				break
		encoded_message=encoded_message+str(count)+ch 
		i = j+1
	return encoded_message 

def decode(s): 
      output = "" 
      num="" 
      for i in s: 
         if i.isalpha() or i == ' ': 
            output+=i*int(num) 
            num="" 
         else:
            num+=i 
      return output 


#Provide different values for message and test your program 
encoded_message=encode("hi there") 
with open('runlength_encode.txt', 'wb+') as output_file:
            output_file.write(bytearray(encoded_message, 'utf-8') )
print(encoded_message) 
print(decode(encoded_message))

with open('runlength_decode.txt', 'w+') as output_file:
            output_file.write(decode(encoded_message))