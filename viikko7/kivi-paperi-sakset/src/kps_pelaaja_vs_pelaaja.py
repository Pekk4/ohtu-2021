from kps import KPS


class KPSPelaajaVsPelaaja(KPS):
    def __init__(self):
        super().__init__()

    def _tokan_siirto(self):
        return input("Toisen pelaajan siirto: ")
