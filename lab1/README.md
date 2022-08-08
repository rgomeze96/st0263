Tópicos de Telemática ST0263
Laboratorio 1
Rafael Gomez

Usé https://realpython.com/python-sockets/ para poder construir ese proyecto.

Para poder interactuar con el servidor de HTTP a través de AWS me debes contactar para la IP elástica.

Requisitos para correr el servidor: Python 3.6+ 

Para correr el servidor en la máquina local sigues los siguientes pasos:
  1. En la carpeta donde deseas abres Visual Studio Code.
  2. En la parte de extensiones instalas Python para VS Code, está publicado por Microsoft.
  3. Abres un terminal y pegas: "git clone https://github.com/rgomeze96/st0263.git ." (con el punto al final)
  4. Corres el comando: "cd lab1"
  5. Corres el comando: "python /http_server.py" (Usando windows y corriendo en local no se puede usar puerto 80 por permisos).
  5. Abres un navegador y pegas: "localhost:8080"

Detalles de diseño:
  Eso es un servidor http implementado usando sockets en Python. Cuando el servidor está activado en AWS usa el puerto 80 entonces solamente toca ingresar la IP elástica y el servidor muestra los recursos.

Detalles Técnicos:
  Cuando no hay un recurso en la URL el servidor entrega el index.html archivo que tiene enlaces para ver otros recursos. Hay un archivo de PDF y 3 imágenes para probar distintos tipos archivos. Las URLS son: /mr-robot.webp, /mr-robot.jpg, /test.jpg (no tiene enlace en el index.html para mostrar que no solamente funciona con enlace), y todos los recursos se puede recoger sin la necesidad de un enlace. Si una URL ingresada no corresponde a un recurso el servidor retorna un error de 404 y muestra un error al usuario demostrando que el archivo no se encuentra "Error 404 File Not Found". El servidor también decodifica el request y imprime el HTTP REQUEST y tambien el HTTP Response antes que se hace el encode y enviarlo al cliente.

El códgio está disponible en un repo público de Github: "https://github.com/rgomeze96/st0263/tree/master/lab1".
