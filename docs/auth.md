# Autenticación con token

La autenticación que he implementado en el microservicio se basa en tokens.

Proceso de creación de usuario:
- Se genera un UUID único para ese usuario.
- Se cifra su contraseña con SHA256.

Proceso de login:
- Se comprueba si el usuario existe.
- Se comprueba el hash del password almacenado con el hash del que se introduce.
- En caso de ser correctas las credenciales se genera un token a partir del UUID del usuario y de una clave secreta. Además se le asigna un tiempo de expiración de 20 minutos.
- Se devuelve el token generado.

[**Almacenamiento de credenciales en la BD.**](bd.md)