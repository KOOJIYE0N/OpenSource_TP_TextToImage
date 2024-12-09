import os

class FileHandler:
    @staticmethod
    def create_directory(path):
        """
        Create a directory, ignore it if it already exists.
        :param path: 생성할 디렉토리 경로.
        """
        try:
            os.makedirs(path, exist_ok=True)
            print(f"Directory created or already exists: {path}")
        except Exception as e:
            print(f"Error creating directory {path}: {e}")

    @staticmethod
    def is_file_exists(file_path):
        """
        Verify that the file exists.
        :param file_path: 확인할 파일 경로.
        :return: 파일 존재 여부 (True/False).
        """
        return os.path.isfile(file_path)

    @staticmethod
    def delete_file(file_path):
        """
        Delete the file.
        :param file_path: 삭제할 파일 경로.
        """
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File deleted: {file_path}")
            else:
                print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")