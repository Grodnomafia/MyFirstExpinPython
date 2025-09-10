def demo():
      while True:
            demo_text = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')
            if '{name}' in demo_text and '{age}' in demo_text:
                  break
            else:
                  print('Ошибка отсуствует одна или две конструкции')

      name_text = input('Список людей через запятую: ').split(', ')

      age_text =input('Возраст людей через пробел: ').split()
      if len(name_text) != len(age_text):
            print('Ошибка: количество людей и возрастов не совпадает!')
            return


      for i in range(len(name_text)):
            total_text = demo_text.format(name = name_text[i] , age = age_text[i])
            print(total_text)
      people = [' '.join([name_text[i], age_text[i]]) for i in range(len(name_text))]
      print()
      people = ', '.join(people)
      print(f'Имениники : {people}')



demo()
