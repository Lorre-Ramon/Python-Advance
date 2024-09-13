# 用不同的方法做一种事情

from abc import abstractmethod, ABC

class ProcessStrategy(ABC): 
    @abstractmethod
    def process(self, file_path: str) -> None:
        pass
    
class ExcelProcessor(ProcessStrategy):
    def process(self, file_path: str) -> None:
        print(f"Processing Excel file: {file_path}")
        
class CsvProcessor(ProcessStrategy):
    def process(self, file_path: str) -> None:
        print(f"Processing CSV file: {file_path}")
        
class JsonProcessor(ProcessStrategy):
    def process(self, file_path: str) -> None:
        print(f"Processing JSON file: {file_path}")
        
class FileProcessor:
    def __init__(self, file_path:str) -> None:
        self.file_path = file_path
        self.file_type = file_path.split('.')[-1] 
        
    def process_file(self) -> None:
        match self.file_type:
            case 'xls' | 'xlsx':
                ExcelProcessor().process(self.file_path)
            case 'csv':
                CsvProcessor().process(self.file_path)
            case 'json':
                JsonProcessor().process(self.file_path) 
                
if __name__ == '__main__':
    file_path = 'data.csv'
    file_processor = FileProcessor(file_path)
    file_processor.process_file()