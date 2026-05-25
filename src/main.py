"""
SISTEMA DE COSTOS ABC POR ÓRDENES DE TRABAJO
Empresa Demo: TechManufacturing S.A.
Versión: 1.0
"""

import sys
import os
from pathlib import Path

# Agregar directorio src al path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from ui.main_window import MainWindow
from PyQt5.QtWidgets import QApplication
from database.connection import initialize_database
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def main():
    """Punto de entrada principal de la aplicación"""
    try:
        # Inicializar base de datos
        logger.info("Inicializando base de datos...")
        initialize_database()
        
        # Crear aplicación PyQt5
        app = QApplication(sys.argv)
        
        # Crear y mostrar ventana principal
        logger.info("Iniciando interfaz gráfica...")
        window = MainWindow()
        window.show()
        
        sys.exit(app.exec_())
        
    except Exception as e:
        logger.error(f"Error al iniciar la aplicación: {str(e)}")
        raise

if __name__ == '__main__':
    main()
