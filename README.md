# 🧊 FrozenBot - Bot Interactivo para Heladerías 🍦

Bienvenido a **FrozenBot**, un bot interactivo para la gestión de pedidos en heladerías que utiliza lógica condicional, validaciones, clima en tiempo real y experiencia conversacional para mejorar la atención al cliente.

## 📋 Descripción

FrozenBot es una aplicación en consola que simula un sistema de pedidos de helados. El bot:
- Consulta la temperatura actual en **Pehuajó** mediante la API de OpenWeather.
- Adapta la interacción del cliente según el clima.
- Permite seleccionar sabores disponibles.
- Valida códigos de descuento mediante comparación tolerante a errores.
- Confirma pedidos con una experiencia visual amigable (barra de carga, mensajes animados, etc).

## 🚀 Tecnologías Utilizadas

- 🐍 Python 3.10+
- 📦 [Pandas](https://pandas.pydata.org/)
- 🌍 [OpenWeather API](https://openweathermap.org/api)
- ⌛ Módulos estándar (`os`, `time`, `random`, `requests`, `input`)

## 📦 Estructura del Proyecto

frozen_bot/
│
├── main.py # Script principal con clase FrozenBot
├── services/
│ └── geo_api_service.py # Módulo con clase GeoAPI para consultar clima
├── requirements.txt # Dependencias del proyecto
└── README.md 

## ⚙️ Instalación y Ejecución

1. **Clona el repositorio**

```bash
git clone https://github.com/tuusuario/frozen_bot.git
cd frozen_bot

2. **Crea un entorno virtual (opcional pero recomendado)**

python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate     # En Windows

## 🔐 Configuración con variables de entorno

Este proyecto utiliza variables de entorno para ocultar datos sensibles. Asegúrate de crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
API_KEY=tu_clave_de_openweathermap
LAT
LON