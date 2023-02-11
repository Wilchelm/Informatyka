#ifndef LISTA_H
#define LISTA_H

template <class T> 
  class Lista {
    public:
          Lista();
          void wstawElement(T element);
          T podajElement(int index);
    private:
      T _dane[100];
      int _rozmiar;
  };

#endif
