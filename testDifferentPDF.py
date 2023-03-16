from pypdf import PdfReader, PdfWriter

reader = PdfReader("testPDF.pdf")
writer = PdfWriter()

page = reader.pages[0]
fields = reader.get_fields()


print(reader.get_form_text_fields(True))

writer.add_page(page)

dictFields = {'test1': "hello", 'another2': 'dasdf44'}

writer.update_page_form_field_values(writer.pages[0], dictFields)

# write "output" to pypdf-output.pdf
with open("testOut.pdf", "wb") as output_stream:
    writer.write(output_stream)
