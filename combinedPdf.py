import PyPDF2
import sys

# What I want to do is I want to be able to call: 
# Python3 "myfile" ____ ____ ....  -> and then give it some arguments -> using sys.
# Let's combine tilt, dummy,twopage as well,
#  and we can just keep adding different PDFs and combining them.

inputs = sys.argv[1:]# this is going to grab all the arguments (not the first one - 0), using slice. into a list could inputs.

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfMerger() 
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
		# tells us : merge everything into this merger object,
		# the PDFs that we're going to loop through.
		#  at the end of the loop: this merger is going to have all these three PDFs.
	merger.write('super.pdf')	
pdf_combiner(inputs)

# If we're working on a book, for example, 
# and maybe we have different people working on different chapters,
# I can just run it through this function now and combine my entire PDF into one.
# Very, very cool.







