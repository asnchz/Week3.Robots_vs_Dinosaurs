from Dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def dinosaur_herd(self):
        dino1 = Dinosaur("T-Rex")
        dino2 = Dinosaur("Raptor")
        dino3 = Dinosaur("Triceratop")

        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)
