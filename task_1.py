import asyncio
import os
import shutil
import argparse
import logging


async def read_folder(source_folder, output_folder):
    for root, _, files in os.walk(source_folder):
        for file in files:
            source_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1]
            output_path = os.path.join(output_folder, extension.strip("."), file)
            await copy_file(source_path, output_path)


async def copy_file(source_path, output_path):
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        shutil.copy(source_path, output_path)
        logging.info(f"Copied {source_path} to {output_path}")
    except Exception as e:
        logging.error(f"Error copying {source_path}: {e}")


async def main(source_folder, output_folder):
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    await read_folder(source_folder, output_folder)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Async file sorting script")
    parser.add_argument("source", type=str, help="Source folder path")
    parser.add_argument("output", type=str, help="Destination folder path")
    args = parser.parse_args()

    asyncio.run(main(args.source, args.output))
