#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:38:00 2020

@author: avmejia
"""

import unittest

import duplicado


class Testprueba (unittest.TestCase):

    def test_codificacion(self):
        self.assertEqual(duplicado.elimina_duplicado("Hola amigos"),"Error tipo")
        self.assertEqual(duplicado.elimina_duplicado([1,2,3,1,4,2,5,6,1,9]),[1, 2, 3, 4, 5, 6, 9])
        self.assertEqual(duplicado.elimina_duplicado(["a",1,"b",2,"a",1,"c"]),['a', 1, 'b', 2, 'c'])
        

if __name__ == '__main__':
    unittest.main()
