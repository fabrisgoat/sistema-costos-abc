"""
Pestaña de Inventarios
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget,
    QTableWidgetItem, QMessageBox, QLabel, QComboBox
)
from PyQt5.QtCore import Qt
from database.connection import get_db
from database.models import MaterialPrima, Inventario
from core.valorization import ValorizacionInventario
import logging

logger = logging.getLogger(__name__)

class InventarioTab(QWidget):
    """Pestaña de gestión de inventarios"""
    
    def __init__(self):
        super().__init__()
        self.db = get_db()
        self.valorizacion = ValorizacionInventario()
        self.initUI()
        self.cargar_inventarios()
    
    def initUI(self):
        """Inicializa la interfaz"""
        layout = QVBoxLayout(self)
        
        # Botones de acción
        botones_layout = QHBoxLayout()
        
        btn_movimiento = QPushButton("➕ Registrar Movimiento")
        btn_movimiento.clicked.connect(self.nuevo_movimiento)
        botones_layout.addWidget(btn_movimiento)
        
        btn_refresh = QPushButton("🔄 Actualizar")
        btn_refresh.clicked.connect(self.cargar_inventarios)
        botones_layout.addWidget(btn_refresh)
        
        btn_reporte = QPushButton("📊 Reporte")
        btn_reporte.clicked.connect(self.generar_reporte)
        botones_layout.addWidget(btn_reporte)
        
        layout.addLayout(botones_layout)
        
        # Tabla de inventarios
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(7)
        self.tabla.setHorizontalHeaderLabels([
            "Código", "Nombre", "Cantidad", "Costo Unitario Promedio",
            "Valor Total", "Stock Mínimo", "Estado"
        ])
        layout.addWidget(self.tabla)
    
    def cargar_inventarios(self):
        """Carga el resumen de inventarios"""
        try:
            resumen = self.valorizacion.obtener_resumen_inventarios()
            
            self.tabla.setRowCount(len(resumen))
            
            for row, item in enumerate(resumen):
                self.tabla.setItem(row, 0, QTableWidgetItem(item['codigo']))
                self.tabla.setItem(row, 1, QTableWidgetItem(item['nombre']))
                self.tabla.setItem(row, 2, QTableWidgetItem(f"{item['cantidad']:.2f}"))
                self.tabla.setItem(
                    row, 3,
                    QTableWidgetItem(f"${item['costo_unitario_promedio']:.4f}")
                )
                self.tabla.setItem(
                    row, 4,
                    QTableWidgetItem(f"${item['valor_total']:.2f}")
                )
                self.tabla.setItem(row, 5, QTableWidgetItem(f"{item['stock_minimo']:.2f}"))
                
                color = "#ffcccc" if item['estado'] == 'BAJO' else "#ccffcc"
                self.tabla.item(row, 6).setText(item['estado'])
                self.tabla.item(row, 6).setBackground(color)
            
            self.tabla.resizeColumnsToContents()
            
        except Exception as e:
            logger.error(f"Error cargando inventarios: {str(e)}")
            QMessageBox.critical(self, "Error", f"Error: {str(e)}")
    
    def nuevo_movimiento(self):
        """Registra un nuevo movimiento de inventario"""
        QMessageBox.information(self, "Movimiento", "Funcionalidad en desarrollo")
    
    def generar_reporte(self):
        """Genera reporte de inventarios"""
        QMessageBox.information(self, "Reporte", "Funcionalidad en desarrollo")
