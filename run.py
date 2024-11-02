import os
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile
import logging


logger = logging.getLogger(__name__)


script_dir = Path(__file__).parent
bin_dir = script_dir / "bin"
jdk_zip_path = bin_dir / "bellsoft-jdk17.0.13+12-macos-amd64-full.zip"
java_home_dir = bin_dir / "jdk-17.0.13-full.jdk"
jvm_path = java_home_dir / "bin" / "java"
oraja_zip_path = bin_dir / "beatoraja0.8.8-modernchic.zip"
oraja_dir = bin_dir / "beatoraja0.8.8-modernchic"
oraja_launcher_path = oraja_dir / "beatoraja-config.command"
jar_path = oraja_dir / "beatoraja.jar"


def download_file(url: str, destination: Path, buffer_size: int = 1048576):
    with urlopen(url) as response:
        with destination.open("wb") as destination_file:
            while True:
                buffer = response.read(buffer_size)
                if not buffer:
                    break
                destination_file.write(buffer)


def check_jdk():
    return java_home_dir.exists()


def install_jdk():
    download_file("https://download.bell-sw.com/java/17.0.13+12/bellsoft-jdk17.0.13+12-macos-amd64-full.zip", jdk_zip_path)
    with ZipFile(jdk_zip_path) as archive:
        archive.extractall(bin_dir)
    jvm_path.chmod(0o755)


def check_beatoraja():
    return jar_path.exists()


def install_beatoraja():
    download_file("https://mocha-repository.info/download/beatoraja0.8.8-modernchic.zip", oraja_zip_path)
    with ZipFile(oraja_zip_path) as archive:
        archive.extractall(bin_dir)
    oraja_launcher_path.chmod(0o755)


def main():
    if not check_jdk():
        logger.info("JDK not found. Installing.")
        install_jdk()
    if not check_beatoraja():
        logger.info("beatoraja not found. Installing.")
        install_beatoraja()

    logger.info("Launching beatoraja.")
    env = os.environ.copy()
    env["JAVA_HOME"] = str(java_home_dir)
    os.chdir(oraja_dir)
    os.execve("beatoraja-config.command", ["beatoraja-config.command"], env)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
