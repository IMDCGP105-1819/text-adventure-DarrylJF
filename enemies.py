class Enemy(object):
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class room_1_enemy(Enemy):
    def __init__(self):
        super().__init__(name="Squatter",
                         hp=10,
                         damage=25)


class room_2_enemy(Enemy):
    def __init__(self):
        super().__init__(name="Robber",
                         hp=80,
                         damage=25)