"""Cambiar valores"""
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0] = 15
estudiantes[0]["last_name"] = "Bryant"
directorio_deportes["fútbol"][0] = "Andres"
z[0]['y'] = 30

print(x)
print(estudiantes)
print(directorio_deportes)
print(z)
