from pydantic import BaseModel


class Fire(BaseModel):
    """
    Represents a passenger on the Titanic with various attributes.
    
    Attributes:
        SIZE (int): Placeholder for values in 'SIZE' attribute
        FUEL (object): Placeholder for values in 'FUEL' attribute
        DISTANCE (int): Placeholder for values in 'DISTANCE' attribute
        DESIBEL (int): Placeholder for values in 'DESIBEL' attribute
        AIRFLOW (float): Placeholder for values in 'AIRFLOW' attribute
        FREQUENCY (int): Placeholder for values in 'FREQUCENCY' attribute
    """

    SIZE: int  
    FUEL: str 
    DISTANCE:  int 
    DESIBEL:  int  
    AIRFLOW:  float
    FREQUENCY:  int  
    STATUS:  int  
    