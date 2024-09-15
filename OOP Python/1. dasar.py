# di paython membuat class harus di atas sebelum program


class Hero:  # template
    pass


hero1 = Hero()  # object / instance
hero2 = Hero()
hero3 = Hero()

hero1.name = "aldi"  # type: ignore
hero1.health = 100  # type: ignore

hero2.name = "riky"  # type: ignore
hero2.health = 200  # type: ignore

hero3.name = "hawin"  # type: ignore
hero3.health = 200  # type: ignore

print(hero1)
print(hero1.__dict__)
print(hero1.name)  # type: ignore
