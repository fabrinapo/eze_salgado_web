import sys
from pathlib import Path
from PIL import Image, UnidentifiedImageError

# Configuración del Pipeline
INPUT_DIR = Path('raw_assets')
OUTPUT_DIR = Path('public/img')
MAX_WIDTH = 1920
WEBP_QUALITY = 80
VIDEO_EXTENSIONS = {'.mov', '.avi', '.mkv', '.mp4'}
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png'}

def setup_directories():
    """Crea los directorios necesarios si no existen."""
    if not INPUT_DIR.exists():
        print(f"❌ Error: El directorio de entrada '{INPUT_DIR}' no existe.")
        sys.exit(1)
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"📂 Directorios configurados. Leyendo desde: {INPUT_DIR}")

def calculate_new_dimensions(width, height):
    """Calcula nuevas dimensiones manteniendo el aspect ratio."""
    if width <= MAX_WIDTH:
        return width, height
    
    ratio = MAX_WIDTH / width
    new_height = int(height * ratio)
    return MAX_WIDTH, new_height

def process_image(file_path):
    """Procesa, redimensiona y convierte una imagen a WebP."""
    try:
        with Image.open(file_path) as img:
            # Obtener nombre de archivo sin extensión
            file_stem = file_path.stem
            output_path = OUTPUT_DIR / f"{file_stem}.webp"

            # 1. Redimensionado Inteligente
            width, height = img.size
            if width > MAX_WIDTH:
                new_w, new_h = calculate_new_dimensions(width, height)
                # Usamos LANCZOS para la mejor calidad de reducción
                img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
                print(f"   ⬇️  Redimensionado: {width}x{height} -> {new_w}x{new_h}")
            
            # 2. Conversión y Guardado
            # WebP maneja transparencia (RGBA), así que no necesitamos convertir a RGB forzosamente
            img.save(output_path, format="WEBP", quality=WEBP_QUALITY, optimize=True)
            
            print(f"   ✅ Generado: {output_path} (Calidad: {WEBP_QUALITY}%)")
            return True

    except UnidentifiedImageError:
        print(f"   ⚠️  Advertencia: No se pudo identificar el formato de imagen de {file_path.name}")
    except OSError as e:
        print(f"   ❌ Error de I/O en {file_path.name}: {e}")
    except Exception as e:
        print(f"   ❌ Error inesperado procesando {file_path.name}: {e}")
    
    return False

def generate_ffmpeg_suggestion(file_path):
    """Genera un comando optimizado para videos pesados."""
    output_video = OUTPUT_DIR / f"{file_path.stem}.mp4"
    
    # Comando sugerido: H.264, preset slow (mejor compresión), CRF 23 (buen balance), sin audio si es background
    cmd = (
        f"ffmpeg -i {file_path} -c:v libx264 -preset slow -crf 23 "
        f"-c:a aac -b:a 128k -movflags +faststart {output_video}"
    )
    print(f"\n   📹 Video detectado: {file_path.name}")
    print(f"      Sugiero correr este comando manualmente para optimizarlo:")
    print(f"      >> {cmd}\n")

def main():
    setup_directories()
    
    files = list(INPUT_DIR.iterdir())
    if not files:
        print("⚠️  El directorio 'raw_assets' está vacío.")
        return

    print(f"🚀 Iniciando optimización de {len(files)} archivos...\n")
    
    processed_count = 0
    
    for file_path in files:
        if file_path.is_file():
            ext = file_path.suffix.lower()
            
            if ext in IMAGE_EXTENSIONS:
                print(f"⚙️  Procesando: {file_path.name}")
                if process_image(file_path):
                    processed_count += 1
            
            elif ext in VIDEO_EXTENSIONS:
                generate_ffmpeg_suggestion(file_path)

    print(f"\n✨ Proceso finalizado. {processed_count} imágenes optimizadas en '{OUTPUT_DIR}'.")

if __name__ == "__main__":
    main()