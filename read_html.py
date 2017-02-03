
from bs4 import BeautifulSoup
soup = BeautifulSoup('/Formato_Datos.html', 'html.parser')

print(soup.prettify())