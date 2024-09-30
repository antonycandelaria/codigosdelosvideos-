def message_creator(text):
   # Escribe tu solución 👇
   match text:
      case "computadora":
         return "Con mi computadora puedo programar usando Python"
      case "celular":
         return "En mi celular puedo aprender usando la app de Platzi"
      case "cable":
         return "¡Hay un cable en mi bota!"
   return 'Artículo no encontrado'

text = 'cable'
response = message_creator(text)
print(response)