from random import randint


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10**n) - 1
    return randint(range_start, range_end)


def generate_file_name()->str:
    """generates file unique file name"""
    return str(random_with_N_digits(5)) + ".csv"


class SdLogger:
    """Class for logging data to CSV"""

    def __init__(self,batch_size:int=1000, headers:str=None,file_name:str=None, path:str="/sd/",overwrite:bool=False):
        self.batch_size = batch_size
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = generate_file_name()  # Generates 5 digits unique name for each file
        self.file_path = path + self.file_name
        if overwrite:
            self.file = open(self.file_path, "w")
        else:
            self.file = open(self.file_path, "a")
        if headers:
            self.set_headers(headers)
        self.index = 0

    def set_headers(self, header):
        """Sets the headers for CSV file"""
        self.file.write(header)
        self.file.write("\r\n")

    def log_data(self, data):
        """Logs the data to the current CSV file"""
        data = str(self.index) + "," + data  # adding index
        self.index += 1
        self.file.write(data)  # Logging data
        self.file.write("\r\n")  # new line
        if self.index % self.batch_size == 0:
            self.save_recorded_data_to_file()

    def save_recorded_data_to_file(self):  # fail safe for power lost - saving data on every 1000th read
        self.file.close()
        self.file = open(self.file_path, "a")

    def close(self):
        """Closing the file and destructing the object"""
        self.file.close()
        del self
