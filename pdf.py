#####################################################################################################################################
#our first step is to find a library that we can use with Python to process PDF files.
# pip3 install PyPDF2

import PyPDF2
print("hhhhh")

#####################################################################################################################################
# Well, remember, binary is ones and zeros.
# If I click on Dummies.pdf
# This is not the PDF we thought. this is not how a pdf should look.
# But you see, depending on the program that you're running, it might not be able to read the PDF file.
# So what we need to do?
# --> we want to read the binary.
# So it's read and then binary. ('rb')
#####################################################################################################################################
with open('dummy.pdf','rb') as file:
	print("\n"+('*' * 20))
	reader = PyPDF2.PdfReader(file)

	####################################################################################################################################
    # this creates : a file stream object.
	# --> So it's going to convert the file object to binary mode.
    # So that the pypdf2 file-reader:  Can read that binary file object.
	#####################################################################################################################################
	
	print(reader.pages[0])
	#We get the page object over here.
	#kip in notice, you need not to cross the limits of the pdf's number of pages, lets say: has only 1 page --> 0 , if you have inserted 2\1\.. --> ERROR
	print("\n"+('*' * 20))
 
	print(f"length of the pdf: {len(reader.pages)}")
	
	print("\n"+('*' * 20))
	
	#####################################################################################################################################
	## print(reader.rotate(180)) # rotate this image and we'll rotate it 180 degrees.
	# --> This doesn't work.
    # Now why is this?
	# It's because PyPDF2 uses the reader object, but it needs to know ("what") to rotate.
	# In our case, we actually have to get the page of the reader to rotate it.
	# ==> 
	page = reader.pages[0] # Get the first page of our dummy pdf, And assign this to the page variable
	print(page.rotate(180)) 
	# we get back an object here, but this object is actually in memory.
    # If I go back to my dummy.
    # Nothing has changed because we haven't really saved anything.
    # This is all in my computer's memory.
    # When this program stops running, well, it gets trashed.
	# --> So let's update our dummy PDF to actually write and rotate counterclockwise.
	
	rotated_page = page.rotate(90)# explanation why below.# i didnt waane delete the print... so its now 180 + 90 = 270 degres.

	writer = PyPDF2.PdfWriter()
	writer.add_page(rotated_page)
	# And we're going to open this "tilt" file and we're going to write to this file and binary format as new_file.
    # And in here, we're going to write the file to this new file.
    # But how?:
    # -> This library gives us something called a PdfWriter object so we can create a writer variable.
    
	# And this writer variable will use instead of reader ->  write
    # This allows us to write the object and memory so that now I can say writer.write.
	
	with open('tilt.pdf', 'wb') as new_file: 
		writer.write(new_file)
		# we actually forgot to do one thing because we've just opened a writer object,
		# but we're not actually writing any PDFs into it.
		# Ideally, we get the rotated page and write inside of it, right?
		# so we will remove the : print in : 	print(page.rotate(180)) 
		# so we have rotated the page, and with the PdfWriter obgect : we can say :  writer.add_page(page) - the page we have rotated. --> run the tilt.pdf (open it) --> works.
		print(f"Page rotation before saving: {rotated_page.get('/Rotate')} degrees")


	print("\n"+('*' * 20))

#####################################################################################################################################