cidades = [('Berlim',29) ,('Cairo',36) ,('Buenos Aires',19), ('Los Angeles',26) ,('Tokio',27) ,("Nova York",28) ,("Londres",22)]
print(cidades)


c_para_f = lambda dado:(dado[0],(9/5)* dado[1]+32)

print(list(map(c_para_f,cidades)))
