class Address:
    def __init__(self,
                 name: str = "",
                 line1: str = "",
                 line2: str = "",
                 city: str = "",
                 state: str = "",
                 zip_code: str = ""
                 ):
        self.name: str = name
        self.line1: str = line1
        self.line2: str = line2
        self.city: str = city
        self.state: str = state
        self.zip_code: str = zip_code
