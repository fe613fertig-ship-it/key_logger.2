from typing import List
from abc import ABC, abstractmethod

class IKeyLogger(ABC):
    @abstractmethod
    def logging_start(self):
        """מתחיל האזנה להקשות"""
        pass

    @abstractmethod
    def logging_stop(self):
        """עוצר האזנה"""
        pass

    @abstractmethod
    def keys_logged_get(self) -> List[str]:
        """מחזיר רשימת ההקשות שנאספו"""
        pass