# variáveis auxiliares para fazer a movimentação do rover no plateau
directions = ["N", "E", "S", "W"]
sides = {
    "left": "L",
    "right": "R"
}

class Rover():
    # posição e direção do rover
    position = (0, 0)
    direction = 0

    def __init__(self, x, y, direction, plateau):
        self.position = (x, y)
        self.direction = directions.index(direction)
        self.plateau = plateau

    def rotate(self, side):
        if side == sides["left"]:
            self.direction = (self.direction - 1) % 4
        else :
            self.direction = (self.direction + 1) % 4
    
    def move(self):
        x, y = self.position
        if directions[self.direction] == "N":
            if y >= self.plateau.size[1]:
                raise ValueError("Unable to go North")
            self.position = (x, y + 1)
        elif directions[self.direction] == "E":
            if x >= self.plateau.size[0]:
                raise ValueError("Unable to go East")
            self.position = (x + 1, y)
        elif directions[self.direction] == "S":
            if y <= 0:
                raise ValueError("Unable to go South")
            self.position = (x, y - 1)
        elif directions[self.direction] == "W":
            if x <= 0:
                raise ValueError("Unable to go West")
            self.position = (x - 1, y)
        else :
            raise ValueError("Direction not found")

    def runCommands(self, commands):
        for command in commands:
            if command == "M":
                self.move()
            else :
                self.rotate(command)

    def __str__(self):
        return "%d %d %s\n" % (self.position[0], self.position[1], directions[self.direction])

