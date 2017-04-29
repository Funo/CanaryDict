class canarydictionary:
    def searchword(self, param):
        diccionario = {'millo': 'maiz', 'papa': 'patata', 'baifo': 'cabra', 'godo': 'miguel'}
        return diccionario.get(param)
