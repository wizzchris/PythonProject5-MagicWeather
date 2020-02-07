
while True:
    weather = input('What is the weather?------').strip().lower()
    if weather == 'no more magic':
        break
    else:
        if weather == 'sunny':
            print('take your shorts!')
        elif 'rainy' in weather and 'stormy' in weather:
            print('stay home')
        elif weather == 'stormy':
            print('take rain coat')
        elif weather == 'rainy':
            print('Take your umbrella')
        else:
            print("sorry, i didn't quite catch that")