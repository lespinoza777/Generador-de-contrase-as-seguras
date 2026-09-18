#  Secure Password Generator (Escritorio / Python)

Una aplicación de escritorio ligera, limpia y enfocada en la seguridad para generar contraseñas robustas de manera local. 

Desarrollé este proyecto para practicar desarrollo en Python y aplicar conceptos reales de ciberseguridad, priorizando la criptografía adecuada y una interfaz gráfica funcional.

## Enfoque Técnico y Seguridad
A diferencia de los generadores básicos que utilizan la librería común `random` (la cual es predecible y no apta para seguridad informática), este script implementa el módulo nativo **`secrets`**. Esto garantiza una verdadera entropía criptográfica para la creación de credenciales seguras.

##  Características
- **Criptografía segura:** Uso de `secrets.choice` para la selección aleatoria de caracteres.
- **Interfaz Gráfica Nativa (GUI):** Desarrollada con `Tkinter`, ligera y optimizada para entornos Linux (Debian).
- **Validación defensiva:** Longitud mínima configurable de 8 caracteres para mitigar claves débiles.
- **Funcionalidad de copiado:** Botón integrado para transferir la contraseña directamente al portapapeles con un solo clic.
