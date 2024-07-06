# goit-cs-hw-04

---

# Завдання 1

### Запуск
```
cd task_1
```
```
python main.py
```

### Результат
    Total files processed: 4
    Execution time: 0.0035109519958496094 seconds
    Keyword 'unchanged' found in files: ['..\\public\\text_1.txt']
    Keyword 'and' found in files: ['..\\public\\text_1.txt', '..\\public\\text_2.txt', '..\\public\\text_3.txt', '..\\public\\text_4.txt']
    Keyword 'Aldus' found in files: ['..\\public\\text_1.txt']
    Keyword 'passage' found in files: ['..\\public\\text_1.txt', '..\\public\\text_3.txt', '..\\public\\text_4.txt']
    Keyword 'accident' found in files: ['..\\public\\text_2.txt']
    Keyword 'opposed' found in files: ['..\\public\\text_2.txt']
    Keyword 'readable' found in files: ['..\\public\\text_2.txt']
    Keyword 'roots' found in files: ['..\\public\\text_3.txt']
    Keyword 'Sections' found in files: ['..\\public\\text_3.txt']
    Keyword 'College' found in files: ['..\\public\\text_3.txt']
    Keyword 'original' found in files: ['..\\public\\text_3.txt']
    Keyword 'suffered' found in files: ['..\\public\\text_4.txt']
    Keyword 'believable' found in files: ['..\\public\\text_4.txt']
    Keyword 'generators' found in files: ['..\\public\\text_4.txt']

--- 

## Завдання 2

### Запуск
```
cd task_2
```
```
python main.py
```

### Результат
    Total files processed: 4
    Execution time: 0.9685494899749756 seconds
    Keyword 'unchanged' found in files: ['..\\public\\text_1.txt']
    Keyword 'and' found in files: ['..\\public\\text_1.txt']
    Keyword 'Aldus' found in files: ['..\\public\\text_1.txt']
    Keyword 'passage' found in files: ['..\\public\\text_1.txt']
    Keyword 'accident' found in files: ['..\\public\\text_2.txt']
    Keyword 'opposed' found in files: ['..\\public\\text_2.txt']
    Keyword 'readable' found in files: ['..\\public\\text_2.txt']
    Keyword 'roots' found in files: ['..\\public\\text_3.txt']
    Keyword 'Sections' found in files: ['..\\public\\text_3.txt']
    Keyword 'College' found in files: ['..\\public\\text_3.txt']
    Keyword 'original' found in files: ['..\\public\\text_3.txt']
    Keyword 'suffered' found in files: ['..\\public\\text_4.txt']
    Keyword 'believable' found in files: ['..\\public\\text_4.txt']
    Keyword 'generators' found in files: ['..\\public\\text_4.txt']

---

# Висновок
Різниця в результатах між багатопотоковою та багатопроцесорною обробкою може бути пояснена наступним чином:

- **Синхронізація даних**: У багатопотоковій обробці потоки поділяють загальний адресний простір пам'яті, що полегшує 
доступ та оновлення загальних даних, таких як результати пошуку. Це дозволяє потокам ефективно оновлювати загальний 
результат без значних витрат на синхронізацію. У багатопроцесорній обробці кожен процес має власний адресний простір, 
і синхронізація даних між процесами вимагає використання механізмів взаємодії між процесами, таких як черги або об'єкти,
що розділяються, що може вносити додаткові витрати часу і зменшувати ефективність оновлення загальних даних.  
- **Час виконання**: Багатопотокова обробка зазвичай швидше багатопроцесорної через менші накладні витрати на створення 
потоків у порівнянні з процесами і більш ефективного обміну даними між потоками. У даному випадку час виконання 
багатопотокової обробки значно менший, що демонструє цю різницю.  
- **Результати пошуку**: У багатопотоковій обробці виявлено більше входження ключових слів, що може бути пов'язане з 
більш ефективною синхронізацією та оновленням загальних даних. У багатопроцесорній обробці можлива втрата деяких 
результатів через труднощі із синхронізацією або через те, що оновлення одного процесу перезаписуються оновленнями 
іншого процесу без належного контролю за порядком цих оновлень.
- **Використання ресурсів**: Багатопроцесорна обробка може бути більш вимогливою до ресурсів через необхідність 
додаткової пам'яті для кожного процесу і витрат на міжпроцесну взаємодію. Це може впливати на загальну продуктивність 
системи, особливо під час роботи з великою кількістю процесів.