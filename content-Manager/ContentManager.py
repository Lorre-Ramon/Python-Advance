import pandas as pd 

class ExcelOpenner: 
    
    def __init__(self, file_path:str):
        self.file_path = file_path
        
    def __enter__(self):
        self.file = pd.read_excel(self.file_path)
        return self.file 
        print('File opened')
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.to_excel(self.file_path, index=False)
        print('File saved')
        
        if exc_type is not None:
            print('Error Caught:', exc_value)
            print("\nTraceback:", traceback)
            return True
        
if __name__ == '__main__':
    with ExcelOpenner('data.xlsx') as data:
        if True: 
            raise ZeroDivisionError('Cannot divide by zero')
        print(data.info(), data.head()) 
        