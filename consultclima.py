import requests
from bs4 import BeautifulSoup

def clima():
    """
    Funcion que extrae los datos del clima desde la pagina de accuwather
    """
    page = requests.get("https://www.meteorologia.gov.py/")
    soup = BeautifulSoup(page.content,'html.parser').find_all("div",class_="forecast-owl-item")
    
    #se recolectan los datos con busqueda y consulta css
    temp = soup[0].find_all("span",class_="temp-max")[0].get_text().replace("º",'')
    ciudades = soup[0].find_all("span",class_="city")[0].get_text()
    vientos = soup[0].find_all("div",class_="wind col-forecast-today")[0].select("span.speed span")[0].get_text()
    direccion = soup[0].find_all("div",class_="wind col-forecast-today")[0].select("span.dir")[0].get_text()

    #se carga estos datos en un diccionario y se retorna
    datos = {
        "ciudad":ciudades,
        "temperatura":float(temp),
        "vientos":float(vientos),
        "direccion":direccion
    }
    return datos



    
    

clima()