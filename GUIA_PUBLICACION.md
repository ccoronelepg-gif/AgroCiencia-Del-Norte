# Publicar AgroCiencia Del Norte, web independiente

**Nombre web:** AgroCiencia Del Norte  
**Repositorio independiente:** `ccoronelepg-gif/AgroCiencia-Del-Norte`  
**Dirección prevista — todavía no verificada:** https://ccoronelepg-gif.github.io/AgroCiencia-Del-Norte/

## Paso 1. Crear un repositorio nuevo en GitHub

Abrir el enlace preconfigurado:
https://github.com/new?owner=ccoronelepg-gif&name=AgroCiencia-Del-Norte&description=Plataforma%20cientifica%20agricola%20del%20norte%20del%20Peru&visibility=public

Comprobar propietario `ccoronelepg-gif`; seleccionar **Public**, habilitar **Add a README file** y crear el repositorio. No elegir OAF-Lambayeque como destino de archivos.

## Paso 2. Cargar el contenido de este paquete

Descomprimir el ZIP y subir a la raíz de `main` **todos los archivos y subcarpetas**: `index.html`, `herramientas/`, `datos/`, `tests/`, `.github/workflows/`, `.nojekyll` y `README.md`. No subir el ZIP como único archivo.

Para publicar mediante Git desde una terminal, clonar primero el repo con README inicial, copiar el contenido del ZIP y ejecutar:

```bash
git add .
git commit -m "Publicar AgroCiencia Del Norte v2.1"
git push origin main
```

## Paso 3. Activar GitHub Pages

En el repositorio nuevo, abrir `Settings > Pages > Build and deployment` y elegir **GitHub Actions** como origen de la publicación. El paquete incluye `.github/workflows/publicar-github-pages.yml` y su prueba de integridad. En `Actions`, observar el resultado del flujo `Publicar AgroCiencia Del Norte en GitHub Pages`. Si falla por no estar activado Pages durante el primer push, volver a ejecutar el flujo desde su pestaña de acciones.

## Paso 4. Comprobar

Revisar la dirección publicada que GitHub muestra en `Settings > Pages`; abrir el menú, el observatorio, el buscador de AgroSanidad y los accesos externos a OAF. Probar también en un teléfono.

## Separación de repositorios

- **AgroCiencia Del Norte:** su propia página y repositorio.
- **AgroSanidad Norte:** módulo científico consultivo incluido sin tocar sus fuentes originales.
- **OAF Lambayeque:** proyecto y dominio propios, sin modificación.

**Estado de esta entrega:** archivos preparados; publicación en producción depende de la creación del repositorio y activación de Pages. La conexión GitHub disponible desde ChatGPT no permite crear repositorios ni modificar la opción Pages. Una vez creado el repo nuevo, puede autorizarse su acceso a la conexión GitHub para cargar los archivos aquí.