import hashlib as hlib


def generate_sha1(string):
	encoded_string = str.encode(string)
	return hlib.sha1(encoded_string).hexdigest()
	
	
def generate_sha512(string):
	encoded_string = str.encode(string)
	return hlib.sha512(encoded_string).hexdigest()


def generate_md5(string):
	encoded_string = str.encode(string)
	return hlib.md5(encoded_string).hexdigest()

	
def generate_sha256(string):
	encoded_string = str.encode(string)
	return hlib.sha256(encoded_string).hexdigest()


def main():
	print("Available algorithms:\n1 = MD5\n2 = SHA-1\n3 = SHA-256\n4 = SHA-512\n5 = all of the above")
	choice = input("Please enter desired hashing algorithm: \n")
	string = input("Please enter your text: ")
	if(choice <='0' or choice >'5'):
		print("Invalid choice number ")
	elif(choice=="1"):
		print("MD5:",generate_md5(string))
	elif(choice=="2"):
		print("SHA-1:",generate_sha1(string))
	elif(choice=="3"):
		print("SHA-256:",generate_sha256(string))
	elif(choice=="4"):
		print("SHA-512:",generate_sha512(string))
	elif(choice=="5"):
		print("MD5:",generate_md5(string))
		print("SHA1:",generate_sha1(string))
		print("SHA-256:",generate_sha256(string))
		print("SHA-512:",generate_sha512(string))
		
		
if __name__ == "__main__":
	main()
	
			
