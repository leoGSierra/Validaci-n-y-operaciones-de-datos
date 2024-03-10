{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7b77c447-2f28-446b-add1-67b8209b7bab",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#VALIDAR LONGITUD DE UNA PALABRA.\n",
    "#El siguiente programa valida la longitud de una palabra intoducida por el usuario\n",
    "#si la palabra tiene mas de 8 caracteres o menos de 4 el codigo se repite \n",
    "#hasta que se introdusca una palabra dentro de 4 y 8 caracteres.\n",
    "\n",
    "def validar_longitud():\n",
    "    while True:\n",
    "        palabra = input(\"Ingrese una palabra: \")\n",
    "        longitud = len(palabra)\n",
    "        if longitud >= 4 and longitud <= 8:\n",
    "            print(\"La palabra es correcta\")\n",
    "            break\n",
    "        elif longitud < 4:\n",
    "            print(f\"Hacen falta letras. Solo tiene {longitud} letra(s).\")\n",
    "        else:\n",
    "            print(f\"Sobran letras. Tiene {longitud} letra(s).\")\n",
    "\n",
    "validar_longitud()\n",
    "\n",
    "\n",
    "\n",
    "#ENCUENTRA EL CUADRANTE\n",
    "#El siguiente codigo localiza por medio de coordenadas dadas por el usuario\n",
    "#la ubicasion de un punto en un plano cartesiano\n",
    "#primero llamamos a la funcion e introducimos las coordenadas a ubicar.\n",
    "\n",
    "def ubicar_coordenadas(x,y):\n",
    "    if x > 0 and y > 0:\n",
    "        return \"Se encuentra en el cuadrante I\"\n",
    "    elif x < 0 and y > 0:\n",
    "        return\"Se encuentra en el cuadrante II\"\n",
    "    elif x < 0 and y < 0:\n",
    "        return \"Se encuentra en el cuadrante III\"\n",
    "    elif x > 0 and y < 0:\n",
    "        return \"Se encuentra en el cuadrante IV\"\n",
    "    elif x == 0 and y != 0:\n",
    "        return \"Se encuentra sobre el eje Y\"\n",
    "    elif y == 0 and x !=0:\n",
    "        return \"Se encuentra sobre el eje X\"\n",
    "    else:\n",
    "        return \"Se encuentra en el origen\"\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54c9ec4c-8b03-4bbf-b247-6f7e7cb1e91e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
