# Verificación de AgroCiencia Del Norte v2.1 integrada

Fecha de preparación: 28/10/2026 (Perú).

## Superadas

- Integridad ZIP sin archivos corruptos y rutas locales conservadas.
- Validación sintáctica de todos los bloques JavaScript mediante `node --check`.
- Cinco pruebas automáticas de integridad en `tests/verificar_integracion.py` (navegación, IDs, rutas, catálogo de 120 registros reales, siete cultivos, puente entre módulos y advertencias).
- Pruebas unitarias aisladas de las funciones heredadas: URL Open-Meteo, rechazo de datos diarios incompletos, representación de gráfico con/sin datos, normalización textual y conversión UTM a coordenadas geográficas.
- Datos de búsqueda derivados directamente del JSON incrustado en AgroSanidad Norte v1.1. No se han generado registros artificiales.

## Pendiente de comprobación visual y de servicios externos

- El navegador automatizado de este entorno rechaza las direcciones incluso locales por una política administrativa (`URLBlocklist: *`). Por ello NO se afirma que haya pasado un test end-to-end de usuario, ni un test visual responsive en navegador real.
- La disponibilidad y el contenido en tiempo real de Open-Meteo requieren una comprobación desde un sitio desplegado con internet.
- OAF Lambayeque está conectado como página remota externa; su embebido puede ser bloqueado por políticas del navegador o de la página. La aplicación ofrece apertura directa como alternativa.
- Las imágenes de Wikimedia Commons dependen de la disponibilidad de los archivos en sus respectivas páginas fuente.

## Recomendación de aceptación antes de operar

1. Publicar el ZIP completo en GitHub Pages (raíz del repositorio independiente).
2. Abrir el panel principal y comprobar imágenes reales, menú y accesibilidad en escritorio/móvil.
3. En `#integraciones`, seleccionar cultivo `Café`, coordenadas `-6.7714, -79.8409`; aplicar y comprobar que AgroSanidad muestre `Café` y que el observatorio cambie el punto.
4. Buscar `roya` y comprobar los resultados y sus alertas de vigencia regulatoria.
5. Entrar en `OAF Lambayeque` y verificar el panel; usar el botón de pestaña nueva si el navegador bloquea el marco.
6. Consultar un pronóstico de siete días real y verificar la fecha de la actualización; repetir en móvil.
7. Confirmar siempre productos y condiciones vigentes en SENASA SIGIA antes de utilizarlos.

## Cambios del sitio v2.1
- Nombre comercial y metadatos, cabecera, navegación, exportación de consultas, enlaces de publicación actualizados a **AgroCiencia Del Norte**.
- Prueba adicional de marca y separación del repositorio OAF.
- Publicación efectiva en Internet **pendiente**: no existe repositorio nuevo accesible mediante la conexión del usuario.

## Comprobación adicional de accesibilidad HTTP de la versión renombrada

- `http.server` local: respuesta **HTTP 200** para `index.html`.
- Chromium automatizado: el entorno de ejecución devuelve `net::ERR_BLOCKED_BY_ADMINISTRATOR` al abrir `127.0.0.1`; no hay confirmación de pruebas interactivas completas ni de presentación móvil.
- Publicación remota: no se puede verificar todavía un despliegue en el repositorio independiente porque no existe bajo la instalación GitHub conectada.