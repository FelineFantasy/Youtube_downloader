import yt_dlp
import subprocess
import os
import shutil

def check_ffmpeg():
    """Проверяет, установлен ли ffmpeg в системе."""
    return shutil.which("ffmpeg") is not None

def progress_hook(d):
    """Выводит прогресс загрузки."""
    if d['status'] == 'downloading':
        progress = d.get('_percent_str', '0%').strip()
        speed = d.get('_speed_str', '0 MB/s').strip()
        eta = d.get('_eta_str', '?').strip()
        print(f"\rЗагрузка: {progress} | Скорость: {speed} | Осталось: {eta}", end="")
    elif d['status'] == 'finished':
        print("\nЗагрузка завершена!")

def get_quality_choice():
    """Показывает меню выбора качества и возвращает формат."""
    print("\nВыберите качество:")
    print("1. Лучшее (до 4K)")
    print("2. 1080p (Full HD)")
    print("3. 720p (HD)")
    print("4. 480p")
    print("5. 360p")
    print("6. Только аудио (M4A)")
    print("7. Конвертировать в MMPGEF")

    choice = input("Ваш выбор (1-7): ").strip()

    formats = {
        "1": "best",
        "2": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
        "3": "bestvideo[height<=720]+bestaudio/best[height<=720]",
        "4": "bestvideo[height<=480]+bestaudio/best[height<=480]",
        "5": "bestvideo[height<=360]+bestaudio/best[height<=360]",
        "6": "bestaudio[ext=m4a]",
        "7": "best",
    }

    return formats.get(choice, "best"), choice

def convert_to_mmpgef(input_file, output_file):
    """Конвертирует видео в формат mmpgef с помощью ffmpeg."""
    print("\nКонвертация в MMPGEF...")
    try:
        audio_input = input_file.replace('.mp4', '.m4a')
        if os.path.exists(audio_input):
            subprocess.run([
                'ffmpeg', '-i', input_file, '-i', audio_input,
                '-c:v', 'libx264', '-c:a', 'aac',
                '-map', '0:v:0', '-map', '1:a:0',
                output_file + '.mmpgef'
            ], check=True)
            os.remove(audio_input)
        else:
            subprocess.run([
                'ffmpeg', '-i', input_file,
                '-c:v', 'libx264', '-c:a', 'aac',
                output_file + '.mmpgef'
            ], check=True)
        print("Конвертация в MMPGEF завершена!")
        os.remove(input_file)
    except Exception as e:
        print(f"Ошибка конвертации: {e}")

def main():
    if not check_ffmpeg():
        print("ffmpeg не найден!")
        print("Установите ffmpeg:")
        print("  Linux: sudo apt install ffmpeg  или  sudo pacman -S ffmpeg")
        print("  macOS: brew install ffmpeg")
        print("  Windows: скачайте с ffmpeg.org и добавьте в PATH")
        return

    url = input("Вставьте ссылку на YouTube: ").strip()

    if not url:
        print("Ошибка: пустая ссылка!")
        return

    if "youtube.com" not in url and "youtu.be" not in url:
        print("Ошибка: неверная ссылка на YouTube!")
        return

    format_choice, choice = get_quality_choice()

    ydl_opts = {
        'format': format_choice,
        'quiet': True,
        'no_warnings': True,
        'progress_hooks': [progress_hook],
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
    }

    print("\nЗагрузка...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        print("Готово! Видео сохранено.")

        if choice == "7":
            base_name = os.path.splitext(filename)[0]
            convert_to_mmpgef(filename, base_name)

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
