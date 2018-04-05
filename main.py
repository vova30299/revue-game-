nothing = 0 #ничего
rock = 1 #скала
shrimp = 2 #креветка
fish = 3 #рыба
animals = []
loneliness = []
loneliness.append(2)
loneliness.append(2)
many = []
many.append(4)
many.append(4)
animals.append(shrimp)
animals.append(fish)
select = 0
while (select != 3):
  print("МЕНЮ:")
  print("1 - запустить игру")
  print("2 - добавить животное")
  print("3 - выход")
  select = int(input())
  if (select == 1):
    print("Введите количество поколений")
    number_of_generations = int(input())
    print("Введите размеры океана")
    length, width = input().split(' ')
    length = int(length)
    width = int(width)
    ocean = []
    new_ocean = []
    ocean.append([0] * (width + 2))
    new_ocean.append([0] * (width + 2))
    print("Введите начальное состояние океана")
    for i in range(0, length):
      events = [0]
      events = events + map(int, input().split(' '))
      events = events + [0]
      subevents = [0] * (length + 2)
      new_ocean.append(subevents)
      ocean.append(events)
    ocean.append([0] * (width + 2)) 
    new_ocean.append([0] * (width + 2)) 
    length += 2
    width += 2
    count_animals = len(animals)
    for q in range (0, number_of_generations):
      for i in range(1, length - 1):
        for j in range(1, width - 1):
             neighbors = 0
             if (ocean[i - 1][j - 1] == ocean[i][j]):
                neighbors += 1
             if (ocean[i - 1][j] == ocean[i][j]):
                neighbors += 1
             if (ocean[i - 1][j + 1] == ocean[i][j]):
                neighbors += 1
             if (ocean[i][j - 1] == ocean[i][j]):
                neighbors += 1
             if (ocean[i][j + 1] == ocean[i][j]):
                neighbors += 1
             if (ocean[i + 1][j - 1] == ocean[i][j]):
                neighbors += 1
             if (ocean[i + 1][j] == ocean[i][j]):
                neighbors += 1
             if (ocean[i + 1][j + 1] == ocean[i][j]):
                neighbors += 1
             if (animals.count(ocean[i][j]) != 0):
                if (neighbors >= many[animals.index(ocean[i][j])]):
                   new_ocean[i][j] = nothing
                if (neighbors < loneliness[animals.index(ocean[i][j])]):
                   new_ocean[i][j] = nothing
                if (neighbors < many[animals.index(ocean[i][j])]):
                   if (neighbors >= loneliness[animals.index(ocean[i][j])]):
                      new_ocean[i][j] = ocean[i][j]
             if (ocean[i][j] == rock):
                new_ocean[i][j] = ocean[i][j]
             if (ocean[i][j] == nothing): 
                neighbors_animals = [0] * count_animals
                for k in range(0, count_animals):
                   if (ocean[i - 1][j - 1] == animals[k]):
                      neighbors_animals[k] += 1
                   if (ocean[i - 1][j] == animals[k]):
                      neighbors_animals[k] += 1
                   if (ocean[i - 1][j + 1] == animals[k]):
                      neighbors_animals[k] += 1
                   if (ocean[i][j - 1] == animals[k]):
                      neighbors_animals[k] += 1
                   if (ocean[i][j + 1] == animals[k]):
                      neighbors_animals[k] += 1
                   if (ocean[i + 1][j - 1] == animals[k]):
                      neighbors_animals[k] += 1
                   if (ocean[i + 1][j] == animals[k]):
                      neighbors_animals[k] += 1
                   if (ocean[i + 1][j + 1] == animals[k]):
                     neighbors_animals[k] += 1
                if (neighbors_animals.count(3) > 0):
                  new_ocean[i][j] = animals[neighbors_animals.index(3)]
    ocean = new_ocean
    ocean.pop(length - 1)
    ocean.pop(0)
    for c in range(0, length - 2):
       ocean[c].pop(0)
       ocean[c].pop(width - 2)
    for row in ocean:
      print(' '.join([str(elem) for elem in row]))
  if (select == 2):
    new_animal = len(animals) + 1
    print("Вы добавили животное под номером:")
    print(new_animal)
    print("Введите минимально допустимое число соседей этого же вида:")
    few = int(input())
    loneliness.append(few)
    print("Введите максимально допустимое число соседей этого же вида:")
    most = int(input())
    many.append(most)
    animals.append(new_animal)