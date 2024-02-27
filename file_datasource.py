from csv import reader
from datetime import datetime
from domain.accelerometer import Accelerometer
from domain.gps import Gps
from domain.aggregated_data import AggregatedData
import config


class FileDatasource:
    def __init__(
        self,
        accelerometer_filename: str,
        gps_filename: str,
    ) -> None:
        self.i = 0
        self.a_path = accelerometer_filename
        self.g_path = gps_filename
        self.a_data = None
        self.g_data = None

    def read(self) -> AggregatedData:
        """Метод повертає дані отримані з датчиків"""
        a_tup = self.a_data[self.i]
        g_tup = self.g_data[self.i]
        print(f"Iteration number: {self.i}\n")
        self.i += 1
        return AggregatedData(
            Accelerometer(a_tup[0], a_tup[1], a_tup[2]),
            Gps(g_tup[0], g_tup[1]),
            datetime.now(),
            config.USER_ID,
        )

    def startReading(self):
        """Метод повинен викликатись перед початком читання даних"""
        self.a_file = open(self.a_path, "r")
        self.g_file = open(self.g_path, "r")
        a_read = reader(self.a_file)
        g_read = reader(self.g_file)
        self.a_data = list(a_read)
        self.g_data = list(g_read)
        self.i += 1
        self.stopReading()

    def stopReading(self):
        """Метод повинен викликатись для закінчення читання даних"""
        self.a_file.close()
        self.g_file.close()
