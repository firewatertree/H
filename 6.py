richter=float(input("please input a richter scale value: "))
richter_scale_value=richter

energy=10**((1.5*richter)+4.8)

ton_of_exploded_TNT=energy/(4.184*10**9)
nutritious_luches=energy/(4.184*10**9)

print(richter)
print(richter_scale_value)
print(energy)
print(ton_of_exploded_TNT)
print(nutritious_luches)

