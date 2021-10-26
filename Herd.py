from Dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.dinosaur_herd()

    def dinosaur_herd(self):
        dino1 = Dinosaur("T-Rex", 50)
        dino2 = Dinosaur("Raptor", 50)
        dino3 = Dinosaur("Triceratop", 50)

        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)
