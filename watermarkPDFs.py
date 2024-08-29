# I want a program that can watermark my PDFs.
# instead of me doing manually -> let's say we had thousands of pages...

# Let's say you're working on a TV show.
# you want to give the script  to your cast members and all these actors that are going to get a draft of the script.
# which is super secret, because you don't want the audience to find out what happens in the show...
# But we don't want them to leak the script to the press so that everybody finds out about it.

# So usually big companies in Hollywood watermark their script with usually an actor's name.
# So if that actor leaks the script, well, they'll know that that person has their name on the script...

# What we want to do is ideally use the wtr.pdf that I'll provide for you.
# I want to write this water pdf on all the pages of super pdf that we combined - in combinedPdf.py.


import PyPDF2
# b : PDFs are binary files, meaning they contain data that isn't just plain text. When working with binary files, you should open them in binary mode.
# Read Mode (r): The "r" indicates that the file is opened for reading. Since you are opening the PDFs (super.pdf and wtr.pdf) to read their contents, you use the "r" mode.

# Open the main PDF that you want to watermark (super.pdf) in read-binary mode.
template = PyPDF2.PdfReader(open('super.pdf', 'rb'))

# Open the watermark PDF (wtr.pdf) in read-binary mode.
# This is the PDF that contains the watermark you want to apply to every page.
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))

# Create a PdfWriter object that will be used to write the new watermarked PDF.
output = PyPDF2.PdfWriter()

# Loop through each page of the main PDF (super.pdf).
for i in range(len(template.pages)):  # If super.pdf has 5 pages, this loop runs 5 times.
    page = template.pages[i]  # Get the current page.
    
    # Merge the first page of the watermark PDF with the current page.
    # The watermark PDF only has one page, which will be applied to all pages of super.pdf.
    page.merge_page(watermark.pages[0])
    
    # Add the merged page (original + watermark) to the output PDF.
    output.add_page(page)
    
    # Write the watermarked pages to a new PDF file called 'watermarked_output.pdf'.
    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
