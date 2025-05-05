import requests

from settings import API_KEY, LAT, LON

class GeoAPI():
    API_KEY = API_KEY
    LAT = LAT
    LON = LON

    @classmethod
    def is_temperature_greater_than_twenty_eight(
        self,
        temperature: float
    ) -> bool:
        '''
        Funcion encargada de verificar si la temperatura pasada por parametro es mayor
        a 28°C

        :param temperature `float`: Temperatura en grados Celcius.

        :return False `bool`si la temperatura es menor:
        :return True `bool`si la temperatura es mayor:
        '''
        return temperature > 28


    @classmethod
    def is_hot_in_pehuajo(self):
        """
        Funcion encargada de consultar el clima en pehuajo y determinar
        si la temperatura actual es mayor a 28°C (Method: GET)

        Returns:
        bool: True si la temperatura es mayor a 28°C,
        bool: False si la temperatura es menor a 28°C
        """
        
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={self.LAT}&lon={self.LON}&appid={self.API_KEY}&units=metric'
        
        try:
            req = requests.get(url=url)
            
            if req.status_code >= 400:
                return {
                'results': False,
                'temperature': None
            }
            
            if req.status_code == 200:
                data = req.json()

                temperature = data['main']['temp']
                
                result = self.is_temperature_greater_than_twenty_eight(
                    temperature=temperature
                )
                
                return {
                    'results': result,
                    'temperature': temperature
                }
            
        except requests.exceptions.RequestException:
            return {
                'results': False,
                'temperature': None
            }