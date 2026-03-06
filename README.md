
# GESTION DE HERRAMIENTAS🔧📦

**Versión 2026  Python**

Una aplicacion desarrollada en python para gestionar el control de herramientas, registrando entradas, salidas, y ajustes con auditoría de cada operación. Diseñada para los habitantes del barrio que requieren trazabilidad completa de movimientos de stock.

---

## 🧩 Problemática que resuelve 👥

Barrio con múltiples herramientas necesitan:
- Registrar movimientos de productos (entradas, salidas, ajustes).
- Validar operaciones según disponibilidad y estado.
- Mantener un historial completo 
- Evitar inconsistencias en stock ante errores o anulaciones.

---

## ✨ Funcionalidades principales

- Gestión de herramientas, categorías.
- Registro de movimientos de stock y estado.
- Auditoría automática de todas las operaciones CRUD en formato JSON.


---

```

---

## 🧠 Detalles técnicos destacados

- **Auditoría **: Cada cambio se registra en una entidad `Audit` con:
  - `EntityName`, `Operation`, `DataBefore`, `DataAfter`, `User`, `Date`.
  - Formato JSON completo antes y después del cambio.
  - Funciones específicas para `logInsert`, `logUpdate`, `logDelete`.
  - Uso de `@Transactional` para garantizar integridad.

- **Validaciones y reglas **:
  - Campos únicos verificados manualmente ( documento, nombres, apellidos, numeros de telefono ).
  - Manejo de estados automáticos (ej: producto agotado si stock = 0).
  - Prevención de eliminaciones que causen inconsistencias de stock.



---



---

## 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio

git clone https://github.com/orduzdarney-dot/gestion-herramientas.git

2. Entrar a la carpeta del proyecto

cd gestion-herramientas

3. Ejecutar la aplicación

python main.py
   ```


---

## 🧠 Autor 

Este proyecto fue completamente diseñado, modelado y desarrollado por [christofer orduz](mail to:orduzdarney@gmail.com) como parte de su portafolio profesional, incluyendo:




---


---

## 📫 Contacto

¿Dudas o sugerencias? Puedes escribirme a:

- 📧 correo.com
- 🌐 [LinkedIn]

