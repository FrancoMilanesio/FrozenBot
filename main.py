import pandas as pd
import time
import os
import random

from services.geo_api_service import GeoAPI

class FrozenBot:
    _AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]
    _PRODUCT_DF = pd.DataFrame({
        "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
        "quantity": [3, 10, 0, 5]
    })

    def start(self):
        os.system('clear')
        time.sleep(1.5)

        print("Buscando temperatura en Pehuajo...")
        self._loading_bar(2, 0.1, clear=True)

        geoAPI = GeoAPI.is_hot_in_pehuajo()

        print("-" * 38)
        print("| Bienvenido a Heladerías Frozen SRL |")
        print("-" * 38)

        if geoAPI["temperature"]:
            print(f'\nLa temperatura en Pehuajo es de {geoAPI["temperature"]}°C')

        print("\nQué degustamos en este caluroso día?" if geoAPI['results'] else "\nQué degustamos en este templado día?")
        self._charge_product_name_and_quantity()

    def _loading_bar(self, total_time, interval, clear=False):
        current_time = 0
        while current_time < total_time:
            current_time += interval
            percentage = int(current_time / total_time * 100)
            bar = '[' + '=' * (percentage // 5) + '>' + '.' * (20 - (percentage // 5)) + ']'
            print(f"Cargando: {percentage}% {bar}", end='\r')
            time.sleep(interval)
        if clear:
            os.system('clear')

    def _charge_product_name_and_quantity(self, tries=3):
        while tries > 0:
            print(f"\nIntentos restantes: {tries}")
            tries -= 1

            product_name = input('\nIngrese el nombre del sabor: ').strip().lower()

            try:
                quantity = int(input("Ingrese cantidad: "))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

            print(f"\nBuscando sabor: {product_name} cantidad: {quantity}")
            self._loading_bar(2, 0.1, clear=True)
            self._show_products_table()

            if self._is_product_available(product_name, quantity):
                print(f"\n¡Stock disponible del sabor {product_name}!")
                self._charge_discount_code(product_name, quantity)
                return
            else:
                print(f"\nNo se encontró stock suficiente para {product_name}.")

        self._handle_failed_attempts()

    def _handle_failed_attempts(self):
        os.system('clear')
        print("\nDemasiados intentos fallidos. Mostrando productos con stock...\n")
        self._show_products_table()

        if input("\n¿Desea intentar nuevamente? [Y/N]: ").strip().lower() == 'y':
            self._loading_bar(2, 0.1, clear=True)
            self._charge_product_name_and_quantity(tries=1)
        else:
            os.system('clear')
            print('\nGracias por utilizar el Bot de Heladerías Frozen SRL!')

    def _charge_discount_code(self, product_name, quantity):
        while True:
            code = input('\nIngrese el código de descuento: ').strip()
            if len(code) >= 4 and code.isalnum():
                break
            print("Ingrese al menos 4 caracteres alfanuméricos.")

        print(f'\nValidando código: {code}')
        self._loading_bar(2, 0.1, clear=True)

        if self._validate_discount_code(code):
            print('¡Código validado correctamente!\n')
            time.sleep(1)
            print(f'\nConfirmando pedido: {product_name}, cantidad: {quantity}')
            self._loading_bar(3, 0.1)
            print(f'\n¡Pedido número {random.randint(1000, 9999)} confirmado con éxito!\n')
        else:
            print(f"\nCódigo de descuento '{code}' no válido. Intente nuevamente.")
            self._charge_discount_code(product_name, quantity)

    def _validate_discount_code(self, code):
        for valid_code in self._AVAILABLE_DISCOUNT_CODES:
            differences = sum(c1 != c2 for c1, c2 in zip(code, valid_code)) + abs(len(code) - len(valid_code))
            if differences < 3:
                return True
        return False

    def _is_product_available(self, product_name, quantity):
        matches = self._PRODUCT_DF.loc[self._PRODUCT_DF["product_name"].str.lower() == product_name]
        if not matches.empty:
            stock = matches.iloc[0]["quantity"]
            return 0 < quantity <= stock
        return False

    def _show_products_table(self):
        df = self._PRODUCT_DF.rename(columns={"product_name": "Sabores Disponibles", "quantity": "Cantidad"})
        tabla = df.to_string(index=False)
        linea = "-" * len(tabla.split("\n")[0])
        separador = "\n" + linea + "\n"
        tabla_formateada = tabla.replace("\n", separador)
        print(f"{linea}\n{tabla_formateada}\n{linea}")


if __name__ == "__main__":
    bot = FrozenBot()
    bot.start()
