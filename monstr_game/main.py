from monsters import Goblins,Ork
from heroes import Tank,Healer



def battle():

    heroes =[Tank('Танк'),Healer('Лекарь')]
    monsters = [Goblins('Гоблин'), Ork('Орк')]
    round_rum = 1

    while True:
        print("\n📊 СТАТУС:")
        print(f'Раунд {round_rum}')
        print("Герои:")
        for hero in heroes:
            if hero.alive:
                print(f"  {hero.name}: {hero.health} /{hero.max_health}HP")



        print("\nМонстры:")
        for monstr in monsters:
            if monstr.alive:
                print(f"  {monstr.name}: {monstr.health} /{monstr.max_health}HP")


        print("\n⚔️ ХОД ГЕРОЕВ:")
        for hero in heroes:
            if hero.alive:
                hero.make_move(heroes, monsters)


        monsters = [m for m in monsters if m.alive]
        if not monsters:
            print("\n" + "=" * 50)
            print("🎉 ПОБЕДА! Все монстры побеждены!")
            print("=" * 50)
            break
        print('\n Ход монстров:')
        for monstr in monsters:
            if monstr.alive:
                monstr.make_move(monsters,heroes)

            if not heroes:
                print("\n" + "=" * 50)
                print("🎉 ПОБЕДА! Все монстры побеждены!")
                print("=" * 50)
                break

        heroes = [h for h in heroes if h.alive]
        round_rum += 1

    print(f"\n📈 ИТОГИ БИТВЫ:")
    print(f"Битва длилась {round_rum} раундов")
    print(f"Выжило героев: {len(heroes)}")
    print(f"Убито монстров: {5 - len(monsters)}")

if __name__ == "__main__":
    battle()