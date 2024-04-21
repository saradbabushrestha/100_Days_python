letter = "Hey my name is {} and I am from {}"
country="Nepal"
name="Sarad"


print(letter.format(name,country))

print(f"Hey my name is {name} and I am from {country}")

print(f"we use f-string like this : Hey my name is {{name}} and I am from {{country}}")


price=49.0999
txt=f"For only{price: .2f} dollars!"
print(txt)

print(f"{2*30}")