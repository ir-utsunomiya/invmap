class ProcessedData():
    """Processing Data 

    """
    def __init__(self,X,Z,mac_address_dict):
        """Initializer

        Args:
            X (ndarray): XY coordinates
            Z (ndarray): wifi signal strength
            mac_address_dict (ndarray): macadress dict
        """
        self.data = {'X':X, 'Y':Z, 'Var':Z}
        self.nm = X.shape[0]
        self.all_mac_dict = mac_address_dict