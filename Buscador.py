import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

class GoogleScraper:
    def __init__(self, query, num_results=10):
        self.query = query
        self.num_results = num_results
        self.base_url = "https://www.google.com/search?q="

    def get_search_url(self):
        """Genera la URL de búsqueda en Google con la consulta proporcionada."""
        return f"{self.base_url}{quote_plus(self.query)}&num={self.num_results}"

    def fetch_results(self):
        """Obtiene el contenido HTML de la página de resultados de búsqueda."""
        url = self.get_search_url()
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            response.raise_for_status()  # Verifica que la solicitud fue exitosa
            return response.text
        except requests.RequestException as e:
            print(f"Error al realizar la solicitud: {e}")
            return None

    def parse_results(self, html):
        """Analiza el HTML para extraer enlaces y títulos de los resultados de búsqueda."""
        soup = BeautifulSoup(html, 'html.parser')
        results = []

        # Encuentra todos los elementos que son resultados de búsqueda
        for g in soup.find_all('div', class_='g'):
            title = g.find('h3')
            link = g.find('a')

            if title and link:
                results.append({
                    'title': title.text,
                    'link': link['href']
                })
        return results

    def scrape(self):
        """Maneja el flujo de trabajo del scrapper, desde la obtención de resultados hasta su análisis."""
        html = self.fetch_results()
        if html:
            results = self.parse_results(html)
            return results
        return []

# Ejemplo de uso
if __name__ == "__main__":
    query = "Python programming"
    scraper = GoogleScraper(query)
    results = scraper.scrape()

    # Imprimir resultados
    for result in results:
        print(f"Título: {result['title']}\nEnlace: {result['link']}\n")