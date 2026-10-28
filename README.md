# AgroCiencia Del Norte · Sitio web independiente v2.1

Plataforma científico-técnica para consulta agroclimática y fitosanitaria, independiente del proyecto **OAF Lambayeque**.

## Archivos
- `index.html`: página principal y herramientas de consulta meteorológica.
- `herramientas/agrosanidad-norte.html`: módulo documental AgroSanidad Norte v1.1, incluido como copia autónoma.
- `datos/agrosanidad-indice.json`: 120 fichas indexadas de siete cultivos, vinculadas a sus fuentes.
- `.github/workflows/`: verificación y despliegue automático por GitHub Pages.
- `tests/verificar_integracion.py`: verificación estática de integración, navegación y catalogación.

## Dirección pública esperada, NO publicada hasta verificar el despliegue
`https://ccoronelepg-gif.github.io/AgroCiencia-Del-Norte/`

## Publicación
1. Crear el repositorio público `ccoronelepg-gif/AgroCiencia-Del-Norte`, con un archivo README inicial en `main`.
2. Subir **el contenido** de esta carpeta a la raíz del nuevo repositorio. Es importante incluir la carpeta `.github` (oculta en algunos exploradores).
3. Entrar a `Settings > Pages` y seleccionar `Build and deployment > Source: GitHub Actions`.
4. En `Actions` comprobar la ejecución `Publicar AgroCiencia Del Norte en GitHub Pages`; volver a lanzarla si fue ejecutada antes de activar Pages.
5. Verificar la URL real anunciada por GitHub Pages y probar los módulos en escritorio y móvil.

## Advertencias
La conectividad de Open-Meteo requiere internet. OAF Lambayeque se enlaza como proyecto externo; no se modifican sus fuentes ni se afirma integración de modelos o datos que no exista. Las fichas fitosanitarias son documentales; comprobar autorizaciones vigentes en SENASA SIGIA antes de usar productos. El sitio no constituye diagnóstico profesional ni servicio oficial.