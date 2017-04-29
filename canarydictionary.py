class canarydictionary:
    def searchword(self, param):
        diccionario = {'millo': 'maiz', 'papa': 'patata', 'baifo': 'cabra', 'godo': 'miguel', 'guagua': 'autobus'}
        return diccionario.get(param)
