import requests

# download and save a picture ----------------------------------------------
pic_url = 'https://www.python.org/static/opengraph-icon-200x200.png'
downloded_data = requests.get(pic_url)

with open("image1.png", "wb") as code:
	code.write(downloded_data.content)

# download and save a pdf file ---------------------------------------------
pdf_url = 'https://media.readthedocs.org/pdf/urllib3/latest/urllib3.pdf'
downloded_data = requests.get(pdf_url)

with open("pdf1.pdf", "wb") as code:
	code.write(downloded_data.content)

# download and save a zip file ---------------------------------------------
zip_url = 'https://docs.python.org/2/archives/python-2.7.14-docs-pdf-a4.zip'
downloded_data = requests.get(zip_url)

with open("zip1.zip", "wb") as code:
	code.write(downloded_data.content)

