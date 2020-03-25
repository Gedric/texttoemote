Text = input("Give input ")
Text = Text.lower()
new_text = str()
for i in Text:
    if i == " ":
        new_text = new_text+"     "
    else:
        new_text = new_text+(" :regional_indicator_"+i+":")
print(new_text)
input()